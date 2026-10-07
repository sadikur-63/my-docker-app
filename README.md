# Multi-Container App & Render Deployment
A complete reference guide for managing a multi-container setup (Nginx Web Frontend, Node.js API, and PostgreSQL Database) using Docker Compose, as well as deploying live services to Render.
---
## 🚀 Live Deployment on Render

* **Web App URL:** `https://my-docker-app-o43s.onrender.com`
* **Deployment Workflow:** Connected to GitHub repository for automated CI/CD deployment on every `git push`.
---
## 🏗️ Architecture & Services (`compose.yaml`)

* **`web-frontend`**: Nginx web server running on lightweight Alpine Linux (`nginx:alpine`), mapping host port `8080` to container port `80`.
* **`api-service`**: Node.js runtime (`node:18-alpine`) executing an API background service.
* **`database`**: PostgreSQL database service for persistent data storage.
---
## 🐙 Docker Compose Commands
### 1. Start All Services
```bash
docker compose up -d
docker compose ps (Check Running Services)
docker compose down(Stop and Remove All Containers)

## 🛠️ Single Docker Commands

| Command | Action |
| :--- | :--- |
| `docker build -t <image_name> .` | Build an image from a local Dockerfile |
| `docker run -d <image_name>` | Run an image in the background |
| `docker ps` | List all running Docker containers |
| `docker logs <container_id>` | View logs of a specific container |
| `docker stop <container_id>` | Stop a running container |
| `docker rm <container_id>` | Delete a stopped container |
| `docker rmi <image_name>` | Delete a Docker image |

