# simulation/simulate_sensor.py

import time
import random
import requests

def simulate_sensor_reading():
    """
    Simulates a sensor reading.
    In a real scenario, this could be a dust level or soiling index.
    Here, it returns a random integer between 0 and 100.
    """
    return random.randint(0, 100)

def main():
    # Define a threshold value for triggering the cleaning mission.
    threshold = 80
    # Adjust the endpoint URL as needed; assume the Flask server is running on localhost:5000.
    endpoint_url = "http://localhost:5000/start_mission"
    
    print("Starting sensor simulation...")
    while True:
        sensor_value = simulate_sensor_reading()
        print(f"Simulated sensor value: {sensor_value}")
        
        # If sensor reading exceeds the threshold, trigger the mission.
        if sensor_value > threshold:
            print("Threshold exceeded! Triggering cleaning mission...")
            try:
                response = requests.post(endpoint_url)
                print("Response from server:", response.json())
            except Exception as e:
                print("Failed to trigger mission:", e)
            # Wait longer after triggering to simulate mission duration.
            time.sleep(20)
        else:
            print("Sensor reading below threshold, no mission triggered.")
        
        # Wait a few seconds before running the next reading.
        time.sleep(5)

if __name__ == "__main__":
    ma
  in()
