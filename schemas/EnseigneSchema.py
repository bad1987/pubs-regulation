from typing import Optional
from pydantic import BaseModel
from schemas.DispositifPubSchema import DispositifPubSchema
from schemas.TypeEnseigne import TypeEnseigneSchema

class EnseigneSchema(DispositifPubSchema):
    IDEnseigne: int
    CodeEnseigne: str
    SurfaceEnseigne: float
    NbreFaceEnseigne: int
    SpecificiteFacture: bool
    UniteFacturationEnseigne: str
    IDTypeEnseigne: int
    type_enseigne: TypeEnseigneSchema

    class config:
        orm_mode = True
        from_attributes = True

class EnseigneCreateSchema(BaseModel):
    CodeDispositifPub: str 
    LibelleDispoPub: str 
    SurfaceDispoPub: float 
    UniteFacturationDispoPub: str 
    IDTypeDispositif: int 
    IDEmplacementAffichage: int 
    IDTiers: int 
    CodeEnseigne: str
    SurfaceEnseigne: float
    NbreFaceEnseigne: int
    SpecificiteFacture: bool
    UniteFacturationEnseigne: str
    IDTypeEnseigne: int

class EnseigneUpdateSchema(BaseModel):
    IDEnseigne: int
    CodeDispositifPub: Optional[str] = None
    LibelleDispoPub: Optional[str] = None
    SurfaceDispoPub: Optional[float] = None
    UniteFacturationDispoPub: Optional[str] = None
    IDTypeDispositif: Optional[int] = None
    IDEmplacementAffichage: Optional[int] = None
    IDTiers: Optional[int] = None
    CodeEnseigne: Optional[str] = None
    SurfaceEnseigne: Optional[float] = None
    NbreFaceEnseigne: Optional[int] = None
    SpecificiteFacture: Optional[bool] = None
    UniteFacturationEnseigne: Optional[str] = None
    IDTypeEnseigne: Optional[int] = None