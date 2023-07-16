
from ast import List
from typing import Optional
from pydantic import BaseModel

class TypeEnseigneSchema(BaseModel):
    IDTypeEnseigne: Optional[int]
    CodeTypeEnseigne: Optional[str]
    LibelleTypeEnseigne: Optional[str]
    enseignes: List[int] = []

    class Config:
        orm_mode = True

class TypeEnseigneCreateSchema(BaseModel):
    CodeTypeEnseigne: Optional[str]
    LibelleTypeEnseigne: Optional[str]