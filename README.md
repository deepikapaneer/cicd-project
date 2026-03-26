# CI/CD Pipeline with GitHub Actions

A Flask web application with an automated CI/CD pipeline using GitHub Actions and Docker.

## Project Overview

This project demonstrates a real-world CI/CD pipeline that automatically tests and builds
a Dockerized Flask application on every code push to the main branch.

## Architecture
```
Code Push → GitHub Actions Triggered
                ↓
          Run pytest tests
                ↓
         Tests Pass? ✅
                ↓
       Build Docker Image
                ↓
         Pipeline Green ✅
```

## Tech Stack

- **Python 3.11** — application runtime
- **Flask** — web framework
- **pytest** — automated testing
- **Docker** — containerization
- **GitHub Actions** — CI/CD pipeline

## API Endpoints

| Endpoint | Method | Response |
|---|---|---|
| `/` | GET | `{"message": "Hello from CI/CD!"}` |
| `/users` | GET | `{"message": "CI/CD Project - users page"}` |

## How to Run Locally

**Clone the repo:**
```bash
git clone https://github.com/deepikapaneer/cicd-project.git
cd cicd-project
```

**Install dependencies:**
```bash
pip install flask pytest
```

**Run the app:**
```bash
python app.py
```
Visit `http://localhost:5000`

**Run tests:**
```bash
pytest test_app.py -v
```

**Run with Docker:**
```bash
docker build -t cicd-app .
docker run -p 5000:5000 cicd-app
```

## CI/CD Pipeline

The pipeline has 2 jobs that run automatically on every push:

| Job | What it does |
|---|---|
| `test` | Sets up Python, installs dependencies, runs pytest |
| `build` | Builds Docker image (only runs if tests pass) |

If any test fails the pipeline stops immediately and the build job never runs —
preventing broken code from being packaged or deployed.

## What I Learned

- How to build a CI/CD pipeline from scratch with GitHub Actions
- How automated testing protects production from bad code
- How to containerize a Python app with Docker
- How pipelines trigger automatically on every code push

## Project Status

![CI Pipeline](https://github.com/deepikapaneer/cicd-project/actions/workflows/ci.yml/badge.svg)
