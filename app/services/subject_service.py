from app.models.subject import Subject
from sqlalchemy.orm import Session
from app.core.logger import log_error

def create_subjects(db: Session, subject):
    db_subject = Subject(**subject.dict())
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

def update_subjects(db: Session, subject_id: int, subject):
    db_subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not db_subject:
        return None
    update_data = subject.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_subject, key, value)
    db.commit()
    db.refresh(db_subject)
    return db_subject

def delete_subjects(db: Session, subject_id: int):
    db_subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not db_subject:
        return None
    db.delete(db_subject)
    db.commit()
    return True

# def get_subject(db: Session, subject_id: int):
#     return db.query(Subject).filter(Subject.id == subject_id).first()

def get_subjects(db: Session, skip: int = 0, limit: int = 10):
    base_query = db.query(Subject).order_by(Subject.id)
    total = base_query.count()
    subjects = base_query.offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": subjects
    }