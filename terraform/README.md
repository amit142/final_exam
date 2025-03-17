# Terraform Infrastructure

This directory contains Terraform configurations to provision an AWS EC2 instance with Docker and Docker Compose installed.

## Components

- EC2 instance named "builder"
- Security group allowing SSH (port 22) and HTTP (port 5001, 8080) access
- SSH key pair for secure access

## Usage

1. Initialize Terraform:
   ```
   terraform init
   ```

2. Apply the configuration:
   ```
   terraform apply
   ```

3. Access the EC2 instance:
   ```
   ssh -i builder_key.pem ec2-user@<instance-ip>
   ```

## Outputs

- EC2 instance public IP
- SSH key location
- Security group ID 