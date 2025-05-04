Demonstration Summary

For Video see DockerDroneDemo.MP4 (ca. 22 MB)

We have successfully demonstrated an end-to-end edge AI workflow for predictive maintenance of solar panels, integrating multiple components:
1. Sensor Simulation & Edge Node

    A sensor simulation script generates soiling data, mimicking real-world sensors on solar panels at the edge.
    When the simulated soiling exceeds a defined threshold, the edge node triggers a cleaning mission by sending an HTTP POST request to the backend.

2. Backend Command Server

    The backend (edge command server) receives mission triggers from the edge node.
    It orchestrates the mission by communicating with a drone (mocked in this demo) via UDP, sending commands such as command, takeoff, and land.
    The backend waits for acknowledgments from the drone and logs mission progress and results.

3. Mock Drone

    The mock drone simulates a real drone’s UDP interface, receiving commands from the backend and responding with "ok".
    This allows for safe, repeatable testing of the full mission workflow without real hardware.

4. Predictive Maintenance with Copernicus Data

    The system includes a Copernicus fetcher that retrieves dust storm risk forecasts from the CAMS API.
    This predictive data can be used to trigger preemptive cleaning missions before soiling becomes critical, enhancing maintenance efficiency.

Integration with NebulOuS

    The edge node and backend are designed to be orchestrated by the NebulOuS platform, which can deploy, monitor, and manage these components across distributed edge/cloud resources.
    NebulOuS can use the predictive maintenance insights (from Copernicus and local sensors) to automatically schedule and trigger cleaning missions as part of a larger, intelligent maintenance workflow.

Full Workflow

    Sensor data is gathered at the edge (simulated here).
    Predictive analytics (from Copernicus/CAMS) provide dust storm risk forecasts.
    Edge logic combines real-time soiling and predictive risk to decide when to trigger cleaning.
    Backend receives the trigger and manages the drone mission.
    Drone (mocked) executes the cleaning sequence.
    NebulOuS can orchestrate, monitor, and optimize this workflow across multiple sites and edge nodes.

Key Takeaways

    Seamless integration of real-time sensor data, predictive analytics, and autonomous actuation (drones).
    Edge-to-cloud orchestration ready for NebulOuS deployment.
    Modular, testable architecture with clear interfaces for sensors, predictive services, and actuators.

