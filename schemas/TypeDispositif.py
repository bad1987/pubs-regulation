
from typing import Optional, List
from pydantic import BaseModel


class TypeDispositifSchema(BaseModel):
    IDTypeDispositif: int
    CodeTypeDispositif: str
    LibelleTypeDispo: str

    class Config:
        orm_mode = True
        from_attributes = True

class TypeDispositifCreateSchema(BaseModel):
    CodeTypeDispositif: str
    LibelleTypeDispo: str