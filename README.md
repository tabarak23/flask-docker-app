👤 Author
Khaja Tabarak uddin
💼 DevOps & mlops engineer https://linkedin.com/in/tabarak8106749169


# 🚀 Flask K8s App: CI/CD with GitHub Actions, Docker & Kubernetes

A **production-style Python Flask application** that is:

- 🐳 **Containerized using Docker**
- ☸️ **Deployed on Kubernetes**
- 🔁 **Fully automated with GitHub Actions CI/CD**
- 🧠 **Uses dynamic Docker image tags** based on commit SHA to ensure fresh deployments every push!

---

## 📖 Description

This project is a modern DevOps showcase where **every code change triggers a full CI/CD pipeline**. When you push code to the `main` branch:

1. ✅ Code is **linted, tested**, and **auto-formatted**
2. 🐳 A **Docker image is built with a dynamic tag** (`${{ github.sha }}`) — ensuring every build is unique
3. 📦 The image is **pushed to DockerHub**
4. 🛠 Kubernetes manifests (`k8s/dep.yaml`) are dynamically updated with the new image tag using `sed`
5. ☸️ The app is deployed to a **local `kind` cluster** inside GitHub Actions for validation
6. 🔄 Kubernetes rollout status is checked for successful deployment

> ✅ All this happens automatically via GitHub Actions with every push or pull request to `main`.

---


---

## 🔥 Key Features

- ✅ **Dynamic Docker Image Tags** (`github.sha`) on every commit
- 🔐 GitHub Secrets used for DockerHub authentication
- ☸️ `kubectl` + `kind` for in-pipeline Kubernetes deployments
- 🧪 Code tested using `pytest` and coverage reported
- 🎯 Strict code quality with `flake8` and `black`

---

## 🌐 Endpoints

| Method | Endpoint     | Description                 |
|--------|--------------|-----------------------------|
| GET    | `/`          | Root route with app message |
| GET    | `/healthz`   | Health check for probes     |

---

## 🛠️ Technologies Used

- **Python 3.13**
- **Flask**
- **Docker & DockerHub**
- **Kubernetes (Kind)**
- **GitHub Actions**
- **Pytest, Coverage, Flake8, Black**

---

## 🚀 Running Locally

### Build & Run with Docker

```bash
docker build -t flask-k8s-app .
docker run -p 5000:5000 flask-k8s-app


sed -i "s|TAG|latest|g" k8s/dep.yaml
kubectl apply -f k8s/
kubectl get svc nodeport

curl http://localhost:30800/



| Stage      | Description                                   |
| ---------- | --------------------------------------------- |
| ✅ Checkout | Clones the code from GitHub                   |
| 🧪 Testing | Runs `pytest` and coverage                    |
| 🧹 Linting | Runs `flake8` and `black`                     |
| 🐳 Docker  | Builds image with dynamic tag                 |
| ☸️ Deploy  | Updates K8s YAML and applies it via `kubectl` |


| Name                               | Purpose                   |
| ---------------------------------- | ------------------------- |
| `DOCKER_USERNAME`                  | Your DockerHub username   |
| `DOCKER_PASSWORD` / `DOCKER_TOKEN` | DockerHub token for login |

👤 Author
Khaja Tabarak uddin
💼 DevOps & mlops engineer https://linkedin.com/in/tabarak8106749169


