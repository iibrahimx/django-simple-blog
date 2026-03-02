# Django Simple Blog 📝

A simple practice blog web application built with Django that allows users to create accounts, write blog posts, and comment on posts.  
This project demonstrates core Django concepts including authentication, models, views, templates, CRUD operations, and deployment.

---

## 🚀 Live Demo

**Deployed Application:**

- https://django-simple-blog.onrender.com

---

## ✨ Features

- User authentication (sign up, login, logout)
- Create, edit, and delete blog posts (author-only permissions)
- Comment system on blog posts
- Responsive layout for mobile and desktop
- Django Admin panel for managing content
- Deployed to Render with PostgreSQL

---

## 🛠️ Tech Stack

- **Backend:** Django 5
- **Database:** PostgreSQL (production), SQLite (local)
- **Frontend:** Django Templates + CSS
- **Deployment:** Render
- **Static Files:** WhiteNoise
- **Server:** Gunicorn + Uvicorn workers

---

## 📂 Project Structure

```text
django-simple-blog/
├── accounts/        # Authentication (signup)
├── posts/           # Blog posts and comments
├── config/          # Project settings and URLs
├── templates/       # Global templates (base, auth)
├── static/          # CSS and static assets
├── manage.py
└── requirements.txt
└── README.md
```

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/iibrahimx/django-simple-blog.git
cd django-simple-blog
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (admin)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open:
http://127.0.0.1:8000
Admin panel: http://127.0.0.1:8000/admin

## 🔐 Environment Variables (Production)

The following environment variables are required in production:

```env
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=postgres://...
ALLOWED_HOSTS=your-app.onrender.com
```

## 📦 Deployment

This project is deployed on Render using:

- build.sh for build steps
- PostgreSQL database
- Gunicorn with Uvicorn workers
- WhiteNoise for static files

## 🧪 Notes

- Only authenticated users can create posts
- Only post authors can edit or delete their posts
- Comments require authentication
- Logout is handled securely using POST requests

## 👤 Author

**Ibrahim Ibrahim**
GitHub: https://github.com/iibrahimx

## 📄 License

This project is for learning and portfolio purposes.
