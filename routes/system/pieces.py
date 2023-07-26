import asyncio
from fastapi import APIRouter, Depends, status
from fastapi.params import Body, Path, Query
from sqlalchemy.orm import Session
from dependencies.db_dependencies import get_db

from controllers.pieces import PiecesController
from schemas.PiecesSchema import PiecesSchema, PiecesUpdateSchema, PiecesCreateSchema

router = APIRouter(
    tags=["Pieces"],
)

# get by NumPiece
@router.get("/pieces/numPiece", response_model=PiecesSchema, status_code=status.HTTP_200_OK, description="Get pieces by NumPiece")
async def get_by_NumPiece(NumPiece: str = Query(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(PiecesController.getByNum, db, NumPiece)

# get by ID
@router.get("/pieces/{IDPieces}", response_model=PiecesSchema, status_code=status.HTTP_200_OK, description="Get pieces by ID")
async def get_by_ID(IDPieces: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(PiecesController.get, db, IDPieces)

# get all
@router.get("/pieces", response_model=list[PiecesSchema], status_code=status.HTTP_200_OK, description="Get all pieces")
async def get_all(db: Session = Depends(get_db)):
    return await asyncio.to_thread(PiecesController.getAll, db)

# create
@router.post("/pieces", response_model=PiecesSchema, status_code=status.HTTP_201_CREATED, description="Create pieces")
async def create(pieces: PiecesCreateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(PiecesController.create, db, pieces)

# update
@router.put("/pieces/{IDPieces}", response_model=PiecesSchema, status_code=status.HTTP_200_OK, description="Update pieces")
async def update(IDPieces: int = Path(...), pieces: PiecesUpdateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(PiecesController.update, db, pieces)

# delete
@router.delete("/pieces/{IDPieces}", status_code=status.HTTP_204_NO_CONTENT, description="Delete pieces")
async def delete(IDPieces: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(PiecesController.delete, db, IDPieces)
