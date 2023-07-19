
from typing import Optional
from pydantic import BaseModel

from schemas.DocEnteteSchema import DocEnteteSchema
from schemas.RepartitionFraisSchema import RepartitionFraisSchema


class RepDocSchema(BaseModel):
    IDRepDoc: int
    MontantReparti: float
    IDDocEntete: DocEnteteSchema
    IDRepartitionFrais: RepartitionFraisSchema

    class Config:
        orm_mode = True
        from_attributes = True

class RepDocCreateSchema(BaseModel):
    IDRepDoc: int
    MontantReparti: float
