# the controller that implement all actions for emplacementAffichage model

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.emplacementAffichage import EmplacementAffichage
from models.quartierAffichage import QuartierAffichage
from schemas.EmplacementAffichageSchema import EmplacementAffichageSchema, EmplacementAffichageUpdateSchema, EmplacementAffichageCreateSchema

class EmplacementAffichageController:
    # get
    @classmethod
    def get(cls, db: Session, IDEmplacementAffichage: int) -> EmplacementAffichageSchema:
        try:
            emplacementAffichage = EmplacementAffichage.get(db, IDEmplacementAffichage)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not emplacementAffichage:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EmplacementAffichage not found")
        return EmplacementAffichageSchema.model_validate(emplacementAffichage)
    
    # get by CodeEmplacement
    @classmethod
    def get_by_code(cls, db: Session, CodeEmplacement: str) -> EmplacementAffichageSchema:
        try:
            emplacementAffichage = EmplacementAffichage.get_by_code(db, CodeEmplacement)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not emplacementAffichage:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EmplacementAffichage not found")
        return EmplacementAffichageSchema.model_validate(emplacementAffichage)
    
    # get all by IDQuartierAffichage
    @classmethod
    def get_all_by_IDQuartierAffichage(cls, db: Session, IDQuartierAffichage: int) -> list[EmplacementAffichageSchema]:
        try:
            emplacementAffichages = EmplacementAffichage.get_all_by_id_quartier(db, IDQuartierAffichage)
            return [EmplacementAffichageSchema.model_validate(emplacementAffichage) for emplacementAffichage in emplacementAffichages]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # get all
    @classmethod
    def get_all(cls, db: Session) -> list[EmplacementAffichageSchema]:
        try:
            emplacementAffichages = EmplacementAffichage.get_all(db)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not emplacementAffichages:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EmplacementAffichages not found")
        return [EmplacementAffichageSchema.model_validate(emplacementAffichage) for emplacementAffichage in emplacementAffichages]
    
    # create
    @classmethod
    def create(cls, db: Session, emplacementAffichage: EmplacementAffichageCreateSchema):
        # check if codeEmplacement is unique
        if EmplacementAffichage.get_by_code(db, emplacementAffichage.CodeEmplacement):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="CodeEmplacement already exists")
        # check if the foreign key IDQuartierAffichage is valid
        quartierAffichage = QuartierAffichage.get(db, emplacementAffichage.IDQuartierAffichage)
        if not quartierAffichage:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid foreign key IDQuartierAffichage: {emplacementAffichage.IDQuartierAffichage}")
        try:
            emplacementAffichage = EmplacementAffichage(**emplacementAffichage.model_dump())
            emplacementAffichage.quartier = quartierAffichage
            emplacementAffichage = EmplacementAffichage.create(db, emplacementAffichage)
            return EmplacementAffichageSchema.model_validate(emplacementAffichage)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # update
    @classmethod
    def update(cls, db: Session, emplacementAffichage: EmplacementAffichageUpdateSchema) -> EmplacementAffichageSchema:
        try:
            emplacementAffichage_to_update = EmplacementAffichage.get(db, emplacementAffichage.IDEmplacementAffichage)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not emplacementAffichage_to_update:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EmplacementAffichage not found")
        try:
            update_data = emplacementAffichage.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(emplacementAffichage_to_update, key, value)
            emplacementAffichage_to_update = EmplacementAffichage.update(db, emplacementAffichage_to_update)
            return EmplacementAffichageSchema.model_validate(emplacementAffichage_to_update)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # delete
    @classmethod
    def delete(cls, db: Session, IDEmplacementAffichage: int) -> bool:
        try:
            emplacementAffichage = EmplacementAffichage.get(db, IDEmplacementAffichage)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not emplacementAffichage:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EmplacementAffichage not found")
        try:
            return EmplacementAffichage.delete(db, IDEmplacementAffichage)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        