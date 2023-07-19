
from datetime import datetime
from pydantic import BaseModel


class RepartitionFraisSchema(BaseModel):
    IDRepartitionFrais: int
    IntervenantEntite: str
    TauxRepartition: float
    AnneeRepart: datetime

    class Config:
        orm_mode = True
        from_attributes = True

class RepartitionFraisCreateSchema(BaseModel):
    IntervenantEntite: str
    TauxRepartition: float
    AnneeRepart: datetime