# Pull Request Plan

## Week 1 - PR 1: PyTorch foundation
Branch: `feature/pytorch-model`

Suggested commits:
- `feat(model): add CIFAR-10 ResNet18 classifier`
- `feat(training): add configurable training and early stopping`
- `test(model): add output-shape unit test`

PR description should explain model choice, YAML configuration, JSON-line metrics, early stopping, and checkpoint output.

## Week 1 - PR 2: Docker workloads
Branch: `feature/docker-training-serving`

Suggested commits:
- `feat(docker): add multi-stage training image`
- `feat(serving): add FastAPI prediction service`
- `feat(docker): add non-root serving image and healthcheck`

Attach Docker build/run screenshots, `/health`, and `/predict` evidence.

## Week 2 - PR 3: Kubernetes training
Branch: `feature/k8s-training`

Suggested commits:
- `feat(k8s): add namespace configmap and persistent storage`
- `feat(k8s): add PyTorch training job`

Attach `kubectl get pods`, completed Job status, and training logs showing `checkpoint_saved`.

## Week 2 - PR 4: Kubernetes serving and validation
Branch: `feature/k8s-serving`

Suggested commits:
- `feat(k8s): add model serving deployment and service`
- `feat(k8s): add horizontal pod autoscaler`
- `docs(readme): add end-to-end validation evidence`

Attach serving pod status, deployment description, service/HPA output, port-forward, and prediction result.

## Final PR
Create `develop -> main` PR named: `release: complete PyTorch MLOps pipeline` and include the final validation screenshots plus links to the four feature PRs.
