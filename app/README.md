# Flask AWS Monitoring Application

This directory contains a Flask application that monitors AWS resources such as EC2 instances, VPCs, Load Balancers, and AMIs.

## Application Structure

- `app.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `Dockerfile` - Multi-stage Docker build configuration

## Running Locally

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set AWS credentials as environment variables:
   ```
   export AWS_ACCESS_KEY_ID=your-access-key
   export AWS_SECRET_ACCESS_KEY=your-secret-key
   export AWS_REGION=us-east-1
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Access the application at http://localhost:5001

## Docker Deployment

1. Build the Docker image:
   ```
   docker build -t aws-monitor:latest .
   ```

2. Run the container:
   ```
   docker run -p 5001:5001 -e AWS_ACCESS_KEY_ID=your-access-key -e AWS_SECRET_ACCESS_KEY=your-secret-key -e AWS_REGION=us-east-1 aws-monitor:latest
   ```

3. Access the application at http://localhost:5001 