from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.schemas.student_schema import student_create, student_update ,student_list_response
from app.controllers.student_controller import register_student, update_student_controller, delete_student_controller, get_students
from app.core.auth import get_current_user

router = APIRouter()


@router.post("/register")
def register(user: student_create, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return register_student(db, user, current_user)


@router.put("/update/{student_id}")
def update(student_id: int, user: student_update, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return update_student_controller(db, student_id, user)


@router.get("/list", response_model=student_list_response)
def list_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return get_students(db, skip, limit)


@router.delete("/delete/{student_id}")
def delete(student_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return delete_student_controller(db, student_id)