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
