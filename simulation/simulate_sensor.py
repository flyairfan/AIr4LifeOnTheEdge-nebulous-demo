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
SOILING_THRESHOLD = float(os.getenv("SOILING_THRESHOLD", "0.7"))  # 0-1 scale
SERVER_URL = os.getenv("SERVER_URL", "http://server:5000/start_mission")

# === Logging Setup ===
logger = logging.getLogger("SensorSimulation")
logger.setLevel(logging.INFO)

# Rotating file handler (2MB files, keep 2 backups)
file_handler = RotatingFileHandler(
    'sensor_simulation.log',
    maxBytes=2 * 1024 * 1024,
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
    """Send mission trigger with retry logic."""
    try:
        # Simulate including a 'value' metric in the payload
        payload = {"simulated": True, "value": random.uniform(0.7, 1.0)}
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
        logger.info("Mission triggered successfully with payload: %s", payload)
        return True
    except Exception as e:
        logger.error("Mission trigger failed: %s", str(e))
        raise

def generate_sensor_data() -> float:
    """Generate realistic sensor data with occasional spikes."""
    base_value = random.uniform(0.3, 0.6)
    # 10% chance of an artificial spike
    if random.random() < 0.1:
        return round(min(base_value + random.uniform(0.2, 0.5), 1.0), 2)
    return round(base_value, 2)

def main():
    """Main simulation loop."""
    logger.info("Starting sensor simulation | Threshold: %.2f | Interval: %.1fs",
                SOILING_THRESHOLD, SENSOR_POLL_INTERVAL)
    try:
        while True:
            sensor_value = generate_sensor_data()
            logger.info("Current simulated soiling: %.2f", sensor_value)
            # Trigger cleaning mission if sensor value exceeds threshold.
            if sensor_value >= SOILING_THRESHOLD:
                logger.warning("Threshold exceeded (%.2f >= %.2f)", sensor_value, SOILING_THRESHOLD)
                try:
                    trigger_mission(SERVER_URL)
                    # Extended cooldown period after a trigger
                    time.sleep(20)
                except Exception:
                    logger.error("Aborting mission trigger after retries")
            # Wait for the next sensor read
            time.sleep(SENSOR_POLL_INTERVAL)
    except KeyboardInterrupt:
        logger.info("Simulation shutdown requested")
    finally:
        logger.info("Sensor simulation stopped")

if __name__ == "__main__":
    main()

