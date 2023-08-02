from datetime import date, datetime
from typing import ForwardRef, List, Optional
from pydantic import BaseModel, field_validator

from schemas.DispositifPubSchema import DispositifPubSchema
ProduitConsessionSchemaRef = ForwardRef('ProduitConsessionSchema')


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

class CampagneProduitUpdateSchema(BaseModel):
    IDCampagneProduit: int
    SurfaceFacturable: Optional[float] = None
    IDProduitConcession: int
    IDCampagnePub: int

class CampagnePubSchema(BaseModel):
    IDCampagnePub: int
    CodeCampagne: str
    LibelleCampagne: str
    DateDeb: date
    DateFin: date
    SurfaceDispositif: float
    produits: List[CampagneProduitSchema] = []

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
    SurfaceDispositif: float
    produits_campagne: List[CampagneProduitCreateSchema] = []

    @field_validator('produits_campagne', mode='before')
    def validate_produits_ids(cls, v):
        # Add your validation logic here
        # For example, you could check if the integers in v correspond to valid primary keys of ProduitConsession instances
        return v

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
    SurfaceDispositif: float

    @field_validator('DateDeb', 'DateFin')
    def parse_date(cls, v):
        if isinstance(v, str):
            return datetime.strptime(v, '%Y-%m-%d').date()
        elif isinstance(v, date):
            return v
        else:
            raise ValueError('Invalid date format')

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

    campagnes: List[CampagneProduitSchema] = []

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
