
from typing import List, Optional
from pydantic import BaseModel

from schemas.DispositifPubSchema import DispositifPubSchema
from schemas.CampagneSchema import CampagnePubSchema

class ProduitConsessionSchema(BaseModel):
    IDProduitConcession: int
    CodeProduitConcession: str
    ObservationsProduit: str
    DureeMinimaleFacturation: int
    HasSpecificiteFacturation: bool
    SurfaceMinSpecificiteFact: Optional[float] = None
    TauxApplicableSpecificiteFact: Optional[float] = None
    IDDispositifPub: int
    dispositif_pub: DispositifPubSchema
    campagnes: List[CampagnePubSchema] = []

    class Config:
        orm_mode = True
        from_attributes = True

class ProduitConsessionCreateSchema(BaseModel):
    CodeProduitConcession: str
    ObservationsProduit: str
    DureeMinimaleFacturation: int
    HasSpecificiteFacturation: bool
    SurfaceMinSpecificiteFact: Optional[float] = None
    TauxApplicableSpecificiteFact: Optional[float] = None
    IDDispositifPub: int

class ProduitConsessionUpdateSchema(BaseModel):
    IDProduitConcession: int
    CodeProduitConcession: str
    ObservationsProduit: str
    DureeMinimaleFacturation: int
    HasSpecificiteFacturation: bool
    SurfaceMinSpecificiteFact: Optional[float] = None
    TauxApplicableSpecificiteFact: Optional[float] = None
    IDDispositifPub: int