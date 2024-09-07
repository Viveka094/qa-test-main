# Automated Integration Testing: Frontend and Backend services

This project demonstrates automated integration testing between frontend and backend services using Kubernetes, Docker, and Python scripts. Since my local environment lacked the necessary configurations, I utilized GitHub Codespaces for deployment and testing.

## Table of Contents
1. Prerequisites
2. Setup and Deployment
    - Clone the Repository
    - Build Docker Images
    - Push Docker Images
    - Deploy Services to Kubernetes
    - Verify Communication
3. Python Test Script
    - Installation
    - Test Execution
4. GitHub Codespaces Notes
5. Additional Commands

# Prerequisites
Ensure you have the following software installed on your system:

  * Docker
  * Minikube for local Kubernetes clusters
  * kubectl for managing Kubernetes
  * Python 3.x (for automated testing)

# Setup and Deployment
# 1. Clone the Repository
   Start by cloning the repository from GitHub:

   ```bash
   # Bash code
   git clone <repository-url>
   cd <repository-folder>
```
# 2. Build Docker Images
You need to build Docker images for both the backend and frontend services:
  * From the backend folder:
      ```bash
      # Bash code
     docker build -t vengatesh27/backend:v1 .
      ```
  * From the frontend folder:
      ```bash
      # Bash code
     docker build -t vengatesh27/frontend:v1 .
      ```
# 3. Push Docker Images
Push the Docker images to Docker Hub:
 ```bash
 # Bash code
 docker push vengatesh27/backend:v1
 docker push vengatesh27/frontend:v1
```
# 4. Deploy Services to Kubernetes
Deploy both services to Kubernetes using the provided YAML files:
  * From the Deployment folder, run:
    ```bash
    # Bash code
    kubectl apply -f backend-deployment.yaml
    kubectl apply -f frontend-deployment.yaml
    ```
Verify that the pods and services are running:
  ```bash
    # Bash code
    kubectl get pods
    kubectl get svc
  ```
# 5. Verify Communication
The frontend service should fetch the greeting message from the backend. Ensure that both services are working correctly by accessing the frontend:

Start Minikube:
```bash
# Bash code
minikube start --driver=docker
```
Once deployed, access the frontend URL in the browser, and you should see the message Hello from the Backend!.

<img width="358" alt="Screenshot 2024-09-06 011350 - Copy" src="https://github.com/user-attachments/assets/e04029e2-b49a-47b3-9203-5f8d542c65a3">

# Python Test Script
This project includes a Python test script to automate the verification process. The script ensures that the frontend communicates correctly with the backend.

# Installation
In GitHub Codespaces, install the required package:
```bash
  # Bash code
  pip install requests
```
Test Execution
Run the Python script to test the integration:
```bash
  # Bash code
  python test_integration.py
```
Expected output:
```bash
Status Code: 200
Response Text: <h1>Hello from the Backend!</h1>
Test passed: Frontend displays the correct message from the backend.
```
# What the Test Script Does
  * Sends an HTTP request to the frontend service.
  * Checks if the response contains the message "Hello from the Backend!".
  * Logs the results into a log file test_log.log for future reference.

# GitHub Codespaces Notes
Since my local environment was not configured, I used GitHub Codespaces for deployment and testing. You can follow these steps to set up services in a Codespace:

1. Install minikube and kubectl.
2. Use minikube to manage Kubernetes services.
3. Use Docker to build images directly within the Codespace.

# Additional Commands
To check Minikube status:
```bash
  # Bash code
  minikube status
```
To forward a port:
```bash
  # Bash code
  kubectl port-forward <pod-name> 8080:80
```
