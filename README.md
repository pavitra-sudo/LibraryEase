# 📚 LibraryEase – Backend API

LibraryEase is a modular and beginner-friendly backend system for managing a library. It is built using FastAPI, PostgreSQL, and follows clean code principles like SOLID to ensure maintainability and scalability.

---

## 🛠️ Tech Stack

- **Backend Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Password Security**: Passlib (bcrypt)
- **Modular Structure**: Follows SOLID principles
- **Version Control**: Git + GitHub

---

## 📁 Project Structure

```
LibraryEase/
├── app/
│   ├── main.py                 # FastAPI app entrypoint
│   ├── core/
│   │   ├── database.py         # DB connection & session
│   │   ├── initialize.py       # DB tables creation
│   │   └── security.py         # Password hashing utilities
│   ├── models/
│   │   └── user.py             # SQLAlchemy User model
│   ├── schemas/
│   │   └── user.py             # Pydantic User schemas
│   ├── routes/
│   │   └── user.py             # API route definitions
│   └── services/
│       └── user.py             # User service logic (CRUD)
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ✨ Features

- User creation with password hashing
- Clean and modular folder structure
- PostgreSQL integration
- Automatic table creation on app startup
- Ready-to-extend service and routing structure

---

## 🚀 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/pavitra-sudo/LibraryEase.git
cd LibraryEase

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload
```

---

## 🔐 Example: Create User API

```http
POST /users/
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "secure123"
}
```

---

## ⚙️ .gitignore Best Practice

```bash
# Add to .gitignore
__pycache__/
*.pyc
venv/
.env
```

---

## 🤝 Contributions

This is a beginner-friendly backend project. Fork it, try it, and grow with it 🚀

---

## 🧠 Author

[Pavitra N Dubey](https://github.com/pavitra-sudo)