# ALX Project Nexus 🚀

## Overview
This repository documents my major learnings from the **ProDev Backend Engineering Program** at ALX.  
It also showcases my final project, an **Online Poll System**, built using **Django** and **Django REST Framework (DRF)**.

---

## Program Learnings

### 🔑 Key Technologies
- **Python** – core backend programming language.
- **Django** – web framework with ORM and built-in admin.
- **Django REST Framework (DRF)** – for building APIs.
- **Swagger (drf-yasg)** – for auto-generated API documentation.
- **Authentication** – token-based user authentication.
- **Environment Variables** – secure handling of sensitive info.

### 📚 Important Backend Concepts
- **Database Design** – modeling users, polls, options, and votes.
- **REST APIs** – CRUD operations for resources.
- **Authentication & Permissions** – restricting poll creation to logged-in users.
- **Settings Management** – using `.env` for secrets and configs.

### ⚡ Challenges & Solutions
- **Challenge**: Exposing sensitive info in `settings.py`.  
  **Solution**: Moved secrets into `.env` and loaded them with `python-decouple`.  

- **Challenge**: Errors in Swagger Docs when serializers were misconfigured.  
  **Solution**: Fixed invalid fields in serializers and adjusted views.  

- **Challenge**: Restricting who can create polls.  
  **Solution**: Added authentication and custom `get_permissions()` in views.  

### ✅ Best Practices & Takeaways
- Always use `.env` for secrets (never commit sensitive info).  
- Add Swagger early to visualize APIs and debug.  
- Restrict write operations with authentication.  
- Keep the app modular (separate `polls` app, serializers, views, urls).  

---

## Final Project: Online Poll System 🗳️

### 📌 Features
1. Create polls with multiple choices.  
2. Allow users to vote.  
3. View poll results.  
4. Restrict poll creation to authenticated users.  
5. Interactive API docs via Swagger (`/api/docs`).  

### 🛠️ Tech Stack
- **Backend**: Django, Django REST Framework  
- **Database**: SQLite (default, can switch to PostgreSQL later)  
- **Auth**: Token Authentication (DRF)  
- **Docs**: Swagger via drf-yasg  

---

## Running the Project

### 1️⃣ Clone the repo
```bash
git clone https://github.com/<your-username>/alx-project-nexus.git
cd alx-project-nexus
