# the schema for emplacementAffichage model

from pydantic import BaseModel
from schemas.QuartierAffichageSchema import QuartierAffichageSchema

class EmplacementAffichageSchema(BaseModel):
    IDEmplacementAffichage: int
    CodeEmplacement: str
    IDQuartierAffichage: int
    quartier: QuartierAffichageSchema

    class Config:
        orm_mode = True
        from_attributes = True

class EmplacementAffichageCreateSchema(BaseModel):
    CodeEmplacement: str
    IDQuartierAffichage: int

class EmplacementAffichageUpdateSchema(BaseModel):
    IDEmplacementAffichage: int
    CodeEmplacement: str
    IDQuartierAffichage: int