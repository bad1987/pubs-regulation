from datetime import datetime
from typing import Optional
from pydantic import BaseModel, field_validator, validator

from schemas.TiersSchema import TiersSchema

class DocEnteteSchema(BaseModel):
    IDDocEntete: int
    TypeDocEntete: int
    NumDocEntete: str
    DateDocEntete: datetime
    MontantHTDoc: int
    MontantTaxeDoc: float
    MontantTTCDoc: float
    StatutDoc: str
    PenalitesDoc: int
    IDTiers: int
    tiers: TiersSchema

    class Config:
        orm_mode = True
        from_attributes = True
    
    @field_validator('DateDocEntete')
    def parse_date(cls, value):
        if isinstance(value, datetime):
            # Parse the string value using the desired format
            return value.isoformat()
        return value
    
class DocEnteteCreateSchema(BaseModel):
    TypeDocEntete: int
    MontantHTDoc: int
    MontantTaxeDoc: float
    MontantTTCDoc: float
    StatutDoc: str
    PenalitesDoc: int
    IDTiers: int

class DocEnteteUpdateSchema(BaseModel):
    IDDocEntete: int
    TypeDocEntete: int
    NumDocEntete: Optional[str]
    MontantHTDoc: int
    MontantTaxeDoc: float
    MontantTTCDoc: float
    StatutDoc: str
    PenalitesDoc: int
    IDTiers: int