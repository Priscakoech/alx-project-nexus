# ALX Project Nexus 🚀

## Overview
This repository documents my major learnings from the **ProDev Backend Engineering Program** at ALX.  
It also showcases my final project, an **Online Poll System**, built using Django and Docker.

---

## Program Learnings

### 🔑 Key Technologies
- **Python** – core programming language for backend logic.
- **Django** – rapid backend development with ORM and built-in features.
- **REST APIs** – building and consuming HTTP APIs.
- **GraphQL** – flexible query language for APIs.
- **Docker** – containerization and environment consistency.
- **CI/CD** – automating testing and deployment pipelines.

### 📚 Important Backend Concepts
- **Database Design** – modeling entities like users, polls, and votes.
- **Asynchronous Programming** – handling background tasks and scalability.
- **Caching Strategies** – using Redis for response and query caching.
- **Signals** – automatic cache invalidation and event handling.

### ⚡ Challenges & Solutions
- **Challenge**: Setting up Docker for multi-service environments (Django + Postgres + Redis).  
  **Solution**: Used `docker-compose.yml` with proper volume and network configuration.  

- **Challenge**: Optimizing database queries for polls and votes.  
  **Solution**: Applied Django ORM `select_related` and caching with Redis.  

- **Challenge**: Managing cache invalidation when polls or votes change.  
  **Solution**: Implemented Django signals (`post_save`, `post_delete`) to clear Redis keys.  

### ✅ Best Practices & Takeaways
- Always separate **settings** for local, staging, and production.  
- Use **environment variables** for secrets instead of hardcoding.  
- Write **modular apps** in Django for scalability.  
- Add **logging and monitoring** early to debug efficiently.  
- Keep the project **lightweight and iterative** – ship features step by step.

---

## Final Project: Online Poll System 🗳️

### 📌 Features
1. Create a poll with multiple choices.  
2. Allow users to vote.  
3. Display poll results in real time.  
4. Cache poll results in Redis for faster responses.  
5. Automatic cache invalidation when new votes are cast.  

### 🛠️ Tech Stack
- **Backend**: Django, Django REST Framework  
- **Database**: PostgreSQL  
- **Cache**: Redis  
- **Containerization**: Docker & Docker Compose  
- **Version Control**: GitHub  

---

## Running the Project
```bash
# Clone the repo
git clone https://github.com/<your-username>/alx-project-nexus.git
cd alx-project-nexus

# Build and start services
docker-compose up --build
