\# Assignment Submission Summary



\## Student Details

\- Name: Ganesan SP

\- Roll No: DA25M564



\## Repository

https://github.com/da25m564/mlops-pytorch-pipeline



\## Implementation Summary



This repository implements an end-to-end PyTorch MLOps workflow covering:



\- CIFAR-10 image classification using PyTorch

\- ResNet-18 based model architecture

\- YAML-based training configuration

\- Structured JSON metric logging

\- Early stopping and model checkpointing

\- Dockerized model training

\- Dockerized FastAPI model serving

\- GET /health endpoint

\- POST /predict endpoint

\- Kubernetes namespace and ConfigMap

\- PersistentVolumeClaim for model storage

\- Kubernetes training Job

\- Two-replica serving Deployment

\- Liveness and readiness probes

\- Resource requests and limits

\- ClusterIP Service

\- Horizontal Pod Autoscaler

\- GitHub Actions CI

\- Unit testing with pytest



\## Validation Summary



The implementation was validated through:



\- Successful pytest execution

\- Model checkpoint generation

\- Docker /health validation

\- Docker /predict validation

\- Kubernetes training completion

\- Persistent checkpoint storage

\- Two serving pods running successfully

\- ClusterIP Service configuration

\- HPA configuration

\- Kubernetes /health validation

\- Kubernetes /predict validation



\## Final Validation Results



\- Best validation loss: 0.3973

\- Final validation accuracy: 0.8709

\- Checkpoint: /app/checkpoints/classifier\_v1.pt



\## Reflection



The detailed 300-500 word reflection is available in:



`REFLECTION.md`

## Final Submission Checklist

The following items are included in the repository for final submission:

- Public GitHub repository
- PyTorch CIFAR-10 training pipeline
- ResNet-18 model implementation
- YAML-based training configuration
- JSON metric logging
- Early stopping
- Model checkpoint generation
- Docker training image
- Docker serving image
- FastAPI `/health` endpoint
- FastAPI `/predict` endpoint
- Kubernetes namespace
- Kubernetes ConfigMap
- PersistentVolumeClaim
- Kubernetes training Job
- Two-replica serving Deployment
- Liveness and readiness probes
- CPU and memory requests/limits
- ClusterIP Service
- Horizontal Pod Autoscaler
- Unit testing with pytest
- GitHub Actions CI
- README with architecture and setup instructions
- 300-500 word reflection
- End-to-end validation evidence

## Submission Links

Repository:
https://github.com/da25m564/mlops-pytorch-pipeline

Final Pull Request:
To be added after the final develop-to-main merge.

