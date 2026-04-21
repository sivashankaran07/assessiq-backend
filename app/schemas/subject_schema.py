from pydantic import BaseModel, ConfigDict
from typing import List,Optional

class subject_create(BaseModel):
    name: str

class subject_update(BaseModel):
    name: Optional[str] = None

class subject_response(BaseModel):
    id: int
    name: str
   
    model_config = ConfigDict(from_attributes=True)

class subject_list_response(BaseModel):
    total: int
    skip: int
    limit: int
    data: List[subject_response]
    model_config = ConfigDict(from_attributes=True) 