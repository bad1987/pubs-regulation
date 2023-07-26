from pydantic import BaseModel

from schemas.TiersSchema import TiersSchema
from schemas.TaxesSchema import TaxesSchema
from schemas.DocEnteteSchema import DocEnteteSchema

class TaxTiersDocEnteteSchema(BaseModel):
    IDTiersDocEntete: int
    TauxTaxeTiersDocEnt: float
    IDTiers: int
    IDTaxes: int
    IDDocEntete: int
    tiers: TiersSchema
    taxe: TaxesSchema
    doc_entete: DocEnteteSchema

    class Config:
        orm_mode = True
        from_attributes = True

class TaxTiersDocEnteteCreateSchema(BaseModel):
    TauxTaxeTiersDocEnt: float
    IDTiers: int
    IDTaxes: int
    IDDocEntete: int

class TaxTiersDocEnteteUpdateSchema(BaseModel):
    IDTiersDocEntete: int
    TauxTaxeTiersDocEnt: float
    IDTiers: int
    IDTaxes: int
    IDDocEntete: int