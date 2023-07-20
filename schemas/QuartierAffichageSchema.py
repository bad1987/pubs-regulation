
from typing import Optional
from pydantic import BaseModel, Field

from schemas.ZoneAffichage import ZoneAffichageSchema


class QuartierAffichageSchema(BaseModel):
    IDQuartierAffichage: int
    NomQuartier: str
    SousQuartierAffich: str
    ObservationsQuartier: str
    ArrondissementQuartier: str
    IDZoneAffichage: int
    zone_affichage: ZoneAffichageSchema

    class Config:
        orm_mode = True
        from_attributes = True

class QuartierAffichageCreateSchema(BaseModel):
    NomQuartier: str
    SousQuartierAffich: str
    ObservationsQuartier: str
    ArrondissementQuartier: str
    IDZoneAffichage: int

class QuartierAffichageUpdateSchema(BaseModel):
    IDQuartierAffichage: Optional[int] = Field(..., description="The primary key of the quartier affichage")
    NomQuartier: Optional[str]
    SousQuartierAffich: Optional[str]
    ObservationsQuartier: Optional[str]
    ArrondissementQuartier: Optional[str]
    IDZoneAffichage: Optional[int] = Field(..., description="The foreign key of the zone affichage")
