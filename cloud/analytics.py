# analytics.py
# Advanced cloud analytics for AIr4LifeOnTheEdge

import json
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

def analyze_node_data(node_id, data):
    """
    Analyze data from a single edge node.
    Calculates average soiling, triggers alert if anomaly detected.
    """
    avg_soiling = sum(data) / len(data)
    max_soiling = max(data)
    needs_attention = avg_soiling > 0.75 or max_soiling > 0.9

    result = {
        'node_id': node_id,
        'avg_soiling': avg_soiling,
        'max_soiling': max_soiling,
        'needs_attention': needs_attention,
        'timestamp': time.time()
    }
    # Simulate more advanced analytics (trend detection, etc.) here
    return result

def fetch_data_from_edge_nodes(num_nodes=5, batch_size=10):
    """
    Simulate fetching sensor data batches from multiple edge nodes.
    """
    return {
        f'node_{i}': [round(random.uniform(0.3, 1.0), 2) for _ in range(batch_size)]
        for i in range(1, num_nodes + 1)
    }

def main():
    print("Starting cloud analytics for AIr4LifeOnTheEdge.")

    while True:
        # Simulate real-time batch fetching
        edge_data_batches = fetch_data_from_edge_nodes(num_nodes=4, batch_size=12)

        results = []
        with ThreadPoolExecutor(max_workers=4) as executor:
            future_to_node = {
                executor.submit(analyze_node_data, node_id, data): node_id
                for node_id, data in edge_data_batches.items()
            }
            # Aggregate results as they complete (parallel step)
            for future in as_completed(future_to_node):
                result = future.result()
                results.append(result)
                print(json.dumps(result))

        # Optionally, aggregate or send to dashboard/cloud storage here
        print("Batch analytics summary:",
              json.dumps({'nodes_analyzed': len(results), 'timestamp': time.time()}, indent=2))

        time.sleep(20)  # Wait before next batch

if __name__ == "__main__":
    main()
