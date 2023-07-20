from pydantic import BaseModel

from schemas.TiersSchema import TiersSchema

class DocEnteteSchema(BaseModel):
    IDDocEntete: int
    TypeDocEntete: int
    NumDocEntete: str
    DateDocEntete: str
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
    
class DocEnteteCreateSchema(BaseModel):
    TypeDocEntete: int
    NumDocEntete: str
    DateDocEntete: str
    MontantHTDoc: int
    MontantTaxeDoc: float
    MontantTTCDoc: float
    StatutDoc: str
    PenalitesDoc: int
    IDTiers: int

class DocEnteteUpdateSchema(BaseModel):
    IDDocEntete: int
    TypeDocEntete: int
    NumDocEntete: str
    DateDocEntete: str
    MontantHTDoc: int
    MontantTaxeDoc: float
    MontantTTCDoc: float
    StatutDoc: str
    PenalitesDoc: int
    IDTiers: int