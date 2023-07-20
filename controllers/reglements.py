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
        return ReglementSchema.from_orm(reglement)
    
    # get all
    @classmethod
    def getAll(cls, db: Session) -> list[ReglementSchema]:
        try:
            return [ReglementSchema.from_orm(reglement) for reglement in Reglement.getAll(db)]
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
            reglement = Reglement(**reglement.dict())
            reglement.doc_entete = doc_entete
            reglement = Reglement.create(db, reglement)
            return ReglementSchema.from_orm(reglement)
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
            return ReglementSchema.from_orm(reglement)
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
            return ReglementSchema.from_orm(reglement)
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
            return ReglementSchema.from_orm(reglement)
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
            return ReglementSchema.from_orm(reglement)
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
            return ReglementSchema.from_orm(reglement)
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
            return ReglementSchema.from_orm(reglement)
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