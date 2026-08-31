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

