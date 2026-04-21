from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserLogin
from app.controllers.auth_controller import register_controller, login_controller
from app.db.dependencies import get_db

router = APIRouter()



@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_controller(db, user)


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_controller(db, user)