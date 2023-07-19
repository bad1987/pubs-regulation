
from typing import Optional
from pydantic import BaseModel

from schemas.DocEnteteSchema import DocEnteteSchema
from schemas.RepartitionFraisSchema import RepartitionFraisSchema


class RepDocSchema(BaseModel):
    IDRepDoc: int
    MontantReparti: float
    IDDocEntete: int
    IDRepartitionFrais: int
    doc_entete: DocEnteteSchema
    repartition_frais: RepartitionFraisSchema

    class Config:
        orm_mode = True
        from_attributes = True

class RepDocCreateSchema(BaseModel):
    MontantReparti: float
    IDDocEntete: int
    IDRepartitionFrais: int
