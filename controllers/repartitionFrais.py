from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.repartitionFrais import RepartitionFrais
from schemas.RepartitionFraisSchema import RepartitionFraisSchema, RepartitionFraisCreateSchema

class RepartitionFraisController:
    # get
    @classmethod
    def get(cls, db: Session, IDRepartitionFrais: int) -> RepartitionFraisSchema:
        try:
            rep_frais = RepartitionFrais.get(db, IDRepartitionFrais)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not rep_frais:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RepartitionFrais not found")
        return RepartitionFraisSchema.from_orm(rep_frais)
    
    # get all
    @classmethod
    def getAll(cls, db: Session) -> list[RepartitionFraisSchema]:
        try:
            return [RepartitionFraisSchema.from_orm(rep_frais) for rep_frais in RepartitionFrais.get_all(db)]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # create
    @classmethod
    def create(cls, db: Session, rep_frais: RepartitionFraisCreateSchema) -> RepartitionFraisSchema:
        try:
            rep_frais = RepartitionFrais.create(db, RepartitionFrais(**rep_frais.dict()))
            return RepartitionFraisSchema.from_orm(rep_frais)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # update IntervenantEntite
    @classmethod
    def updateIntervenantEntite(cls, db: Session, IDRepartitionFrais: int, IntervenantEntite: str) -> RepartitionFraisSchema:
        try:
            rep_frais = RepartitionFrais.get(db, IDRepartitionFrais)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not rep_frais:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RepartitionFrais not found")
        try:
            rep_frais.IntervenantEntite = IntervenantEntite
            rep_frais = RepartitionFrais.update(db, rep_frais)
            return RepartitionFraisSchema.from_orm(rep_frais)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # update TauxRepartition
    @classmethod
    def updateTauxRepartition(cls, db: Session, IDRepartitionFrais: int, TauxRepartition: float) -> RepartitionFraisSchema:
        try:
            rep_frais = RepartitionFrais.get(db, IDRepartitionFrais)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not rep_frais:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RepartitionFrais not found")
        try:
            rep_frais.TauxRepartition = TauxRepartition
            rep_frais = RepartitionFrais.update(db, rep_frais)
            return RepartitionFraisSchema.from_orm(rep_frais)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # update AnneeRepart
    @classmethod
    def updateAnneeRepart(cls, db: Session, IDRepartitionFrais: int, AnneeRepart: datetime) -> RepartitionFraisSchema:
        try:
            rep_frais = RepartitionFrais.get(db, IDRepartitionFrais)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not rep_frais:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RepartitionFrais not found")
        try:
            rep_frais.AnneeRepart = AnneeRepart
            rep_frais = RepartitionFrais.update(db, rep_frais)
            return RepartitionFraisSchema.from_orm(rep_frais)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # delete
    @classmethod
    def delete(cls, db: Session, IDRepartitionFrais: int) -> bool:
        try:
            rep_frais = RepartitionFrais.get(db, IDRepartitionFrais)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not rep_frais:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RepartitionFrais not found")
        try:
            return RepartitionFrais.delete(db, IDRepartitionFrais)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))