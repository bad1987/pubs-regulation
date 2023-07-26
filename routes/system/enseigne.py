import asyncio
from fastapi import APIRouter, Depends, status
from fastapi.params import Body, Path, Query
from sqlalchemy.orm import Session
from dependencies.db_dependencies import get_db

from controllers.enseigne import EnseigneController
from schemas.EnseigneSchema import EnseigneSchema, EnseigneUpdateSchema, EnseigneCreateSchema

router = APIRouter(
    tags=["Enseigne"],
)

# get by CodeEnseigne
@router.get("/enseigne/code", response_model=EnseigneSchema, status_code=status.HTTP_200_OK, description="Get enseigne by CodeEnseigne")
async def get_by_code(CodeEnseigne: str = Query(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(EnseigneController.get_by_code, db, CodeEnseigne)

# get by ID
@router.get("/enseigne/{IDEnseigne}", response_model=EnseigneSchema, status_code=status.HTTP_200_OK, description="Get enseigne by ID")
async def get_by_ID(IDEnseigne: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(EnseigneController.get, db, IDEnseigne)

# get all
@router.get("/enseigne", response_model=list[EnseigneSchema], status_code=status.HTTP_200_OK, description="Get all enseigne")
async def get_all(db: Session = Depends(get_db)):
    return await asyncio.to_thread(EnseigneController.get_all, db)

# create
@router.post("/enseigne", response_model=EnseigneSchema, status_code=status.HTTP_201_CREATED, description="Create enseigne")
async def create(enseigne: EnseigneCreateSchema, db: Session = Depends(get_db)):
    return await asyncio.to_thread(EnseigneController.create, db, enseigne)

# update
@router.put("/enseigne/{IDEnseigne}", response_model=EnseigneSchema, status_code=status.HTTP_200_OK, description="Update enseigne")
async def update(IDEnseigne: int = Path(...), enseigne: EnseigneUpdateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(EnseigneController.update, db, enseigne)

# delete
@router.delete("/enseigne/{IDEnseigne}", status_code=status.HTTP_204_NO_CONTENT, description="Delete enseigne")
async def delete(IDEnseigne: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(EnseigneController.delete, db, IDEnseigne)
