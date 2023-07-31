from typing import Optional
from pydantic import BaseModel

class CampagneProduitSchema(BaseModel):
    IDCampagneProduit: int
    SurfaceFacturable: Optional[float] = None
    IDProduitConcession: int
    IDCampagnePub: int

    class Config:
        orm_mode = True
        from_attributes = True

class CampagneProduitCreateSchema(BaseModel):
    SurfaceFacturable: Optional[float] = None
    IDProduitConcession: int
    IDCampagnePub: int

class CampagneProduitUpdateSchema(BaseModel):
    IDCampagneProduit: int
    SurfaceFacturable: Optional[float] = None
    IDProduitConcession: int
    IDCampagnePub: int