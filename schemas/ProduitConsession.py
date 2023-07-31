from typing import List, Optional
from pydantic import BaseModel, validator

from schemas.DispositifPubSchema import DispositifPubSchema
# from  schemas import CampagneSchema

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

    @validator('campagnes', pre=True)
    def validate_campagnes(cls, v):
        from schemas.CampagneSchema import CampagnePubSchema
        return [CampagnePubSchema(**campagne) for campagne in v]

    campagnes: List['CampagnePubSchema'] = []

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