```mermaid
flowchart TD
    %% Edge Node Block
    subgraph "Edge Node (Raspberry Pi CM5)"
      A["Collect Sensor Data<br>(main.py)"]
      B["Reactive Cleaning Trigger<br>(if soiling threshold exceeded)"]
      C["Request Forecast Data<br>(for proactive cleaning)"]
      D["Report Telemetry to Cloud"]
    end

    %% Predictive Maintenance Block
    subgraph "Predictive Maintenance Module"
      E["Copernicus Data Fetcher<br>(copernicus_fetcher.py)"]
      F["Predictive Trigger<br>(predictive_trigger.py)"]
    end

    %% Cloud Analytics Block (AWS Integration)
    subgraph "Cloud Analytics & Scaling (AWS)"
      G["Process Sensor Data<br>(analytics.py)"]
      H["Autoscaling Logic<br>(scale_logic.py)"]
      I["AWS Cloud Infrastructure<br>(EC2, AutoScaling)"]
    end

    %% Orchestration Layer
    subgraph "NebulOuS Orchestration"
      J["OAM Descriptor<br>(application.oam.yaml)"]
    end

    %% Data Flow
    A --> B
    A --> C
    A --> D
    C --> F
    E --> F
    F --> B
    D --> G
    G --> H
    H --> I
    J --> G
    J --> H
