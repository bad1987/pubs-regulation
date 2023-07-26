import asyncio
from fastapi import APIRouter, Depends, status
from fastapi.params import Body, Path, Query
from sqlalchemy.orm import Session
from dependencies.db_dependencies import get_db

from controllers.panneauAffich import PanneauAffichController
from schemas.PanneauAffich import PanneauAffichSchema, PanneauAffichUpdateSchema, PanneauAffichCreateSchema

router = APIRouter(
    tags=["PanneauAffich"],
)

# get by CodePanneau
@router.get("/panneauAffich/code", response_model=PanneauAffichSchema, status_code=status.HTTP_200_OK, description="Get panneauAffich by CodePanneau")
async def get_by_code(CodePanneau: str = Query(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(PanneauAffichController.get_by_code, db, CodePanneau)

# get by ID
@router.get("/panneauAffich/{IDPanneauAffich}", response_model=PanneauAffichSchema, status_code=status.HTTP_200_OK, description="Get panneauAffich by ID")
async def get_by_ID(IDPanneauAffich: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(PanneauAffichController.get, db, IDPanneauAffich)

# get all
@router.get("/panneauAffich", response_model=list[PanneauAffichSchema], status_code=status.HTTP_200_OK, description="Get all panneauAffich")
async def get_all(db: Session = Depends(get_db)):
    return await asyncio.to_thread(PanneauAffichController.get_all, db)

# create
@router.post("/panneauAffich", response_model=PanneauAffichSchema, status_code=status.HTTP_201_CREATED, description="Create panneauAffich")
async def create(panneauAffich: PanneauAffichCreateSchema, db: Session = Depends(get_db)):
    return await asyncio.to_thread(PanneauAffichController.create, db, panneauAffich)

# update
@router.put("/panneauAffich/{IDPanneauAffich}", response_model=PanneauAffichSchema, status_code=status.HTTP_200_OK, description="Update panneauAffich")
async def update(IDPanneauAffich: int = Path(...), panneauAffich: PanneauAffichUpdateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(PanneauAffichController.update, db, panneauAffich)

# delete
@router.delete("/panneauAffich/{IDPanneauAffich}", status_code=status.HTTP_204_NO_CONTENT, description="Delete panneauAffich")
async def delete(IDPanneauAffich: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(PanneauAffichController.delete, db, IDPanneauAffich)