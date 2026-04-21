from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.schemas.teacher_schema import teacher_create, teacher_update ,teacher_list_response
from app.controllers.teacher_controller import register_teacher, update_teacher_controller, delete_teacher_controller, get_teachers
from app.core.auth import get_current_user

router = APIRouter()

# current_user: dict = Depends(get_current_user)

@router.post("/register")
def register(user: teacher_create, db: Session = Depends(get_db)):
    return register_teacher(db, user)


@router.put("/update/{teacher_id}")
def update(teacher_id: int, user: teacher_update, db: Session = Depends(get_db) ):
    return update_teacher_controller(db, teacher_id, user)


@router.get("/list", response_model=teacher_list_response)
def list_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db) ):
    return get_teachers(db, skip, limit)


@router.delete("/delete/{teacher_id}")
def delete(teacher_id: int, db: Session = Depends(get_db) ):
    return delete_teacher_controller(db, teacher_id)