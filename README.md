# AIr4LifeOnTheEdge – NebulOuS Technical Validation

Welcome to the technical validation repository for **AIr4LifeOnTheEdge**, an autonomous drone cleaning solution, field-tested on solar panels and greenhouse plastics in Almería, Spain.  
This repository demonstrates NebulOuS Open Call #2, Challenge #2 (IoT Application) compliance, highlighting deployability, modularity, predictive maintenance capabilities, and integration-readiness.

---

## Repository Structure

- `/demo/`  
  Field validation video (Almería), field photos, and Energies publication.
- `/edge/`  
  Sensor and drone control scripts, Dockerfile, requirements, container build/run instructions.
- `/cloud/`  
  Kubernetes deployment files, Open Application Model (OAM) descriptor, autoscaling configuration, and cloud analytics scripts.
- `/scaling/`  
  Autoscaling logic/config for edge/cloud scaling demonstration.
- `/predictive_maintenance/`  
  Copernicus data fetcher, predictive cleaning trigger logic, and workflow documentation.
- `/hardware/`  
  Raspberry Pi CM5 specs (Ubuntu 22.04, 4CPU/8GB RAM), LTE modem setup, and public-IP configuration.

---

## What’s Included (Validation Highlights)

- **Field Evidence:**  
  - Real-world demo video in /demo  
  - Peer-reviewed publication (see `/demo/` for DOI or PDF link)
- **Predictive & Reactive Maintenance:**  
  - `/predictive_maintenance/` demonstrates planned Copernicus/forecast integration to trigger preemptive cleaning and scaling, in addition to real-time sensor triggers.
- **Modular, Deployment-Ready Code:**  
  - Edge and cloud code is containerized (Docker/Kubernetes), with build/run instructions in each folder.
  - Edge node and hardware fully comply with NebulOuS IoT specs.
- **Scalable, SLA-Driven Architecture:**  
  - Example K8s and OAM configs for dynamic scaling, burst workloads, and orchestrator integration.
  - Autoscaling policies and simulation logic are provided.

---

## NebulOuS Integration Plan

- All components are modular/containerized, ready for declarative deployment using the NebulOuS Open Application Model (OAM).
- Edge nodes run Ubuntu 22.04 and are accessible via public IP/LTE, supporting NebulOuS automated, remote orchestration.
- Predictive maintenance pipeline leverages Copernicus API (currently simulated—real integration planned during project).
- The full pipeline is field-validated, and designed for dynamic, SLA-driven scaling and orchestration (further NebulOuS enhancements planned).

---

## Usage & Quickstart

- **Edge node:**  
  See `/edge/README.md` for local run and Docker build instructions.
- **Cloud deployment:**  
  Apply `/cloud/kube-deployment.yaml` (Kubernetes), use OAM descriptors for NebulOuS orchestration.
- **Predictive maintenance simulation:**  
  Run `/predictive_maintenance/predictive_trigger.py`.
- **Autoscaling:**  
  See `/scaling/` for policies/examples.

---

*This repository provides a NebulOuS-enabled, self-optimizing cleaning solution with field-tested workflows, advanced predictive (Copernicus-enabled), and SLA-driven orchestration across the edge-cloud continuum.*


