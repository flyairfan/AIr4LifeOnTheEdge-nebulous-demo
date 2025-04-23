# AIr4LifeOnTheEdge – NebulOuS Technical Validation

Welcome to the technical validation repository for **AIr4LifeOnTheEdge** a cleaning solution, field-tested on solar panels and greenhouse plastics in Almería, Spain. This repository provides evidence for NebulOuS Open Call #2, Challenge #2 (IoT Application), demonstrating the solution’s deployability, modularity, and integration-readiness.

## Repository Structure

- `/demo/`  
  Field validation video (Almería), field photos, and Energies publication.  
- `/edge/`  
  Sensor and drone control scripts, Dockerfile, docker-compose example.  
- `/cloud/`  
  Example Kubernetes deployment and cloud analytics code.  
- `/scaling/`  
  Autoscaling logic/config for edge/cloud scaling demonstration.  
- `/hardware/`  
  Specs/photo of Raspberry Pi CM5 (Ubuntu 22.04, 4CPU/8GB RAM, LTE modem); public-IP setup.  

## What’s Included (Validation Highlights)
- **Field Evidence:**  
  - Real-world demo video: `/demo/almeria_cleaning_video.mp4`  
  - Peer-reviewed publication (see `/demo/` for PDF or DOI)
- **Modular Codebase:**  
  - [Python/Node.js] edge and drone code, containerized (Docker/Kubernetes)
- **Deployment-Ready:**  
  - Docker Compose & K8s YAMLs for fast orchestration
  - Edge node setup fully detailed (hardware meets NebulOuS specs)
- **Scalable Architecture:**  
  - Example autoscaling configs for burst workloads and sandstorm simulation

## NebulOuS Integration Plan

- All core functions are modular/containerized and ready for declarative deployment using the NebulOuS Open Application Model (OAM).
- Edge nodes run Ubuntu 22.04 and are accessible via public IP/LTE, supporting NebulOuS remote orchestration.
- Full pipeline tested in the field, with further NebulOuS enhancements planned for dynamic SLA-driven scaling and orchestration.

## Usage
See folder READMEs for build/run instructions.

---

