
# this class defines a pydantic schema for the zoneAffichage model
from typing import Optional, List
from pydantic import BaseModel


class ZoneAffichageSchema(BaseModel):
    IDZoneAffichage: Optional[int]
    CodeZone: Optional[str]
    LibelleZone: Optional[str]

    class Config:
        orm_mode = True
        from_attributes = True

class ZoneAffichageCreateSchema(BaseModel):
    CodeZone: Optional[str]
    LibelleZone: Optional[str]

