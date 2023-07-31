import asyncio
from fastapi import APIRouter, Depends, status
from fastapi.params import Body, Path, Query
from sqlalchemy.orm import Session
from dependencies.db_dependencies import get_db

from controllers.docligne import DocLigneController
from schemas.DocLigneSchema import DocLigneSchema, DocLigneUpdateSchema, DocLigneCreateSchema

router = APIRouter(
    tags=["DocLigne"],
)

@router.get("/docligne", response_model=list[DocLigneSchema], status_code=status.HTTP_200_OK, description="Get all docligne")
async def get_all(db: Session = Depends(get_db)):
    return await asyncio.to_thread(DocLigneController.getAll, db)

@router.post("/docligne", response_model=DocLigneSchema, status_code=status.HTTP_201_CREATED, description="Create docligne")
async def create(docligne: DocLigneCreateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(DocLigneController.create, db, docligne)

@router.put("/docligne/{IDDocLigne}", response_model=DocLigneSchema, status_code=status.HTTP_200_OK, description="Update docligne")
async def update(IDDocLigne: int = Path(...), docligne: DocLigneUpdateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(DocLigneController.update, db, docligne)

@router.delete("/docligne/{IDDocLigne}", status_code=status.HTTP_204_NO_CONTENT, description="Delete docligne")
async def delete(IDDocLigne: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(DocLigneController.delete, db, IDDocLigne)
