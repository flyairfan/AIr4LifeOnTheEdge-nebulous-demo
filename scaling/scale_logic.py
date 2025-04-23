# scale_logic.py
# Example scaling algorithm for AIr4LifeOnTheEdge

import random

def get_current_event_rate():
    # Simulate incoming sensor event rate (events/min)
    return random.randint(30, 300)

def decide_scale(event_rate, threshold=100):
    # Return number of replicas needed based on event rate
    if event_rate < threshold:
        return 1
    elif event_rate < threshold * 2:
        return 2
    else:
        return 4

if __name__ == "__main__":
    current_rate = get_current_event_rate()
    replicas = decide_scale(current_rate)
    print(f"Sensor event rate: {current_rate} → Scale to {replicas} replicas")
