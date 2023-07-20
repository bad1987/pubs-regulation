
from typing import Optional
from pydantic import BaseModel

from schemas.DispositifPubSchema import DispositifPubSchema


class ProduitConsessionSchema(BaseModel):
    IDProduitConcession: int
    CodeProduitConcession: str
    ObservationsProduit: str
    IDDispositifPub: int
    dispositif_pub: DispositifPubSchema

    class Config:
        orm_mode = True
        from_attributes = True

class ProduitConsessionCreateSchema(BaseModel):
    CodeProduitConcession: str
    ObservationsProduit: str
    IDDispositifPub: int

class ProduitConsessionUpdateSchema(BaseModel):
    IDProduitConcession: int
    CodeProduitConcession: str
    ObservationsProduit: str
    IDDispositifPub: Optional[int]