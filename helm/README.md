# Helm Chart for AWS Monitoring Application

This directory contains a Helm chart for deploying the AWS monitoring Flask application to Kubernetes.

## Chart Structure

- `Chart.yaml` - Chart metadata
- `values.yaml` - Default configuration values
- `templates/` - Kubernetes manifest templates

## Deployment

1. Install the chart:
   ```
   helm install aws-monitor ./aws-monitor
   ```

2. Upgrade the deployment:
   ```
   helm upgrade aws-monitor ./aws-monitor
   ```

3. Rollback if needed:
   ```
   helm rollback aws-monitor <revision>
   ```

## Configuration

The following values can be configured in `values.yaml`:

- Docker image and tag
- Replica count
- Environment variables for AWS credentials
- Resource requests and limits
- Service type (ClusterIP or LoadBalancer)

## Accessing the Application

After deployment, the application can be accessed at:
```
http://<service-ip>:5001
``` 