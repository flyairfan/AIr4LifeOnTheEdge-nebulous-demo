# Scaling Folder

This folder contains autoscaling configurations and example scaling logic for the AIr4LifeOnTheEdge platform.

## Contents

- **autoscaling_policy.yaml** – Kubernetes Horizontal Pod Autoscaler configuration for edge/cloud deployments.
- **scale_logic.py** – Example Python script for custom scaling logic based on workload or forecast signals.

## Predictive Maintenance and Scaling

In addition to scaling based on CPU utilization or sensor event rates, the system is designed to use predictive maintenance signals from Copernicus and other environmental forecasts (see `/predictive_maintenance/`).  
When a high-risk dust or sandstorm event is predicted, NebulOuS can preemptively scale up edge or cloud resources to ensure timely cleaning and data processing, then scale down when the risk subsides.

## Usage

- Apply `autoscaling_policy.yaml` in your Kubernetes cluster to enable automatic scaling of the edge-cleaner deployment.
- Use or adapt `scale_logic.py` to simulate or implement custom scaling triggers, including those based on Copernicus forecast data.

## References

- For details on how predictive triggers are generated, see `/predictive_maintenance/`.
- For deployment and orchestration, see `/cloud/`.

---
