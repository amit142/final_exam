# CI/CD Pipeline Configurations

This directory contains CI/CD pipeline configurations for Jenkins and Azure DevOps.

## Jenkins Pipeline

The `Jenkinsfile` defines a pipeline that:
- Runs linting and security scanning in parallel
- Builds a Docker image
- Pushes the image to Docker Hub

### Running the Jenkins Pipeline

1. Set up Jenkins with the necessary plugins:
   - Docker
   - Pipeline
   - Git

2. Configure Jenkins credentials for Docker Hub

3. Create a new pipeline job pointing to the repository

## Azure DevOps Pipeline

The `azure-pipelines.yml` defines a pipeline that:
- Runs linting and security scanning in parallel
- Builds a Docker image
- Pushes the image to Docker Hub

### Running the Azure DevOps Pipeline

1. Set up an Azure DevOps project

2. Configure service connections for:
   - GitHub
   - Docker Hub

3. Create a new pipeline using the YAML file 