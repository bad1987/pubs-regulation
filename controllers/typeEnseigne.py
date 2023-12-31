
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from schemas.TypeEnseigne import TypeEnseigneCreateSchema, TypeEnseigneSchema
from models.typeEnseigne import TypeEnseigne

class TypeEnseigneController:
    # get by id
    @classmethod
    def get(cls, db: Session, type_enseigne_id: int) -> TypeEnseigneSchema:
        # if type_enseigne does not exist, throw an error
        try:
            type_enseigne = TypeEnseigne.get(db, type_enseigne_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
        if not type_enseigne:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="TypeEnseigne not found")
        return TypeEnseigneSchema.model_validate(type_enseigne)
    
    # get all
    @classmethod
    def getAll(cls, db: Session) -> list[TypeEnseigneSchema]:
        try:
            return [TypeEnseigneSchema.model_validate(type_enseigne) for type_enseigne in TypeEnseigne.getAll(db)]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
    
    # create
    @classmethod
    def create(cls, db: Session, type_enseigne: TypeEnseigneCreateSchema) -> TypeEnseigneSchema:
        # check if CodeTypeEnseigne is unique
        if TypeEnseigne.getByCode(db, type_enseigne.CodeTypeEnseigne):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="CodeTypeEnseigne already exists")
        try:
            type_enseigne = TypeEnseigne.create(db, type_enseigne)
            return TypeEnseigneSchema.model_validate(type_enseigne)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
        
    # delete
    @classmethod
    def delete(cls, db: Session, type_enseigne_id: int):
        # check if type_enseigne exists
        type_enseigne = TypeEnseigne.get(db, type_enseigne_id)
        if not type_enseigne:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TypeEnseigne not found")
        try:
            # delete type_enseigne
            type_enseigne = TypeEnseigne.delete(db, type_enseigne_id)
            return TypeEnseigneSchema.model_validate(type_enseigne)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
    
    # update
    @classmethod
    def update(cls, db: Session, type_enseigne_id: int, libelleType: str) -> TypeEnseigneSchema:
        # check if type_enseigne exists
        type_enseigne = TypeEnseigne.get(db, type_enseigne_id)
        if not type_enseigne:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TypeEnseigne not found")
        try:
            # update type_enseigne
            type_enseigne = TypeEnseigne.updateLibelleTypeEnseigne(db, type_enseigne_id, libelleType)
            return TypeEnseigneSchema.model_validate(type_enseigne)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
    