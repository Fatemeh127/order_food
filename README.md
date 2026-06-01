# Order Food AI

An AI-powered food ordering and food analysis application built with FastAPI, JWT authentication, Docker, and Gradio.

This project combines backend API development, authentication systems, database management, and AI-based food analysis into a modern Python application.

---

# Features

* User authentication with JWT
* Food API endpoints
* AI-powered food analysis
* FastAPI backend architecture
* Database migrations with Alembic
* Dockerized development environment
* Interactive Gradio user interface
* Modular and scalable project structure

---

# Tech Stack

* Python
* FastAPI
* SQLAlchemy
* Alembic
* JWT Authentication
* Gradio
* Docker
* Docker Compose

---

# Project Structure

```text
order_food/
├── core/
│   ├── ai/
│   │   ├── food_analyzer.py
│   │   └── __init__.py
│   ├── alembic/
│   │   ├── env.py
│   │   ├── README
│   │   ├── script.py.mako
│   │   └── versions/
│   ├── auth/
│   │   ├── jwt_auth.py
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   └── __init__.py
│   ├── food/
│   │   ├── food_api.py
│   │   ├── routes.py
│   │   └── __init__.py
│   ├── user/
│   │   ├── models.py
│   │   ├── routes.py
│   │   ├── schemas.py
│   │   ├── user_gradio.py
│   │   └── __init__.py
│   ├── alembic.ini
│   └── main.py
├── docs/
├── docker-compose.yml
├── Dockerfile.dev
├── requirements.txt
├── LICENSE
└── README.md
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/Fatemeh127/order_food.git
cd order_food
```

---

## 2. Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

Linux / macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the application

```bash
uvicorn core.main:app --reload
```

Application runs on:

```text
http://localhost:8000
```

FastAPI Swagger documentation:

```text
http://localhost:8000/docs
```

---

# Run with Docker

```bash
docker compose up --build
```

---

# Authentication

The project uses JWT-based authentication for secure user access.

Authentication logic is located in:

```text
core/auth/jwt_auth.py
```

---

# AI Module

The AI functionality is implemented inside:

```text
core/ai/food_analyzer.py
```

This module can be extended for:

* Food recognition
* Nutritional analysis
* Recommendation systems
* AI-powered food insights

---

# Database Migration

Alembic is used for database migrations.

Run migrations with:

```bash
alembic upgrade head
```

---

# API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

---

# Learning Objectives

This project demonstrates:

* Backend API development
* AI integration in web applications
* JWT authentication
* Database architecture
* Docker containerization
* Modular FastAPI architecture
* Database migrations using Alembic

---

# Future Improvements

* Food recommendation engine
* AI meal planning
* Image-based food recognition
* Payment gateway integration
* Admin dashboard
* Cloud deployment
* CI/CD pipeline

---

# Author

**Fatemeh Abidizadegan**

GitHub: https://github.com/Fatemeh127
