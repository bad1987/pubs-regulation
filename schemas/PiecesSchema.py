from datetime import datetime
from typing import Optional
from pydantic import BaseModel, validator

from schemas.ReglementSchema import ReglementSchema

class TypePieceSchema(BaseModel):
    IDTypePiece: int
    CodeTypePiece: str
    LibelleTypePiece: str

    class Config:
        orm_mode = True
        from_attributes = True

class TypePieceCreateSchema(BaseModel):
    CodeTypePiece: str
    LibelleTypePiece: str

class TypePieceUpdateSchema(BaseModel):
    IDTypePiece: int
    CodeTypePiece: str
    LibelleTypePiece: str

class PiecesSchema(BaseModel):
    IDPiece: int
    NumPiece: str
    DateEmmission: datetime
    IDTypePiece: int
    IDReglement: int
    tpye_piece: TypePieceSchema
    reglement: ReglementSchema

    class Config:
        orm_mode = True
        from_attributes = True
    
    @validator('DateEmmission', pre=True)
    def parse_date(cls, value):
        if isinstance(value, datetime):
            # Parse the string value using the desired format
            return value.isoformat()
        return value

class PiecesCreateSchema(BaseModel):
    NumPiece: str
    DateEmmission: datetime
    IDReglement: int
    IDTypePiece: int

    @validator('DateEmmission', pre=True)
    def parse_date(cls, value):
        if isinstance(value, datetime):
            # Parse the string value using the desired format
            return value.isoformat()
        return value

class PiecesUpdateSchema(BaseModel):
    IDPiece: int
    NumPiece: str
    DateEmmission: datetime
    IDReglement: int
    IDTypePiece: int

    @validator('DateEmmission', pre=True)
    def parse_date(cls, value):
        if isinstance(value, datetime):
            # Parse the string value using the desired format
            return value.isoformat()
        return value