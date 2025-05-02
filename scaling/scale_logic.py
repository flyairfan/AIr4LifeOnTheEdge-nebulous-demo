# scale_logic.py
# Revised scaling algorithm for AIr4LifeOnTheEdge using a composite scaling metric.

import random

def get_scaling_metric():
    """
    Simulate fetching a composite scaling metric calculated from Cloud Analytics.
    For example, this metric might be formed by aggregating average soiling values,
    forecast risk, and other parameters.
    
    In this simulation, we return a random integer between 50 and 200.
    """
    return random.randint(50, 200)

def decide_scale(scaling_metric, threshold=130):
    """
    Determine the number of replicas based on the composite scaling metric.
    
    Args:
      scaling_metric (int or float): A composite metric that influences scaling decisions.
      threshold (number): The base threshold for scaling decisions.
    
    Returns:
      int: The number of replicas recommended.
      
    Decision logic example:
      - If scaling_metric is less than threshold: use 1 replica.
      - If scaling_metric is between threshold and threshold * 1.5: use 2 replicas.
      - If scaling_metric exceeds threshold * 1.5: use 4 replicas.
    """
    if scaling_metric < threshold:
        return 1
    elif scaling_metric < threshold * 1.5:
        return 2
    else:
        return 4

if __name__ == "__main__":
    current_metric = get_scaling_metric()
    replicas = decide_scale(current_metric)
    print(f"Composite scaling metric: {current_metric} -> Scale to {replicas} replicas")
