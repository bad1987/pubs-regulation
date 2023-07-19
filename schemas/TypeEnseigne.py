
from typing import Optional, List
from pydantic import BaseModel

class TypeEnseigneSchema(BaseModel):
    IDTypeEnseigne: Optional[int]
    CodeTypeEnseigne: Optional[str]
    LibelleTypeEnseigne: Optional[str]

    class Config:
        orm_mode = True
        from_attributes = True

class TypeEnseigneCreateSchema(BaseModel):
    CodeTypeEnseigne: Optional[str]
    LibelleTypeEnseigne: Optional[str]