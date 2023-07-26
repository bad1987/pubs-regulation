import asyncio
from fastapi import APIRouter, Depends, status
from fastapi.params import Body, Path, Query
from sqlalchemy.orm import Session
from dependencies.db_dependencies import get_db

from controllers.typePiece import TypePieceController
from schemas.PiecesSchema import TypePieceSchema, TypePieceUpdateSchema, TypePieceCreateSchema

router = APIRouter(
    tags=["TypePiece"],
)

# get by id
@router.get("/typePiece/{IDTypePiece}", response_model=TypePieceSchema, status_code=status.HTTP_200_OK, description="Get typePiece by ID")
async def get_by_ID(IDTypePiece: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TypePieceController.getById, db, IDTypePiece)

# get all
@router.get("/typePiece", response_model=list[TypePieceSchema], status_code=status.HTTP_200_OK, description="Get all typePieces")
async def get_all(db: Session = Depends(get_db)):
    return await asyncio.to_thread(TypePieceController.getAll, db)

# create
@router.post("/typePiece", response_model=TypePieceSchema, status_code=status.HTTP_201_CREATED, description="Create typePiece")
async def create(type_piece: TypePieceCreateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TypePieceController.create, db, type_piece)

# update
@router.put("/typePiece/{IDTypePiece}", response_model=TypePieceSchema, status_code=status.HTTP_200_OK, description="Update typePiece")
async def update(IDTypePiece: int = Path(...), type_piece: TypePieceUpdateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TypePieceController.update, db, IDTypePiece, type_piece)

# delete
@router.delete("/typePiece/{IDTypePiece}", status_code=status.HTTP_204_NO_CONTENT, description="Delete typePiece")
async def delete(IDTypePiece: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TypePieceController.delete, db, IDTypePiece)