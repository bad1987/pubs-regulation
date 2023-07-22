import asyncio
from fastapi import APIRouter, Depends, status
from fastapi.params import Body, Path, Query
from sqlalchemy.orm import Session
from dependencies.db_dependencies import get_db

from controllers.reglements import ReglementController
from schemas.ReglementSchema import ReglementSchema, ReglementCreateSchema, ReglementUpdateSchema

router = APIRouter(
    tags=["Reglements"],
)

@router.get("/reglements/numreglement", response_model=ReglementSchema, status_code=status.HTTP_200_OK)
async def get_reglements_by_numreglement(NumReglt: str = Query(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(ReglementController.getByNumReglt, db, NumReglt)

@router.get("/reglements/{IDReglement}", response_model=ReglementSchema, status_code=status.HTTP_200_OK)
async def get_reglements_by_id(IDReglement: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(ReglementController.get, db, IDReglement)

@router.get("/reglements", response_model=list[ReglementSchema], status_code=status.HTTP_200_OK)
async def get_all_reglements(db: Session = Depends(get_db)):
    return await asyncio.to_thread(ReglementController.getAll, db)

@router.post("/reglements", response_model=ReglementSchema, status_code=status.HTTP_201_CREATED)
async def create_reglements(reglement: ReglementCreateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(ReglementController.create, db, reglement)

@router.put("/reglements/{IDReglement}", response_model=ReglementSchema, status_code=status.HTTP_200_OK)
async def update_reglements(IDReglement: int = Path(...), reglement: ReglementUpdateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(ReglementController.update, db, IDReglement, reglement)

@router.delete("/reglements/{IDReglement}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_reglements(IDReglement: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(ReglementController.delete, db, IDReglement)
