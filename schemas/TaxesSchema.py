
from typing import Optional
from pydantic import BaseModel


class TaxesSchema(BaseModel):
    IDTaxes: int
    CodeTaxe: str
    LibelleTaxe: str
    TauxTaxe: float

    class Config:
        orm_mode = True
        from_attributes = True

class TaxesCreateSchema(BaseModel):
    CodeTaxe: str
    LibelleTaxe: str
    TauxTaxe: float