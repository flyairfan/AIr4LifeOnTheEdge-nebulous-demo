flowchart TD
    A[Edge Node: Sensor Data Collection<br>(main.py)]
    B[Evaluate Sensor Data<br>(Soiling Value)]
    C[Reactive Trigger: Cleaning<br>(if soiling ≥ threshold)]
    D[Proceed with Monitoring]
    E[Predictive Module<br>/predictive_maintenance/]
    F[Fetch Forecast Data<br>(copernicus_fetcher.py)]
    G{Dust Storm Risk High?<br>(risk > threshold)}
    H[Preemptive Trigger: Cleaning]
    I[Report Status to Cloud]
    J[Cloud Analytics Module<br>(analytics.py)]
    K[Aggregate Data & Detect Anomalies]
    L[Autoscaling Logic<br>(autoscaling.yaml + scale_logic.py)]
    M[Deploy/Scale Resources<br>via NebulOuS OAM & K8s]
    
    A --> B
    B -- Soiling High --> C
    B -- Not High --> D
    A --> E
    E --> F
    F --> G
    G -- Yes --> H
    G -- No --> I
    C --> I
    H --> I
    I --> J
    J --> K
    K --> L
    L --> M
