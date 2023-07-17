from typing import List, Optional
from pydantic import BaseModel
from schemas.DispositifPubSchema import DispositifPubSchema
from schemas.DocEnteteSchema import DocEnteteSchema
from schemas.TaxTiersDocEnteteSchema import TaxTiersDocEnteteSchema
from schemas.TaxTiersSchema import TaxTiersSchema

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

    # Use nested schemas for the relationships
    dispositifs: List[DispositifPubSchema] # Assuming you have defined DispositifPubSchema
    documents: List[DocEnteteSchema]
    taxes: List[TaxTiersSchema]
    taxes_doc_entete: List[TaxTiersDocEnteteSchema]
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
