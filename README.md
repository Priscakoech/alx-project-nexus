# ALX Project Nexus 🚀

## 📖 Overview

This repository captures my major learnings from the **ProDev Backend Engineering Program** at **ALX**,
and showcases my final project – an **Online Poll System** built with **Django** and **Django REST Framework (DRF)**.

---

## 🧑‍💻 Program Learnings

### 🔑 Key Technologies

* **Python** – core backend programming language
* **Django** – web framework with ORM and admin dashboard
* **Django REST Framework (DRF)** – for building APIs
* **Swagger (drf-yasg)** – API documentation & testing
* **Authentication** – Token-based authentication with DRF
* **Environment Variables** – secure handling of secrets with `.env`

### 📚 Important Backend Concepts

* **Database Design** → modeling users, polls, options, and votes
* **REST APIs** → CRUD operations for resources
* **Authentication & Permissions** → restricting poll creation to logged-in users
* **Settings Management** → using `.env` for sensitive configurations

### ⚡ Challenges & Solutions

* **Sensitive Info in Settings**

  * *Challenge*: API keys and secrets exposed in `settings.py`
  * *Solution*: Moved them to `.env` with `python-decouple`

* **Swagger Errors**

  * *Challenge*: Invalid serializers breaking docs
  * *Solution*: Fixed serializer fields and view configurations

* **Restricting Poll Creation**

  * *Challenge*: Any user could create polls
  * *Solution*: Enforced authentication via `get_permissions()`

### ✅ Best Practices & Takeaways

* Always store secrets in `.env` (never commit to GitHub)
* Add Swagger early to debug and visualize APIs
* Restrict write operations with authentication/permissions
* Keep apps modular (`polls` app, serializers, views, urls)

---

## 🗳️ Final Project: Online Poll System

### 📌 Features

1. Create polls with multiple options
2. Vote on poll options (one vote per user/IP per poll)
3. View real-time poll results
4. Restrict poll creation to authenticated users
5. Interactive API docs via Swagger (`/api/docs`)

### 🛠️ Tech Stack

* **Backend**: Django + DRF
* **Database**: SQLite (default) → easy to switch to PostgreSQL
* **Auth**: DRF Token Authentication
* **Docs**: Swagger & ReDoc (`drf-yasg`)

---

## 🚀 Running the Project

### 1️⃣ Clone the repo

```bash
git clone https://github.com/<your-username>/alx-project-nexus.git
cd alx-project-nexus
```

### 2️⃣ Create & activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file in the root:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 5️⃣ Run migrations

```bash
python manage.py migrate
```

### 6️⃣ Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 7️⃣ Start the server

```bash
python manage.py runserver
```

---

## 🔑 Authentication

Generate a token for a user:

```bash
python manage.py drf_create_token <username>
```

Use it in requests:

```
Authorization: Token your-generated-token
```

---

## 📑 API Endpoints

### Polls

* `GET /api/polls/` → list all polls
* `POST /api/polls/` → create a poll
* `GET /api/polls/{id}/` → retrieve poll details
* `PUT /api/polls/{id}/` → update a poll
* `DELETE /api/polls/{id}/` → delete a poll

### Votes

* `POST /api/polls/{poll_id}/vote/{option_id}/` → vote for an option

### Results

* `GET /api/polls/{poll_id}/results/` → view poll results

---

## 📖 API Documentation

* Swagger UI → `http://127.0.0.1:8000/api/docs/`
* ReDoc → `http://127.0.0.1:8000/api/redoc/`

---

## 🧪 Testing

* Use Swagger UI or ReDoc for interactive testing
* Use **Postman/cURL** for API calls

---


