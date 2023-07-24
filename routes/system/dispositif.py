import asyncio
from fastapi import APIRouter, Depends, status
from fastapi.params import Body, Path, Query
from sqlalchemy.orm import Session
from dependencies.db_dependencies import get_db

from controllers.dispositif import DispositifPubController
from schemas.DispositifPubSchema import DispositifPubSchema, DispositifPubUpdateSchema, DispositifPubCreateSchema

router = APIRouter(
    tags=["Dispositif"],
)

@router.get("/dispositif/code", response_model=DispositifPubSchema, status_code=status.HTTP_200_OK, description="Get dispositif by Code")
async def get_by_code(CodeDispositifPub: str = Query(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(DispositifPubController.get_by_code, db, CodeDispositifPub)

@router.get("/dispositif/{IDDispositif}", response_model=DispositifPubSchema, status_code=status.HTTP_200_OK, description="Get dispositif by ID")
async def get_by_ID(IDDispositif: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(DispositifPubController.get, db, IDDispositif)

@router.get("/dispositif", response_model=list[DispositifPubSchema], status_code=status.HTTP_200_OK, description="Get all dispositif")
async def get_all(db: Session = Depends(get_db)):
    return await asyncio.to_thread(DispositifPubController.get_all, db)

@router.post("/dispositif", response_model=DispositifPubSchema, status_code=status.HTTP_201_CREATED, description="Create dispositif")
async def create(dispositif: DispositifPubCreateSchema, db: Session = Depends(get_db)):
    return await asyncio.to_thread(DispositifPubController.create, db, dispositif)

@router.put("/dispositif/{IDDispositif}", response_model=DispositifPubSchema, status_code=status.HTTP_200_OK, description="Update dispositif")
async def update(IDDispositif: int = Path(...), dispositif: DispositifPubUpdateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(DispositifPubController.update, db, dispositif)

@router.delete("/dispositif/{IDDispositif}", status_code=status.HTTP_204_NO_CONTENT, description="Delete dispositif")
async def delete(IDDispositif: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(DispositifPubController.delete, db,IDDispositif)
