from datetime import date, datetime
from typing import List, ForwardRef, get_args
from pydantic import BaseModel, field_validator, validator

# from schemas import ProduitConsession

class CampagnePubSchema(BaseModel):
    IDCampagnePub: int
    CodeCampagne: str
    LibelleCampagne: str
    DateDeb: date
    DateFin: date
    SurfaceDispoitif: float

    @validator('produits', pre=True)
    def validate_produits(cls, v):
        from schemas.ProduitConsession import ProduitConsessionSchema
        return [ProduitConsessionSchema(**produit) for produit in v]
    
    produits: List['ProduitConsessionSchema'] = []

    class Config:
        orm_mode = True
        from_attributes = True

    @field_validator('DateDeb', 'DateFin')
    def parse_date(cls, v):
        if isinstance(v, str):
            return datetime.strptime(v, '%Y-%m-%d').date()
        elif isinstance(v, date):
            return v
        else:
            raise ValueError('Invalid date format')
        
class CampagnePubCreateSchema(BaseModel):
    CodeCampagne: str
    LibelleCampagne: str
    DateDeb: date
    DateFin: date
    SurfaceDispoitif: float

    @field_validator('DateDeb', 'DateFin')
    def parse_date(cls, v):
        if isinstance(v, str):
            return datetime.strptime(v, '%Y-%m-%d').date()
        elif isinstance(v, date):
            return v
        else:
            raise ValueError('Invalid date format')

class CampagnePubUpdateSchema(BaseModel):
    IDCampagnePub: int
    CodeCampagne: str
    LibelleCampagne: str
    DateDeb: date
    DateFin: date
    SurfaceDispoitif: float

    @field_validator('DateDeb', 'DateFin')
    def parse_date(cls, v):
        if isinstance(v, str):
            return datetime.strptime(v, '%Y-%m-%d').date()
        elif isinstance(v, date):
            return v
        else:
            raise ValueError('Invalid date format')