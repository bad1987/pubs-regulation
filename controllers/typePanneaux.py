from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.typePanneau import TypePanneau
from schemas.TypePanneaux import TypePanneauCreateSchema, TypePanneauSchema
# a controller class to handle all actions on the TypePanneau model

class TypePanneauController:
    # get by id
    @classmethod
    def get(cls, db: Session, type_panneau_id: int) -> TypePanneauSchema:
        # if type_panneau does not exist, throw an error
        try:
            type_panneau = TypePanneau.get(db, type_panneau_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
        if not type_panneau:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="TypePanneau not found")
        return type_panneau
    
    # get all
    @classmethod
    def getAll(cls, db: Session) -> list[TypePanneauSchema]:
        try:
            return TypePanneau.getAll(db)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
        
    # create
    @classmethod
    def create(cls, db: Session, type_panneau: TypePanneauCreateSchema) -> TypePanneauSchema:
        # check if CodeTypePanneau is unique
        if TypePanneau.getByCode(db, type_panneau.CodeTypePanneau):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="CodeTypePanneau already exists")
        try:
            type_panneau = TypePanneau.create(db, type_panneau)
            return type_panneau
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
        
    # delete
    @classmethod
    def delete(cls, db: Session, type_panneau_id: int) -> bool:
        # check if type_panneau exists
        type_panneau = TypePanneau.get(db, type_panneau_id)
        if not type_panneau:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TypePanneau not found")
        try:
            # delete type_panneau
            type_panneau = TypePanneau.delete(db, type_panneau_id)
            return type_panneau
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
    
    # update
    @classmethod
    def update(cls, db: Session, type_panneau_id: int, libelleType: str) -> TypePanneauSchema:
        # check if type_panneau exists
        type_panneau = TypePanneau.get(db, type_panneau_id)
        if not type_panneau:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TypePanneau not found")
        try:
            # update type_panneau
            type_panneau = TypePanneau.updateLibelleType(db, type_panneau_id, libelleType)
            return type_panneau
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
    