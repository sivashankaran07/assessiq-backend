from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.schemas.schedule_schema import schedule_create, schedule_update ,schedule_list_response
from app.controllers.schedule_controller import create_schedule_controller, update_schedule_controller, delete_schedule_controller, get_schedule_controller, get_schedules_controller
from app.core.auth import get_current_user

router = APIRouter()


@router.post("/create")
def create(schedule: schedule_create, db: Session = Depends(get_db)):
    return create_schedule_controller(db, schedule)


@router.put("/update/{schedule_id}")
def update(schedule_id: int, schedule: schedule_update, db: Session = Depends(get_db)):
    return update_schedule_controller(db, schedule_id, schedule)


@router.get("/list", response_model=schedule_list_response)
def list_schedules(skip: int = 0, limit: int = 10, db: Session = Depends(get_db),class_id: int = None,start_date=None,end_date=None):
    return get_schedules_controller(db, skip, limit,class_id,start_date,end_date)


@router.delete("/delete/{schedule_id}")
def delete(schedule_id: int, db: Session = Depends(get_db)):
    return delete_schedule_controller(db, schedule_id)


@router.get("/{schedule_id}")
def get(schedule_id: int, db: Session = Depends(get_db)):
    return get_schedule_controller(db, schedule_id)