AIr4LifeOnTheEdge Integration Overview

This document provides a detailed overview of how AIr4LifeOnTheEdge integrates various components to deliver an autonomous drone cleaning system that is both reactive and predictive. Our architecture is designed to seamlessly interface with the NebulOuS Meta-OS for dynamic orchestration and resource scaling.
1. System Architecture

The solution consists of multiple modules working together:

    Edge Node (Raspberry Pi CM5):

        Collects sensor data (soiling levels) via main.py.

        Triggers cleaning reactively if sensor values exceed a threshold.

        Requests forecast data to make proactive cleaning decisions.

        Reports telemetry to the cloud for further analytics.

    Cloud Analytics Module:

        Processes sensor data batches using analytics.py.

        Performs anomaly detection and triggers autoscaling actions when needed.

        Integrates predictive maintenance by incorporating Copernicus forecast data.

    Predictive Maintenance Module:

        copernicus_fetcher.py: Fetches dust storm risk data from the Copernicus Atmosphere Monitoring Service (CAMS).

        predictive_trigger.py: Determines if preemptive cleaning should be triggered based on forecasted risk.

    Autoscaling Module:

        Kubernetes Autoscaling: Managed using autoscaling.yaml (CPU utilization thresholds).

        Custom Scaling Logic: Provided by scale_logic.py, which adjusts resources based on sensor event rates.

    Deployment and Orchestration:

        All components are containerized (Docker) and orchestrated via Kubernetes.

        OAM descriptor (application.oam.yaml) integrates edge-cleaner and predictive-trigger components.

2. Data Flow & Integration

The interaction between components is illustrated in the flowchart below:

```mermaid
flowchart TD
    A["Edge Node: Sensor Data Collection (main.py)"]
    B["Evaluate Sensor Data (Soiling Value)"]
    C["Reactive Trigger: Cleaning (if soiling ≥ threshold)"]
    D["Proceed with Monitoring"]
    E["Predictive Module (/predictive_maintenance/)"]
    F["Fetch Forecast Data (copernicus_fetcher.py)"]
    G{"Dust Storm Risk High? (risk > threshold)"}
    H["Preemptive Trigger: Cleaning"]
    I["Report Status to Cloud"]
    J["Cloud Analytics Module (analytics.py)"]
    K["Aggregate Data & Detect Anomalies"]
    L["Autoscaling Logic (autoscaling.yaml + scale_logic.py)"]
    M["Deploy/Scale Resources via NebulOuS OAM & K8s"]
    
    A --> B
    B -- "Soiling High" --> C
    B -- "Not High" --> D
    A --> E
    E --> F
    F --> G
    G -- "Yes" --> H
    G -- "No" --> I
    C --> I
    H --> I
    I --> J
    J --> K
    K --> L
    L --> M

2.1 Edge-to-Cloud Data Flow:

    Edge Node Reads Sensor Data:

        main.py captures environmental soiling levels.

        If soiling exceeds a threshold, reactive cleaning is triggered.

    Predictive Maintenance:

        copernicus_fetcher.py fetches environmental forecast data.

        predictive_trigger.py evaluates dust risk; if high, preemptive cleaning is activated.

    Cloud Processing:

        analytics.py processes sensor data and detects anomalies.

        Autoscaling logic (autoscaling.yaml, scale_logic.py) decides whether to adjust resources.

    NebulOuS Orchestration:

        The NebulOuS Meta-OS ensures dynamic orchestration via OAM descriptors (application.oam.yaml).

3. Integration with NebulOuS Meta-OS
3.1 Compliance:

    Containerization & OAM: Components are fully containerized and orchestrated via Kubernetes.

    Dynamic Orchestration: NebulOuS manages deployment, scaling, and reconfiguration dynamically.

    Hardware Compliance: Edge node specs (Ubuntu 22.04, 4 CPUs, 8GB RAM, LTE modem) meet requirements.

3.2 Predictive Reconfiguration:

    Copernicus forecast risk data can dynamically adjust scaling decisions.

    Autoscaling ensures resources expand preemptively before environmental disruptions.

4. Future Enhancements

    Real API Integration for CAMS Data:

        Replace simulated Copernicus fetching with actual API calls and caching mechanisms.

    Advanced Monitoring & Visualization:

        Integrate Prometheus/Grafana dashboards for real-time system performance insights.

    Automated SLA-Driven Reconfigurations:

        Deepen integration with NebulOuS orchestration APIs for real-time SLA enforcement.

5. Conclusion

AIr4LifeOnTheEdge is a fully integrated system combining edge data collection, cloud analytics, predictive maintenance, and autoscaling. Its architecture aligns with NebulOuS standards, ensuring seamless deployment, dynamic resource management, and proactive operational decision-making.
