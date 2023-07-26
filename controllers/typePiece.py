from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.pieces import TypePiece
from schemas.PiecesSchema import TypePieceSchema, TypePieceUpdateSchema, TypePieceCreateSchema

class TypePieceController:
    # get by id
    @classmethod
    def getById(cls, db: Session, IDTypePiece: int) -> TypePieceSchema:
        try:
            type_piece = TypePiece.get(db, IDTypePiece)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not type_piece:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TypePiece not found")
        return TypePieceSchema.from_orm(type_piece)
    
    # get all
    @classmethod
    def getAll(cls, db: Session) -> list[TypePieceSchema]:
        try:
            type_pieces = TypePiece.getAll(db)
            return [TypePieceSchema.from_orm(type_piece) for type_piece in type_pieces]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # create
    @classmethod
    def create(cls, db: Session, type_piece: TypePieceCreateSchema) -> TypePieceSchema:
        try:
            type_piece = TypePiece(**type_piece.dict())
            type_piece = TypePiece.create(db, type_piece)
            return TypePieceSchema.from_orm(type_piece) 
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # update
    @classmethod
    def update(cls, db: Session, IDTypePiece: int, update_type_piece: TypePieceUpdateSchema) -> TypePieceSchema:
        try:
            type_piece = TypePiece.get(db, IDTypePiece)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not type_piece:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TypePiece not found")
        try:
            update_data = update_type_piece.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(type_piece, key, value)
            type_piece = TypePiece.update(db, type_piece)
            return TypePieceSchema.from_orm(type_piece) 
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDTypePiece: int) -> bool:
        try:
            type_piece = TypePiece.get(db, IDTypePiece)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not type_piece:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TypePiece not found")
        try:
            return TypePiece.delete(db, type_piece)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        