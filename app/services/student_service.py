from sqlalchemy.orm import Session
from app.models.student import Student
from app.core.security import hash_password
from app.core.logger import log_error


def create_student(db: Session, student):
    data = student.dict()
    data["password"] = hash_password(data["password"])
    
    # Auto increment roll_no logic
    last_student = db.query(Student).filter(Student.roll_no.like("ASS%")).order_by(Student.roll_no.desc()).first()
    
    if last_student and last_student.roll_no:
        try:
            # Extract digits from 'ASS0001'
            last_roll_num = int(last_student.roll_no[3:])
            new_roll_num = last_roll_num + 1
        except (ValueError, IndexError):
            new_roll_num = 1
    else:
        new_roll_num = 1
        
    data["roll_no"] = f"ASS{new_roll_num:04d}"
    
    db_student = Student(**data)

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def update_student(db: Session, student_id: int, student):
    db_student = db.query(Student).filter(Student.id == student_id).first()

    if not db_student:
        return None

    update_data = student.dict(exclude_unset=True)
    update_data.pop("roll_no", None)
    if "password" in update_data:
        update_data["password"] = hash_password(update_data["password"])
    for key, value in update_data.items():
        setattr(db_student, key, value)

    db.commit()
    db.refresh(db_student)

    return db_student

def list_student(db: Session, skip: int = 0, limit: int = 10):
    base_query = db.query(Student).order_by(Student.id)
    
    total = base_query.count()
    students = base_query.offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": students
    }

def delete_student(db: Session, student_id: int):
    db_student = db.query(Student).filter(Student.id == student_id).first()

    if not db_student:
        return None

    db.delete(db_student)
    db.commit()

    return True  