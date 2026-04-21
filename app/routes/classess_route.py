from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.schemas.classess_schema import ClassCreate, ClassUpdate,ClassListResponse
from app.controllers.classess_controller import register_class, update_class_controller, delete_class_controller, get_classes
from app.core.auth import get_current_user

router = APIRouter()


@router.post("/register")
def register(user: ClassCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return register_class(db, user, current_user)


@router.put("/update/{class_id}")
def update(class_id: int, user: ClassUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return update_class_controller(db, class_id, user,current_user )


@router.get("/list", response_model=ClassListResponse)
def list_classes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return get_classes(db, current_user, skip, limit)


@router.delete("/delete/{class_id}")
def delete(class_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return delete_class_controller(db, current_user, class_id)