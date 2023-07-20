from typing import List, Optional
from pydantic import BaseModel

class TypeTiersSchema(BaseModel):
    IDTypeTiers: int
    LibelleTypeTiers: str

    class Config:
        orm_mode = True
        from_attributes = True

class TypeTiersCreateSchema(BaseModel):
    LibelleTypeTiers: str


# Define the schema for the Tiers model
class TiersSchema(BaseModel):
    IDTiers: int
    CodeTiers: str
    LibelleTiers: Optional[str]
    AdresseTiers: Optional[str]
    TelephoneTiers: Optional[int]
    IDTypeTiers: int
    NumCont: Optional[str]
    EmailTiers: Optional[str]
    Logo: Optional[str]
    SigleTiers: Optional[str]
    type_tiers: TypeTiersSchema

    class Config:
        orm_mode = True
        from_attributes = True

class TiersCreateSchema(BaseModel):
    CodeTiers: str
    LibelleTiers: Optional[str]
    AdresseTiers: Optional[str]
    TelephoneTiers: Optional[int]
    IDTypeTiers: int
    NumCont: Optional[str]
    EmailTiers: Optional[str]
    SigleTiers: Optional[str]

class TiersUpdateSchema(BaseModel):
    IDTiers: Optional[int]
    CodeTiers: Optional[str]
    LibelleTiers: Optional[str]
    AdresseTiers: Optional[str]
    TelephoneTiers: Optional[int]
    IDTypeTiers: Optional[int]
    NumCont: Optional[str]
    EmailTiers: Optional[str]
    SigleTiers: Optional[str]