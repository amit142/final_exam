# DevOps End-to-End Exam Project

This repository contains the implementation of a DevOps end-to-end exam project, which includes infrastructure provisioning, application deployment, and CI/CD pipeline setup.

## Project Structure

- **terraform/** - Infrastructure as Code (Terraform) for AWS EC2 provisioning
- **app/** - Flask application for AWS resource monitoring
- **helm/** - Helm charts for Kubernetes deployment
- **ci-cd/** - CI/CD pipeline configurations (Jenkins and Azure DevOps)
- **kubernetes/** - Kubernetes manifests for direct deployment

## Implementation Details

Each directory contains its own README.md with specific implementation details and instructions.

## Git Workflow

This project follows a structured Git Flow:
- Work is done in feature branches
- Feature branches are merged into dev
- Once validated, dev is merged into main
- No direct pushes to main are allowed

## AWS Credentials

The application uses AWS credentials to access AWS resources. These credentials are provided as environment variables.

## Deployment Options

### Docker
The application can be deployed using Docker:
```bash
docker build -t amit142/aws-monitor:latest .
docker run -p 5001:5001 amit142/aws-monitor:latest
```

### Kubernetes
For Kubernetes deployment, use the manifests in the `kubernetes/` directory:
```bash
kubectl apply -k kubernetes/
```
See the [Kubernetes README](kubernetes/README.md) for detailed instructions.

### Helm
For Helm-based deployment, use the charts in the `helm/` directory.

## CI/CD
The project includes CI/CD configurations for both Jenkins and Azure DevOps in the `ci-cd/` directory. 