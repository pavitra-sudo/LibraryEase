# app/main.py

from fastapi import FastAPI
from app.routes.user import user as user_routes
from app.core.initialize import initialize_database

app = FastAPI()

@app.on_event("startup")
def on_startup():
    initialize_database()

app.include_router(user_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to LibraryEase"}
