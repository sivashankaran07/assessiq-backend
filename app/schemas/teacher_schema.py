from pydantic import BaseModel ,ConfigDict
from typing import Optional ,List

class teacher_create(BaseModel):
    name:str
    email:str
    password:str
    teacher_id:Optional[str]=None
    role:Optional[str]=None
    subject:str
    phone:str
    address:str
    gender:str
    dob:str
    blood_group:str
    religion:str
    nationality:str
    cast:Optional[str]=None
    community:Optional[str]=None
    status:Optional[int]=None
    
class teacher_update(BaseModel):
    name:Optional[str]=None
    email:Optional[str]=None
    password:Optional[str]=None
    teacher_id:Optional[str]=None
    role:Optional[str]=None
    subject:Optional[str]=None
    phone:Optional[str]=None
    address:Optional[str]=None
    gender:Optional[str]=None
    dob:Optional[str]=None
    blood_group:Optional[str]=None
    religion:Optional[str]=None
    nationality:Optional[str]=None
    cast:Optional[str]=None
    community:Optional[str]=None
    status:Optional[int]=None

class teacher_response(BaseModel):
    id: int
    name: str
    email: str
    teacher_id:str
    subject: str
    model_config = ConfigDict(from_attributes=True) 

class teacher_list_response(BaseModel):
    total: int
    skip: int
    limit: int
    data: List[teacher_response]
    model_config = ConfigDict(from_attributes=True)   