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
        return TypeDispositifSchema.from_orm(type_dispositif)
    
    # get all
    @classmethod
    def getAll(cls, db: Session) -> list[TypeDispositifSchema]:
        try:
            return [TypeDispositifSchema.from_orm(type_dispositif) for type_dispositif in TypeDispositif.getAll(db)]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
    
    # create
    @classmethod
    def create(cls, db: Session, type_dispositif: TypeDispositifSchema) -> TypeDispositifSchema:
        # check if CodeTypeEnseigne is unique
        if TypeDispositif.getByCode(db, type_dispositif.CodeTypeDispositif):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="CodeTypeDispositif already exists")
        try:
            type_dispositif = TypeDispositif.create(db, type_dispositif)
            return TypeDispositifSchema.from_orm(type_dispositif)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
        
    # delete
    @classmethod
    def delete(cls, db: Session, type_dispositif_id: int):
        # check if type_dispositif exists
        type_dispositif = TypeDispositif.get(db, type_dispositif_id)
        if not type_dispositif:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TypeDispositif not found")
        try:
            # delete type_dispositif
            type_dispositif = TypeDispositif.delete(db, type_dispositif_id)
            return type_dispositif
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
    
    # update libelleType
    @classmethod
    def updateLibelleTypeDispo(cls, db: Session, type_dispositif_id: int, libelleType: str) -> TypeDispositifSchema:
        # check if type_dispositif exists
        type_dispositif = TypeDispositif.get(db, type_dispositif_id)
        if not type_dispositif:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TypeDispositif not found")
        try:
            # update type_dispositif
            type_dispositif = TypeDispositif.updateLibelleTypeDispo(db, type_dispositif_id, libelleType)
            return TypeDispositifSchema.from_orm(type_dispositif)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
    
    # update
    @classmethod
    def update(cls, db: Session, update_type_dispositif: TypeDispositifSchema) -> TypeDispositifSchema:
        # check if type_dispositif exists
        type_dispositif = TypeDispositif.get(db, type_dispositif.IDTypeDispositif)
        if not type_dispositif:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TypeDispositif not found")
        try:
            # update type_dispositif
            update_data = update_type_dispositif.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(type_dispositif, key, value)
            type_dispositif = TypeDispositif.update(db, type_dispositif)
            return TypeDispositifSchema.from_orm(type_dispositif)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))