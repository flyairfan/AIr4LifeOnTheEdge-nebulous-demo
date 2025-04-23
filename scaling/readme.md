# Scaling Folder

This folder contains autoscaling configurations and logic for the AIr4LifeOnTheEdge platform. These files illustrate how edge/cloud resources are dynamically scaled based on sensor workload, as required for NebulOuS compliance.

- **autoscaling_policy.yaml** – Kubernetes Horizontal Pod Autoscaler for edge/cloud.
- **scale_logic.py** – (Optional) Simulated Python script for custom scaling logic.

Scaling is triggered by CPU utilization or high-frequency sensor event rates.
