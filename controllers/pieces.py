from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.pieces import Piece, TypePiece
from models.reglements import Reglement
from schemas.PiecesSchema import PiecesSchema, PiecesUpdateSchema, PiecesCreateSchema

class PiecesController:
    # get
    @classmethod
    def get(cls, db: Session, IDPiece: int) -> PiecesSchema:
        try:
            piece = Piece.get(db, IDPiece)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not piece:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Piece not found")
        return PiecesSchema.from_orm(piece)
    
    # get by NumPiece
    @classmethod
    def getByNum(cls, db: Session, NumPiece: str) -> PiecesSchema:
        try:
            piece = Piece.getByNum(db, NumPiece)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not piece:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Piece not found")
        return PiecesSchema.from_orm(piece)
    
    # get all
    @classmethod
    def getAll(cls, db: Session) -> list[PiecesSchema]:
        try:
            pieces = Piece.getAll(db)
            return [PiecesSchema.from_orm(piece) for piece in pieces]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # create
    @classmethod
    def create(cls, db: Session, piece: PiecesCreateSchema) -> PiecesSchema:
        # check if NumPiece is unique
        if Piece.getByNum(db, piece.NumPiece):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="CodePiece already exists")
        # check if IDReglement is valid
        reglement = Reglement.get(db, piece.IDReglement)
        if not reglement:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid foreign key IDReglement: {piece.IDReglement}")
        # check if IDTypePiece is valid
        type_piece = TypePiece.get(db, piece.IDTypePiece)
        if not type_piece:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid foreign key IDTypePiece: {piece.IDTypePiece}")
        try:
            piece = Piece(**piece.dict())
            piece.reglement = reglement
            piece.type_piece = type_piece
            piece = Piece.create(db, piece)
            return PiecesSchema.from_orm(piece) 
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # update
    @classmethod
    def update(cls, db: Session, updatePiece: PiecesUpdateSchema) -> PiecesSchema:
        try:
            piece = Piece.get(db, updatePiece.IDPiece)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not piece:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Piece not found")
        try:
            update_data = updatePiece.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(piece, key, value)
            piece = Piece.update(db, piece)
            return PiecesSchema.from_orm(piece)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDPiece: int) -> bool:
        try:
            piece = Piece.get(db, IDPiece)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not piece:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Piece not found")
        try:
            return Piece.delete(db, IDPiece)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))