## Submission Information

**Student Name:** Ganesan SP  
**Roll No:** DA25M564  

**GitHub Repository:**  
https://github.com/da25m564/mlops-pytorch-pipeline

**Final Implementation Pull Request:**  
https://github.com/da25m564/mlops-pytorch-pipeline/pull/3

**Project:**  
Deploying PyTorch ML Workloads with Docker & Kubernetes

### Final Validation

The complete MLOps pipeline was successfully validated with:

- PyTorch CIFAR-10 training using ResNet-18
- YAML-based training configuration
- Model checkpoint generation and persistent storage
- Dockerized training and FastAPI model serving
- Successful `/health` and `/predict` endpoint validation
- Kubernetes training Job completion
- Two model-serving replicas running successfully
- Liveness and readiness probes
- ClusterIP Service
- Horizontal Pod Autoscaler (HPA)
- Unit testing with pytest
- GitHub Actions CI
- End-to-end Kubernetes serving validation

Detailed project reflection is available in [`REFLECTION.md`](REFLECTION.md).



# MLOps PyTorch Pipeline

End-to-end CIFAR-10 image classification pipeline covering Git workflow, PyTorch training, Docker containerization, Kubernetes training Jobs, and scalable FastAPI model serving.

## Architecture

```text
GitHub/PRs -> CI Tests -> Docker Training Image -> Kubernetes Job
                                         |          |
                                         |          v
                                         |       Shared PVC
                                         |          |
                                         v          v
                                  Docker Serve -> Deployment (2 replicas)
                                                    |
                                                    v
                                             ClusterIP Service
                                                    |
                                                    v
                                              POST /predict
```

## Repository structure

- `src/`: model, dataset, training, serving code
- `configs/`: training configuration
- `docker/`: training and serving Dockerfiles
- `k8s/`: Kubernetes manifests
- `requirements/`: pinned dependencies
- `tests/`: PyTorch model tests
- `.github/workflows/`: CI pipeline

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements/train.txt
pip install -r requirements/serve.txt
pytest -q
```

For local non-container training, temporarily change `data.data_dir` and `output.checkpoint_dir` in `configs/training_config.yaml` to `./data` and `./checkpoints`.

## Docker

```bash
docker build -f docker/Dockerfile.train -t mlops-train:v1 .
docker run --rm -v "$(pwd)/data:/app/data" -v "$(pwd)/checkpoints:/app/checkpoints" mlops-train:v1

docker build -f docker/Dockerfile.serve -t mlops-serve:v1 .
docker run --rm -p 8080:8080 -v "$(pwd)/checkpoints:/app/checkpoints:ro" mlops-serve:v1
curl http://localhost:8080/health
curl -X POST http://localhost:8080/predict -F "image=@test_image.png"
```

PowerShell volume syntax can use `${PWD}` instead of `$(pwd)`.

## Kubernetes (Minikube example)

Build images directly into Minikube's Docker daemon:

```bash
minikube start --cpus=4 --memory=8192
eval $(minikube docker-env)
docker build -f docker/Dockerfile.train -t mlops-train:v1 .
docker build -f docker/Dockerfile.serve -t mlops-serve:v1 .
```

Apply resources in order:

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/pvc.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/training-job.yaml
kubectl get jobs,pods -n ml-training
kubectl logs job/pytorch-training -n ml-training

kubectl apply -f k8s/serving-deployment.yaml
kubectl apply -f k8s/serving-service.yaml
kubectl apply -f k8s/hpa.yaml
kubectl get pods,svc,hpa -n ml-training
kubectl describe deployment model-serving -n ml-training
kubectl port-forward svc/model-serving 8080:80 -n ml-training
```

In another terminal:

```bash
curl http://localhost:8080/health
curl -X POST http://localhost:8080/predict -F "image=@test_image.png"
```

> HPA CPU metrics require Metrics Server. On Minikube: `minikube addons enable metrics-server`.

## Git workflow

Use `develop` as the integration branch. Create feature branches from `develop`, submit PRs into `develop`, then create a final PR from `develop` to `main`. Use Conventional Commits, e.g. `feat(training): add configurable PyTorch training pipeline`.

## Evidence to capture

Include screenshots or terminal output for successful Docker builds/runs, training checkpoint creation, `/health`, `/predict`, Kubernetes Job completion/logs, serving pods, Deployment description, Service/HPA status, and port-forward prediction.

## Validation Results

### Unit Testing
- ResNet18 output-shape test passed successfully.

### Docker
- Training image: `mlops-train:v1`
- Serving image: `mlops-serve:v1`
- `/health` returned `model_loaded=true`
- `/predict` returned CIFAR-10 class probabilities.

### Kubernetes Training
- Training Job completed successfully.
- Checkpoint saved to `/app/checkpoints/classifier_v1.pt`
- Best validation loss: `0.3973`
- Final validation accuracy: `0.8709`

### Kubernetes Serving
- Two model-serving replicas running.
- ClusterIP Service configured on port 80.
- Liveness and readiness probes enabled.
- HPA configured.
- `/health` and `/predict` validated through port forwarding.
