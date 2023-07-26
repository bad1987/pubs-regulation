
from pydantic import BaseModel

from schemas.TaxesSchema import TaxesSchema
from schemas.TiersSchema import TiersSchema

class TaxTiersSchema(BaseModel):
    IDTaxTiers: int
    IDTiers: int
    IDTaxes: int
    tiers: TiersSchema
    taxe: TaxesSchema

    class Config:
        orm_mode = True
        from_attributes = True

class TaxTiersCreateSchema(BaseModel):
    IDTiers: int
    IDTaxes: int

class TaxTiersUpdateSchema(BaseModel):
    IDTaxTiers: int
    IDTiers: int
    IDTaxes: int