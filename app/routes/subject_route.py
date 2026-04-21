from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.schemas.subject_schema import subject_create, subject_update ,subject_list_response
from app.controllers.subject_controller import create_subject, update_subject, delete_subject, get_all_subjects
from app.core.auth import get_current_user

router = APIRouter()

# current_user: dict = Depends(get_current_user)

@router.post("/register")
def register(user: subject_create, db: Session = Depends(get_db)):
    return create_subject(db, user)


@router.put("/update/{student_id}")
def update(student_id: int, user: subject_update, db: Session = Depends(get_db)):
    return update_subject(db, student_id, user)


@router.get("/list", response_model=subject_list_response)
def list_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_all_subjects(db, skip, limit)


@router.delete("/delete/{student_id}")
def delete(student_id: int, db: Session = Depends(get_db)):
    return delete_subject(db, student_id)
