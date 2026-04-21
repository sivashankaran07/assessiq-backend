from sqlalchemy import Column, Integer, String, DateTime
from app.db.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    section = Column(String)
    status = Column(Integer, default=1)  # 1=active, 2=inactive
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    schedules = relationship("Schedule", back_populates="class_")