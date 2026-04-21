from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class ClassCreate(BaseModel):
    name: str
    section: str

class ClassUpdate(BaseModel):
    name: Optional[str] = None
    section: Optional[str] = None

class ClassResponse(BaseModel):
    id: int
    name: str
    section: str
    model_config = ConfigDict(from_attributes=True)

class ClassListResponse(BaseModel):
    total: int
    skip: int
    limit: int
    data: List[ClassResponse]
    model_config = ConfigDict(from_attributes=True)