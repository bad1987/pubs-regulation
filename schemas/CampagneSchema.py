from datetime import datetime
from pydantic import BaseModel, field_validator, validator

from schemas.ProduitConsession import ProduitConsessionSchema

class CampagnePubSchema(BaseModel):
    IDCampagnePub: int
    CodeCampagne: str
    LibelleCampagne: str
    DateDeb: datetime
    DateFin: datetime
    SurfaceDispoitif: float
    IDProduitConcession: int
    produit: ProduitConsessionSchema

    class Config:
        orm_mode = True
        from_attributes = True
    
    @field_validator('DateDeb', mode='before')
    def parse_date(cls, value):
        if isinstance(value, datetime):
            # Parse the string value using the desired format
            return value.isoformat()
        return value
    
    @field_validator('DateFin', mode='before')
    def parse_date(cls, value):
        if isinstance(value, datetime):
            # Parse the string value using the desired format
            return value.isoformat()
        return value

class CampagnePubCreateSchema(BaseModel):
    CodeCampagne: str
    LibelleCampagne: str
    DateDeb: datetime
    DateFin: datetime
    SurfaceDispoitif: float
    IDProduitConcession: int

    @field_validator('DateDeb', mode='before')
    def parse_date(cls, value):
        if isinstance(value, datetime):
            # Parse the string value using the desired format
            return value.isoformat()
        return value
    
    @field_validator('DateFin', mode='before')
    def parse_date(cls, value):
        if isinstance(value, datetime):
            # Parse the string value using the desired format
            return value.isoformat()
        return value

class CampagnePubUpdateSchema(BaseModel):
    IDCampagnePub: int
    CodeCampagne: str
    LibelleCampagne: str
    DateDeb: datetime
    DateFin: datetime
    SurfaceDispoitif: float
    IDProduitConcession: int

    @field_validator('DateDeb', mode='before')
    def parse_date(cls, value):
        if isinstance(value, datetime):
            # Parse the string value using the desired format
            return value.isoformat()
        return value
    
    @field_validator('DateFin', mode='before')
    def parse_date(cls, value):
        if isinstance(value, datetime):
            # Parse the string value using the desired format
            return value.isoformat