from pydantic import BaseModel, ConfigDict
from typing import List , Optional

class student_class_create(BaseModel):
    student_id: int
    class_id: int

class student_class_update(BaseModel):
    student_id: Optional[int] = None
    class_id: Optional[int] = None

class student_class_response(BaseModel):
    id: int
    student_id: int
    class_id: int
    model_config = ConfigDict(from_attributes=True)

class student_class_list_response(BaseModel):
    total: int
    skip: int
    limit: int
    data: List[student_class_response]
    model_config = ConfigDict(from_attributes=True)