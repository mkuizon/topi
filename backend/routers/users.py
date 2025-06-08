# backend/users.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from db import get_db_connection

router = APIRouter(prefix="/users", tags=["Users"])

# defining request body
class UserCreate(BaseModel):
    name: str
    email: EmailStr

@router.post("/")
def create_user(user: UserCreate):
    conn = get_db_connection()

    cur = conn.cursor()

    try:
        # checking if email exists
        cur.execute("SELECT * FROM users WHERE email = %s", (user.email,))
        existing = cur.fetchone()

        if existing:
            raise HTTPException(status_code=400, detail="Email is already registered.")
        
        # insert new user
        cur.execute("INSERT INTO users (name, email)")