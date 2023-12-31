from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.reglements import Reglement
from models.docentete import DocEntete
from schemas.ReglementSchema import ReglementSchema, ReglementCreateSchema

class ReglementController:
    # get
    @classmethod
    def get(cls, db: Session, IDReglement: int) -> ReglementSchema:
        try:
            reglement = Reglement.get(db, IDReglement)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not reglement:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reglement not found")
        return ReglementSchema.model_validate(reglement)
    
    # get by NumReglt
    @classmethod
    def getByNumReglt(cls, db: Session, NumReglt: str) -> ReglementSchema:
        try:
            reglement = Reglement.getByNumReglt(db, NumReglt)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not reglement:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reglement not found")
        return ReglementSchema.model_validate(reglement)

    # get all
    @classmethod
    def getAll(cls, db: Session) -> list[ReglementSchema]:
        try:
            return [ReglementSchema.model_validate(reglement) for reglement in Reglement.get_all(db)]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # create
    @classmethod
    def create(cls, db: Session, reglement: ReglementCreateSchema) -> ReglementSchema:
        # check if IDDocEntete exists
        doc_entete = DocEntete.get(db, reglement.IDDocEntete)
        if not doc_entete:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid foreign key {reglement.IDDocEntete}")
        try:
            reglement = Reglement(**reglement.model_dump())
            reglement.doc_entete = doc_entete
            reglement = Reglement.create(db, reglement)
            return ReglementSchema.model_validate(reglement)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # update NumReglt
    @classmethod
    def updateNumReglt(cls, db: Session, IDReglement: int, NumReglt: int) -> ReglementSchema:
        try:
            reglement = Reglement.get(db, IDReglement)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not reglement:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reglement not found")
        try:
            reglement = Reglement.updateNumReglt(db, IDReglement, NumReglt)
            return ReglementSchema.model_validate(reglement)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # update
    @classmethod
    def update(cls, db: Session, IDReglement: int, updateReglement: ReglementCreateSchema) -> ReglementSchema:
        try:
            reglement = Reglement.get(db, IDReglement)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not reglement:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reglement not found")
        try:
            update_data = updateReglement.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(reglement, key, value)
            reglement = Reglement.update(db, reglement)
            return ReglementSchema.model_validate(reglement)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # update DateReglt
    @classmethod
    def updateDateReglt(cls, db: Session, IDReglement: int, DateReglt: datetime) -> ReglementSchema:
        try:
            reglement = Reglement.get(db, IDReglement)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not reglement:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reglement not found")
        try:
            reglement = Reglement.updateDateReglt(db, IDReglement, DateReglt)
            return ReglementSchema.model_validate(reglement)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # update MontantRegle
    @classmethod
    def updateMontantRegle(cls, db: Session, IDReglement: int, MontantRegle: int) -> ReglementSchema:
        try:
            reglement = Reglement.get(db, IDReglement)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not reglement:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reglement not found")
        try:
            reglement = Reglement.updateMontantRegle(db, IDReglement, MontantRegle)
            return ReglementSchema.model_validate(reglement)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # update SoldeRglt
    @classmethod
    def updateSoldeRglt(cls, db: Session, IDReglement: int, SoldeRglt: float) -> ReglementSchema:
        try:
            reglement = Reglement.get(db, IDReglement)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not reglement:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reglement not found")
        try:
            reglement = Reglement.updateSoldeRglt(db, IDReglement, SoldeRglt)
            return ReglementSchema.model_validate(reglement)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # update StatutRglt
    @classmethod
    def updateStatutRglt(cls, db: Session, IDReglement: int, StatutRglt: str) -> ReglementSchema:
        try:
            reglement = Reglement.get(db, IDReglement)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not reglement:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reglement not found")
        try:
            reglement = Reglement.updateStatutRglt(db, IDReglement, StatutRglt)
            return ReglementSchema.model_validate(reglement)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # update ModeRglt
    @classmethod
    def updateModeRglt(cls, db: Session, IDReglement: int, ModeRglt: str) -> ReglementSchema:
        try:
            reglement = Reglement.get(db, IDReglement)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not reglement:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reglement not found")
        try:
            reglement = Reglement.updateModeRglt(db, IDReglement, ModeRglt)
            return ReglementSchema.model_validate(reglement)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDReglement: int) -> bool:
        try:
            reglement = Reglement.get(db, IDReglement)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not reglement:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reglement not found")
        try:
            return Reglement.delete(db, IDReglement)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))