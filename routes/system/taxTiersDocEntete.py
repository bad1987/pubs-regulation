import asyncio
from fastapi import APIRouter, Depends, status
from fastapi.params import Body, Path, Query
from sqlalchemy.orm import Session
from dependencies.db_dependencies import get_db

from controllers.taxTiersDocEntete import TaxTiersDocEnteteController
from schemas.TaxTiersDocEnteteSchema import TaxTiersDocEnteteSchema, TaxTiersDocEnteteUpdateSchema, TaxTiersDocEnteteCreateSchema

router = APIRouter(
    tags=["TaxTiersDocEntete"],
)

# get by IDTiers
@router.get("/taxTiersDocEntete/tiers", response_model=TaxTiersDocEnteteSchema, status_code=status.HTTP_200_OK, description="Get taxTiersDocEntete by IDTiers")
async def get_by_IDTiers(IDTiers: int = Query(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TaxTiersDocEnteteController.getByIDTiers, db, IDTiers)

# get by IDTaxes
@router.get("/taxTiersDocEntete/taxe", response_model=TaxTiersDocEnteteSchema, status_code=status.HTTP_200_OK, description="Get taxTiersDocEntete by IDTaxes")
async def get_by_IDTaxes(IDTaxes: int = Query(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TaxTiersDocEnteteController.getByIDTaxes, db, IDTaxes)

# get all
@router.get("/taxTiersDocEntete", response_model=list[TaxTiersDocEnteteSchema], status_code=status.HTTP_200_OK, description="Get all taxTiersDocEntete")
async def get_all(db: Session = Depends(get_db)):
    return await asyncio.to_thread(TaxTiersDocEnteteController.getAll, db)

# create
@router.post("/taxTiersDocEntete", response_model=TaxTiersDocEnteteSchema, status_code=status.HTTP_201_CREATED, description="Create taxTiersDocEntete")
async def create(taxTiersDocEntete: TaxTiersDocEnteteCreateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TaxTiersDocEnteteController.create, db, taxTiersDocEntete)

# update
@router.put("/taxTiersDocEntete/{IDTiersDocEntete}", response_model=TaxTiersDocEnteteSchema, status_code=status.HTTP_200_OK, description="Update taxTiersDocEntete")
async def update(IDTiersDocEntete: int = Path(...), taxTiersDocEntete: TaxTiersDocEnteteUpdateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TaxTiersDocEnteteController.update, db, taxTiersDocEntete)

# delete
@router.delete("/taxTiersDocEntete/{IDTiersDocEntete}", status_code=status.HTTP_204_NO_CONTENT, description="Delete taxTiersDocEntete")
async def delete(IDTiersDocEntete: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TaxTiersDocEnteteController.delete, db, IDTiersDocEntete)
