# AIr4LifeOnTheEdge - Edge Components

## Overview
Welcome to the edge module of AIr4LifeOnTheEdge—our solution for persistent edge-cloud orchestration in automated infrastructure maintenance. This folder contains all the necessary components to run the edge services, including sensor data acquisition, drone control, and preliminary orchestration. The components are containerized using Docker and can also be deployed on Kubernetes.

## Folder Contents
- Dockerfile: Defines the Docker image for the edge service.
- docker-compose.yml: Orchestrates the containerized services (e.g., the Flask API server, sensor simulator, etc.) for local development and testing.
- config.yaml: Contains runtime configuration settings (like the MQTT broker URL, server details, drone parameters, and sensor thresholds).
- kube-deployment.yaml: A sample Kubernetes deployment manifest to run the edge service on a Kubernetes cluster.
- main.py: The primary entry point for the edge application.
- requirements.txt: Lists all required Python packages (e.g., Flask, requests, paho-mqtt).

## Getting Started

### Prerequisites
- Docker & Docker Compose: Ensure you have Docker and Docker Compose installed.
- Kubernetes (Optional): For deploying via Kubernetes (e.g., using Minikube), ensure you have a local test cluster ready.

### Running Locally with Docker Compose
1. Build and Start the Containers  
   Open a terminal, navigate to this edge folder, and run:
   
       docker-compose up --build
   
   This command builds the Docker image as per the Dockerfile, installs the dependencies from requirements.txt, and starts the containers described in docker-compose.yml.

2. Verify Operation  
   - The service should start on the port specified in config.yaml (default is port 5000).  
   - **Test the API Endpoint:**  
     Use the following curl command to trigger the drone cleaning mission:
     
         curl -X POST http://localhost:5000/start_mission
     
     This command confirms that the API endpoint is active and processing your request.
   - Check Docker logs to verify that the configuration and runtime components (such as sensor data ingestion and drone control) are loading properly.

## Configuration Details (config.yaml)
Below is an example configuration. Adjust the settings as necessary for your test or production environment:

mqtt:
  broker: "mqtt://broker.hivemq.com:1883"
  username: ""         # Fill in if authentication is needed
  password: ""         # Fill in if authentication is needed

server:
  host: "0.0.0.0"
  port: 5000

drone:
  ip: "192.168.10.1"   # Set your drone's IP address here
  port: 8889
  local_port: 9000

sensor:
  threshold: 80        # Sensor threshold to trigger cleaning actions

## Kubernetes Deployment
The kube-deployment.yaml file is a sample manifest for deploying the edge service on a Kubernetes cluster.

To Deploy on Kubernetes:
1. Ensure Kubernetes is Running (e.g., start Minikube or your preferred local cluster).
2. Apply the Deployment:
   
       kubectl apply -f kube-deployment.yaml
   
3. Verify Deployment:
   
       kubectl get pods
       kubectl get svc

## AWS Integration (Future Enhancement)
Although the focus here is on edge functionality, the overall proposal calls for AWS integration for persistent edge-cloud orchestration. A minimal AWS deployment artifact (e.g., a basic CloudFormation template) is provided in the aws-deployment folder at the repository root. This placeholder demonstrates the envisioned integration with cloud services for scalable analytics and orchestration.

## Dependencies
The required Python packages are listed in requirements.txt:

paho-mqtt
requests
Flask==2.2.5

These dependencies are installed automatically during the Docker build process.

## Future Work
- Enhanced AWS Integration: Develop a cloud analytics engine using AWS services (such as AWS IoT Core and auto-scaling groups) to integrate with the edge components.
- Expanded Testing: Implement unit and integration tests to ensure system reliability.
- Improved Orchestration: Incorporate more sophisticated orchestration logic based on dynamic sensor data and operational triggers.
- Modular Integration with NebulOuS: Prepare your containerized microservices (with clear APIs and OAM descriptors) for future integration with NebulOuS Meta-OS.

## Additional Notes
- This module is a key part of the overall AIr4LifeOnTheEdge solution and demonstrates our commitment to edge-cloud integration.
- For more details on the overall architecture and AWS artifacts, please refer to the top-level README and the aws-deployment folder.
- For any questions or further clarification, consult the project documentation or contact the development team.
