# DevOps End-to-End Exam Project

This repository contains the implementation of a DevOps end-to-end exam project, which includes infrastructure provisioning, application deployment, and CI/CD pipeline setup.

## Project Structure

- **terraform/** - Infrastructure as Code (Terraform) for AWS EC2 provisioning
- **app/** - Flask application for AWS resource monitoring
- **helm/** - Helm charts for Kubernetes deployment
- **ci-cd/** - CI/CD pipeline configurations (Jenkins and Azure DevOps)

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

## Deployment

The application is deployed using Docker and Kubernetes. See the respective directories for detailed deployment instructions. 