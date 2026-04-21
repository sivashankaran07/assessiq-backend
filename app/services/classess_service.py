from sqlalchemy.orm import Session
from app.models.classess import Class

def create_class(db: Session, classess):
    db_class = Class(**classess.dict())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

def update_class(db: Session, class_id: int, classess):
    db_class = db.query(Class).filter(Class.id == class_id).first()
    if not db_class:
        return None
    update_data = classess.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_class, key, value)
    db.commit()
    db.refresh(db_class)
    return db_class

def list_class(db: Session, skip: int = 0, limit: int = 10):
    total = db.query(Class).count()
    classes = db.query(Class).offset(skip).limit(limit).all()
    return {
        "total": total,
        "data": classes,
        "skip": skip,
        "limit": limit,
    }

def delete_class(db: Session, class_id: int):
    db_class = db.query(Class).filter(Class.id == class_id).first()
    if not db_class:
        return None
    db.delete(db_class)
    db.commit()
    return True