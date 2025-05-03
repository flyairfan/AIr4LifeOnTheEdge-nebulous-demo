# scaling/scale_logic.py
import random
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def get_scaling_metric():
    """Fetch composite scaling metric with error handling"""
    try:
        # Simulated metric fetch - replace with actual implementation
        metric = random.randint(50, 200)
        logging.info(f"Retrieved scaling metric: {metric}")
        return metric
    except Exception as e:
        logging.error(f"Metric fetch failed: {str(e)}")
        return 0  # Safe default

def decide_scale(scaling_metric, threshold=130):
    """Determine replica count based on metric"""
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
