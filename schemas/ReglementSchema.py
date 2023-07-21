
from datetime import date, datetime

from pydantic import BaseModel, validator

from schemas.DocEnteteSchema import DocEnteteSchema


class ReglementSchema(BaseModel):
    IDReglement: int
    NumReglt: str
    DateReglt: datetime
    MontantRegle: int
    SoldeRglt: float
    StatutRglt: str
    ModeRglt: str
    IDDocEntete: int
    doc_entete: DocEnteteSchema

    class Config:
        orm_mode = True
        from_attributes = True
    
    @validator('DateReglt', pre=True)
    def parse_date(cls, value):
        if isinstance(value, datetime):
            # Parse the string value using the desired format
            return value.isoformat()
        return value

class ReglementCreateSchema(BaseModel):
    NumReglt: str
    DateReglt: datetime
    MontantRegle: int
    SoldeRglt: float
    StatutRglt: str
    ModeRglt: str
    IDDocEntete: int
        
    @validator('DateReglt', pre=True)
    def parse_date(cls, value):
        if isinstance(value, datetime):
            # Parse the string value using the desired format
            return value.isoformat()
        return value

class ReglementUpdateSchema(BaseModel):
    IDReglement: int
    NumReglt: str
    DateReglt: datetime
    MontantRegle: int
    SoldeRglt: float
    StatutRglt: str
    ModeRglt: str
    IDDocEntete: int
        
    @validator('DateReglt', pre=True)
    def parse_date(cls, value):
        if isinstance(value, datetime):
            # Parse the string value using the desired format
            return value.isoformat()
        return value