
from pydantic import BaseModel

from schemas.ZoneAffichage import ZoneAffichageSchema


class QuartierAffichageSchema(BaseModel):
    IDQuartierAffichage: int
    NomQuartier: str
    SousQuartierAffich: str
    ObservationsQuartier: str
    ArrondissementQaurtier: str
    IDZoneAffichage: int
    zone_affichage: ZoneAffichageSchema

    class Config:
        orm_mode = True
        from_attributes = True

class QuartierAffichageCreateSchema(BaseModel):
    NomQuartier: str
    SousQuartierAffich: str
    ObservationsQuartier: str
    ArrondissementQaurtier: str
    IDZoneAffichage: int

class QuartierAffichageUpdateSchema(BaseModel):
    IDQuartierAffichage: int
    NomQuartier: str
    SousQuartierAffich: str
    ObservationsQuartier: str
    ArrondissementQaurtier: str
    IDZoneAffichage: int