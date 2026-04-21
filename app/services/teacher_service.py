from sqlalchemy.orm import Session
from app.models.teacher import Teacher
from app.core.security import hash_password
from app.core.logger import log_error
from sqlalchemy import func, Integer

def create_teacher(db: Session, teacher):
    data = teacher.dict()
    data["password"] = hash_password(data["password"])
    
    # Auto increment teacher_id logic
    last_teacher = db.query(Teacher).order_by(func.substring(Teacher.teacher_id, 4).cast(Integer).desc()
).first()
    if last_teacher and last_teacher.teacher_id:

        try:
            last_teacher_id = int(last_teacher.teacher_id[3:])
            new_teacher_id = last_teacher_id + 1
        except (ValueError, IndexError):
            new_teacher_id = 1
    else:
        new_teacher_id = 1
        
    data["teacher_id"] = f"EMP{new_teacher_id:04d}"
    
    db_teacher = Teacher(**data)

    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)

    return db_teacher


def update_teacher(db: Session, teacher_id: int, teacher):
    db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()

    if not db_teacher:
        return None

    update_data = teacher.dict(exclude_unset=True)
    update_data.pop("teacher_id", None)
    if "password" in update_data:
        update_data["password"] = hash_password(update_data["password"])
    for key, value in update_data.items():
        setattr(db_teacher, key, value)

    db.commit()
    db.refresh(db_teacher)

    return db_teacher

def list_teacher(db: Session, skip: int = 0, limit: int = 10):
    base_query = db.query(Teacher).order_by(Teacher.id)
    
    total = base_query.count()
    teachers = base_query.offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": teachers
    }

def delete_teacher(db: Session, teacher_id: int):
    db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()

    if not db_teacher:
        return None

    db.delete(db_teacher)
    db.commit()

    return True  