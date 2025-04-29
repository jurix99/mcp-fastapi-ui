from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services import users
from app.database import SessionLocal
from pydantic import BaseModel

router = APIRouter()

class UserCreate(BaseModel):
    name: str
    email: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = users.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return users.create_user(db, user.name, user.email)

@router.get("/users/{email}")
def read_user(email: str, db: Session = Depends(get_db)):
    user = users.get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
