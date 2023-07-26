from typing import Optional
from pydantic import BaseModel
from schemas.DispositifPubSchema import DispositifPubSchema
from schemas.TypePanneaux import TypePanneauSchema

class PanneauAffichSchema(DispositifPubSchema):
    IDPanneauAffich: int
    CodePanneau: str
    SuerfacePanneau: float
    NbreFacePanneau: int
    SpecificiteFact: bool
    UniteFacturationPanneau: str
    IDTypePanneau: int
    type_panneau: TypePanneauSchema

    class Config:
        orm_mode = True
        from_attributes = True

class PanneauAffichCreateSchema(BaseModel):
    CodeDispositifPub: str 
    LibelleDispoPub: str 
    SurfaceDispoPub: float 
    UniteFacturationDispoPub: str 
    IDTypeDispositif: int 
    IDEmplacementAffichage: int 
    IDTiers: int 
    CodePanneau: str
    SuerfacePanneau: float
    NbreFacePanneau: int
    SpecificiteFact: bool
    UniteFacturationPanneau: str
    IDTypePanneau: int

class PanneauAffichUpdateSchema(BaseModel):
    IDPanneauAffich: int
    CodeDispositifPub: Optional[str] = None
    LibelleDispoPub: Optional[str] = None
    SurfaceDispoPub: Optional[float] = None
    UniteFacturationDispoPub: Optional[str] = None
    IDTypeDispositif: Optional[int] = None
    IDEmplacementAffichage: Optional[int] = None
    IDTiers: Optional[int] = None
    CodePanneau: Optional[str] = None
    SuerfacePanneau: Optional[float] = None
    NbreFacePanneau: Optional[int] = None
    SpecificiteFact: Optional[bool] = None
    UniteFacturationPanneau: Optional[str] = None
    IDTypePanneau: Optional[int] = None
