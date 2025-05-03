# simulation/simulate_sensor.py
import os
import time
import random
import logging
from logging.handlers import RotatingFileHandler
from tenacity import retry, wait_exponential, stop_after_attempt
import requests

# === Configuration ===
SENSOR_POLL_INTERVAL = float(os.getenv("SENSOR_POLL_INTERVAL", "5.0"))
SOILING_THRESHOLD = float(os.getenv("SOILING_THRESHOLD", "0.7"))
SERVER_URL = os.getenv("SERVER_URL", "http://server:5000/start_mission")

# === Logging Setup ===
logger = logging.getLogger("SensorSimulation")
logger.setLevel(logging.INFO)

# Rotating file handler
file_handler = RotatingFileHandler(
    'sensor_simulation.log',
    maxBytes=2*1024*1024,  # 2MB per file
    backupCount=2,
    encoding='utf-8'
)
file_handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
))

# Console handler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter(
    "%(levelname)s - %(message)s"
))

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

@retry(
    wait=wait_exponential(multiplier=1, min=2, max=10),
    stop=stop_after_attempt(3)
)
def trigger_mission(url: str) -> bool:
    """Send mission trigger with retry logic"""
    try:
        response = requests.post(
            url,
            json={"simulated": True},
            timeout=5
        )
        response.raise_for_status()
        logger.info("Mission triggered successfully")
        return True
    except Exception as e:
        logger.error("Mission trigger failed: %s", str(e))
        raise

def generate_sensor_data() -> float:
    """Generate realistic sensor data with occasional spikes"""
    base_value = random.uniform(0.3, 0.6)
    if random.random() < 0.1:  # 10% chance of spike
        return round(min(base_value + random.uniform(0.2, 0.5), 1.0), 2)
    return round(base_value, 2)

def main():
    """Main simulation loop"""
    logger.info("Starting sensor simulation | Threshold: %.2f | Interval: %.1fs", 
                SOILING_THRESHOLD, SENSOR_POLL_INTERVAL)
    
    try:
        while True:
            sensor_value = generate_sensor_data()
            logger.info("Current simulated soiling: %.2f", sensor_value)

            if sensor_value >= SOILING_THRESHOLD:
                logger.warning("Threshold exceeded (%.2f >= %.2f)", 
                               sensor_value, SOILING_THRESHOLD)
                try:
                    trigger_mission(SERVER_URL)
                    time.sleep(20)  # Extended delay post-trigger
                except Exception:
                    logger.error("Aborting mission trigger after retries")
            time.sleep(SENSOR_POLL_INTERVAL)
    
    except KeyboardInterrupt:
        logger.info("Simulation shutdown requested")
    finally:
        logger.info("Sensor simulation stopped")

if __name__ == "__main__":
    main()
