
# this class defines a pydantic schema for the zoneAffichage model
from ast import List
from typing import Optional
from pydantic import BaseModel


class ZoneAffichageSchema(BaseModel):
    IDZoneAffichage: Optional[int]
    CodeZone: Optional[str]
    LibelleZone: Optional[str]
    quartiers: Optional[list]

    class Config:
        orm_mode = True

class ZoneAffichageCreateSchema(BaseModel):
    CodeZone: Optional[str]
    LibelleZone: Optional[str]
    quartiers: List[int] = []

