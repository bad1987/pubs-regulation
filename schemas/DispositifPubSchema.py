from typing import Optional
from pydantic import BaseModel
from schemas.EmplacementAffichageSchema import EmplacementAffichageSchema
from schemas.TiersSchema import TiersSchema

from schemas.TypeDispositif import TypeDispositifSchema

class DispositifPubSchema(BaseModel):
    IDDispositifPub: int
    CodeDispositifPub: str
    LibelleDispoPub: str
    SurfaceDispoPub: float
    UniteFacturationDispoPub: str
    IDTypeDispositif: int
    IDEmplacementAffichage: int
    IDTiers: int
    type_dispositif: TypeDispositifSchema
    tiers: TiersSchema
    emplacement_affichage: EmplacementAffichageSchema

    class Config:
        orm_mode = True
        from_attributes = True

class DispositifPubCreateSchema(BaseModel):
    CodeDispositifPub: str 
    LibelleDispoPub: str 
    SurfaceDispoPub: float 
    UniteFacturationDispoPub: str 
    IDTypeDispositif: int 
    IDEmplacementAffichage: int 
    IDTiers: int 

class DispositifPubUpdateSchema(BaseModel):
    IDDispositifPub: int
    CodeDispositifPub: Optional[str] = None
    LibelleDispoPub: Optional[str] = None
    SurfaceDispoPub: Optional[float] = None
    UniteFacturationDispoPub: Optional[str] = None
    IDTypeDispositif: Optional[int] = None
    IDEmplacementAffichage: Optional[int] = None
    IDTiers: Optional[int] = None