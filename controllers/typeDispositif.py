from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from schemas.TypeDispositif import TypeDispositifSchema
from models.typeDispositif import TypeDispositif

class TypeDispositifController:

    # get by id
    @classmethod
    def get(cls, db: Session, type_dispositif_id: int) -> TypeDispositifSchema:
        # if type_dispositif does not exist, throw an error
        try:
            type_dispositif = TypeDispositif.get(db, type_dispositif_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
        if not type_dispositif:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="TypeDispositif not found")
        return type_dispositif
    
    # get all
    @classmethod
    def getAll(cls, db: Session) -> list[TypeDispositifSchema]:
        try:
            return TypeDispositif.getAll(db)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
    
    # create
    @classmethod
    def create(cls, db: Session, type_dispositif: TypeDispositifSchema) -> TypeDispositifSchema:
        try:
            # check if CodeTypeEnseigne is unique
            if TypeDispositif.getByCode(db, type_dispositif.CodeTypeDispositif):
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="CodeTypeDispositif already exists")
            type_dispositif = TypeDispositif.create(db, type_dispositif)
            return type_dispositif
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
        
    # delete
    @classmethod
    def delete(cls, db: Session, type_dispositif_id: int):
        try:
            # check if type_dispositif exists
            type_dispositif = TypeDispositif.get(db, type_dispositif_id)
            if not type_dispositif:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TypeDispositif not found")
            # delete type_dispositif
            type_dispositif = TypeDispositif.delete(db, type_dispositif_id)
            return type_dispositif
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
    
    # update
    @classmethod
    def update(cls, db: Session, type_dispositif_id: int, libelleType: str) -> TypeDispositifSchema:
        try:
            # check if type_dispositif exists
            type_dispositif = TypeDispositif.get(db, type_dispositif_id)
            if not type_dispositif:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TypeDispositif not found")
            # update type_dispositif
            type_dispositif = TypeDispositif.updateLibelleTypeDispo(db, type_dispositif_id, libelleType)
            return type_dispositif
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
    