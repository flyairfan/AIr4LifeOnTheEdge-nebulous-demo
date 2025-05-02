# System Diagrams

This folder contains all the key diagrams that describe the architecture and behavior of the AIr4LifeOnTheEdge system. Each diagram offers a unique perspective into the system:

---

## 1. Components Diagram
- **Description:**  
  Illustrates the static structure of the system by showing the various modules (e.g., Edge Node, Predictive Maintenance Service, Cloud Analytics, Autoscaling Logic) and how they interconnect.
- **Key Elements:**  
  - Software modules (e.g., `main.py`, `predictive_trigger.py`, etc.)  
  - The relationships between components
- **Filename:** `components.png`

---

## 2. Sequence Diagram
- **Description:**  
  Depicts the chronological interaction between components, outlining the communication flow. This includes processing steps from sensor reading, invoking predictive maintenance, reporting telemetry, and autoscaling.
- **Key Elements:**  
  - Message sequences between components
  - Timing of interactions and responses
- **Filename:** `sequence.png`

---

## 3. Activity Diagram
- **Description:**  
  Represents the operational process flow and control logic within the edge node. It shows how the process moves from reading sensor data, making reactive or predictive decisions, reporting telemetry, and then looping back.
- **Key Elements:**  
  - Workflow steps (e.g., reading sensors, evaluating soiling levels, triggering cleaning, reporting telemetry)
  - Decision points and loopback for continuous monitoring
- **Filename:** `activities.png`

---

## 4. Data Flow Diagram (DFD)
- **Description:**  
  Focuses on the movement and transformation of data across the system. It details where data originates (from the sensor), how it is processed in the edge node, enriched with forecast risk, reported to Cloud Analytics, and finally influences autoscaling decisions.
- **Key Elements:**  
  - Data sources and sinks (e.g., Soiling Sensor, Edge Node, Forecast Service)
  - The flow and transformation of data through the system
- **Filename:** `dataflow.png`

---

## 5. State Diagram
- **Description:**  
  Models the internal states of the Edge Node and details the transitions based on events (e.g., timer tick, data acquired, reporting complete). Each state shows additional internal actions (entry, do, and exit actions).
- **Key Elements:**  
  - Internal states (e.g., Idle, ReadingSensor, Evaluating)
  - Transition triggers and associated actions within each state
- **Filename:** `statediagram.png`

---

Each diagram plays an important part in visualizing different aspects of the system—from the high-level architecture and component relationships (Components Diagram) to the detailed interactions (Sequence Diagram), process flows (Activity Diagram), data transformations (Data Flow Diagram), and the internal state behavior (State Diagram).
