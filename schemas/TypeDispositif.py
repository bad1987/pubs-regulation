
from typing import Optional, List
from pydantic import BaseModel


class TypeDispositifSchema(BaseModel):
    IDTypeDispositif: int
    CodeTypeDispositif: str
    LibelleTypeDispo: str
    dispositifs: List[int] = []

    class Config:
        orm_mode = True

class TypeDispositifCreateSchema(BaseModel):
    CodeTypeDispositif: str
    LibelleTypeDispo: str