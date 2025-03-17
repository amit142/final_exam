# Kubernetes Deployment

This directory contains Kubernetes manifests for deploying the AWS Monitor application.

## Files

- `deployment.yaml`: Defines the Deployment for the application
- `service.yaml`: Defines the Service to expose the application
- `configmap.yaml`: Contains configuration data for the application

## Deployment Instructions

1. Ensure you have `kubectl` installed and configured to connect to your Kubernetes cluster.

2. Apply the ConfigMap:
   ```bash
   kubectl apply -f configmap.yaml
   ```

3. Apply the Deployment:
   ```bash
   kubectl apply -f deployment.yaml
   ```

4. Apply the Service:
   ```bash
   kubectl apply -f service.yaml
   ```

5. Check the status of the deployment:
   ```bash
   kubectl get deployments
   kubectl get pods
   ```

6. Check the status of the service and get the external IP:
   ```bash
   kubectl get services
   ```

7. Access the application using the external IP provided by the LoadBalancer service.

## Cleanup

To remove the deployment:

```bash
kubectl delete -f service.yaml
kubectl delete -f deployment.yaml
kubectl delete -f configmap.yaml
``` 