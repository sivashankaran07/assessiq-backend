from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, time

class schedule_create(BaseModel):
    teacher_id: int
    subject_id: int
    class_id: int
    date: date
    start_time: time
    end_time: time
    type: int

class schedule_update(BaseModel):
    teacher_id: Optional[int] = None
    subject_id: Optional[int] = None
    class_id: Optional[int] = None
    date: Optional[date] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    type: Optional[int] = None

class TeacherOut(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)

class ClassOut(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)

class SubjectOut(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True) 

class schedule_response(BaseModel):
    id: int 
    teacher: TeacherOut
    subject: SubjectOut
    class_: ClassOut
    date: date
    start_time: time
    end_time: time
    type: int
    model_config = ConfigDict(from_attributes=True) 

class schedule_list_response(BaseModel):
    total: int
    skip: int
    limit: int
    data: List[schedule_response]
    model_config = ConfigDict(from_attributes=True) 
