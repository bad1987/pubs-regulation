
from typing import Optional
from pydantic import BaseModel


class TaxesSchema(BaseModel):
    IDTaxes: int
    CodeTaxe: str
    LibelleTaxe: str
    TauxTaxe: float
    tiers: Optional[list]
    taxes_doc_entete: Optional[list]

    class Config:
        orm_mode = True

class TaxesCreateSchema(BaseModel):
    CodeTaxe: str
    LibelleTaxe: str
    TauxTaxe: float