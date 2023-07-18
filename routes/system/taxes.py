import asyncio
from fastapi import APIRouter, Depends, status
from fastapi.params import Body, Path
from sqlalchemy.orm import Session
from controllers.taxes import TaxesController
from dependencies.db_dependencies import get_db

from schemas.TaxesSchema import TaxesCreateSchema, TaxesSchema

router = APIRouter()

# get by id
@router.get("/taxes/{tax_id}", response_model=TaxesSchema)
async def get_tax_by_id(tax_id: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TaxesController.get, db, tax_id)

# get all
@router.get("/taxes", response_model=list[TaxesSchema])
async def get_all_taxes(db: Session = Depends(get_db)):
    return await asyncio.to_thread(TaxesController.getAll, db)

# get by CodeTaxe
@router.get("/taxes/code/{CodeTaxe}", response_model=TaxesSchema)
async def get_tax_by_code(CodeTaxe: str = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TaxesController.getByCodeTaxe, db, CodeTaxe)

# create
@router.post("/taxes", response_model=TaxesSchema, status_code=status.HTTP_201_CREATED)
async def create_tax(CodeTaxe: str = Body(...), LibelleTaxe: str = Body(...), TauxTaxe: float = Body(...), db: Session = Depends(get_db)):
    tax = TaxesCreateSchema(CodeTaxe=CodeTaxe, LibelleTaxe=LibelleTaxe, TauxTaxe=TauxTaxe)
    return await asyncio.to_thread(TaxesController.create, db, tax)

@router.put("/taxes/{IDTaxes}/libelle", response_model=TaxesSchema)
async def update_libelle_taxe(IDTaxes: int = Path(...), LibelleTaxe: str = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TaxesController.updateLibelleTaxe, db, IDTaxes, LibelleTaxe)

@router.put("/taxes/{IDTaxes}/taux", response_model=TaxesSchema)
async def update_taux_taxe(IDTaxes: int = Path(...), TauxTaxe: float = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TaxesController.updateTauxTaxe, db, IDTaxes, TauxTaxe)

@router.put("/taxes/{IDTaxes}/code", response_model=TaxesSchema)
async def update_code_taxe(IDTaxes: int = Path(...), CodeTaxe: str = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TaxesController.updateCodeTaxe, db, IDTaxes, CodeTaxe)

@router.delete("/taxes/{IDTaxes}")
async def delete_taxe(IDTaxes: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TaxesController.delete, db, IDTaxes)