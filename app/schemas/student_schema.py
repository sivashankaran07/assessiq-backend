from pydantic import BaseModel ,ConfigDict
from typing import Optional ,List

class student_create(BaseModel):
    name: str
    email: str
    password: str
    class_id:int
    role: Optional[str] = None
    roll_no: Optional[str] = None
    std: str
    father_name: str
    mother_name: str
    father_occupation: str
    mother_occupation: str
    address: str
    phone: str
    dob: str
    gender: str
    blood_group: str
    religion: str
    nationality: str
    cast: Optional[str] = None
    community: Optional[str] = None

class student_update(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    class_id:Optional[int] = None
    role: Optional[str] = None
    roll_no: Optional[str] = None
    std: Optional[str] = None
    father_name: Optional[str] = None
    mother_name: Optional[str] = None
    father_occupation: Optional[str] = None
    mother_occupation: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    dob: Optional[str] = None
    gender: Optional[str] = None
    blood_group: Optional[str] = None
    religion: Optional[str] = None
    nationality: Optional[str] = None
    cast: Optional[str] = None
    community: Optional[str] = None

class student_response(BaseModel):
    id: int
    name: str
    email: str
    role: str
    roll_no: Optional[str]
    std: str
    model_config = ConfigDict(from_attributes=True)

class student_list_response(BaseModel):
    total: int
    skip: int
    limit: int
    data: List[student_response]
    model_config = ConfigDict(from_attributes=True)   