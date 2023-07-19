from typing import List, Optional
from pydantic import BaseModel

class TypeTiersSchema(BaseModel):
    IDTypeTiers: int
    LibelleTypeTiers: str

    class Config:
        orm_mode = True

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
    Logo: Optional[bytes]
    SigleTiers: Optional[str]
    type_tiers: TypeTiersSchema

    class Config:
        orm_mode = True

class TiersCreateSchema(BaseModel):
    CodeTiers: str
    LibelleTiers: Optional[str]
    AdresseTiers: Optional[str]
    TelephoneTiers: Optional[int]
    IDTypeTiers: int
    NumCont: Optional[str]
    EmailTiers: Optional[str]
    SigleTiers: Optional[str]
