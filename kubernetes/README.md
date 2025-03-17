# AWS Monitor Kubernetes Deployment

This directory contains the Kubernetes manifests for deploying the AWS Monitor application.

## Prerequisites

- Kubernetes cluster (e.g., Minikube, EKS, GKE)
- Docker image `amit142/aws-monitor:latest` available in Docker Hub
- AWS credentials with appropriate permissions

## Installation Steps

1. Create the AWS credentials secret:
   ```bash
   kubectl create secret generic aws-credentials \
     --from-literal=aws_access_key_id=your-access-key-id \
     --from-literal=aws_secret_access_key=your-secret-access-key
   ```

2. Apply the Kubernetes manifests:
   ```bash
   kubectl apply -f configmap.yaml
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

3. Verify the deployment:
   ```bash
   kubectl get pods
   kubectl get service aws-monitor-service
   ```

4. Access the application:
   - If using Minikube: `minikube service aws-monitor-service`
   - If using cloud provider: Use the external IP from `kubectl get service aws-monitor-service`

## Configuration

The application can be configured using the following environment variables:
- `PORT`: Application port (default: 5001)
- `AWS_ACCESS_KEY_ID`: AWS access key (from secret)
- `AWS_SECRET_ACCESS_KEY`: AWS secret key (from secret)
- `AWS_DEFAULT_REGION`: AWS region (default: us-east-1)

## Health Checks

The application provides two health check endpoints:
- `/health`: Liveness probe endpoint
- `/readiness`: Readiness probe endpoint

## Troubleshooting

1. Check pod logs:
   ```bash
   kubectl logs -l app=aws-monitor
   ```

2. Check pod status:
   ```bash
   kubectl describe pods -l app=aws-monitor
   ```

3. Check service status:
   ```bash
   kubectl describe service aws-monitor-service
   ```

## Files

- `deployment.yaml`: Defines the Deployment for the application
- `service.yaml`: Defines the Service to expose the application
- `configmap.yaml`: Contains configuration data for the application

## Cleanup

To remove the deployment:

```bash
kubectl delete -f service.yaml
kubectl delete -f deployment.yaml
kubectl delete -f configmap.yaml
``` 
-at the second screenshot i used minikube  