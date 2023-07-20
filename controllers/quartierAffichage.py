from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.quartierAffichage import QuartierAffichage
from models.zoneAffichage import ZoneAffichage
from schemas.QuartierAffichageSchema import QuartierAffichageSchema, QuartierAffichageCreateSchema, QuartierAffichageUpdateSchema

class QuartierAffichageController:

    # get
    @classmethod
    def get(cls, db: Session, quartierAffichage_id: int) -> QuartierAffichageSchema:
        try:
            quartierAffichage = QuartierAffichage.get(db, quartierAffichage_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not quartierAffichage:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="QuartierAffichage not found")
        return QuartierAffichageSchema.from_orm(quartierAffichage)
    
    # get all
    @classmethod
    def getAll(cls, db: Session) -> list[QuartierAffichageSchema]:
        try:
            return [QuartierAffichageSchema.from_orm(quartierAffichage) for quartierAffichage in QuartierAffichage.getAll(db)]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # get by NomQuartier
    @classmethod
    def get_by_nom_quartier(cls, db: Session, NomQuartier: str) -> QuartierAffichageSchema:
        try:
            quartierAffichage = QuartierAffichage.get_by_nom_quartier(db, NomQuartier)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not quartierAffichage:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="QuartierAffichage not found")
        return QuartierAffichageSchema.from_orm(quartierAffichage)

    # create
    @classmethod
    def create(cls, db: Session, quartierAffichage: QuartierAffichageCreateSchema) -> QuartierAffichageSchema:
        # check if NomQuartier is unique
        if QuartierAffichage.get_by_nom_quartier(db, quartierAffichage.NomQuartier):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="NomQuartier already exists")
        # check if the foreign key IDZoneAffichage is valid
        zoneAffichage = ZoneAffichage.get(db, quartierAffichage.IDZoneAffichage)
        if not zoneAffichage:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid foreign key {quartierAffichage.IDZoneAffichage}")
        try:
            quartierAffichage = QuartierAffichage(**quartierAffichage.dict())
            quartierAffichage.zone_affichage = zoneAffichage
            quartierAffichage = QuartierAffichage.create(db, quartierAffichage)
            return QuartierAffichageSchema.from_orm(quartierAffichage)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # update
    @classmethod
    def update(cls, db: Session, quartierAffichage_id: int, updateQuartierAffichage: QuartierAffichageUpdateSchema) -> QuartierAffichageSchema:
        quartierAffichage = QuartierAffichage.get(db, quartierAffichage_id)
        if not quartierAffichage:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="QuartierAffichage not found")
        try:
            update_data = updateQuartierAffichage.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(quartierAffichage, key, value)
            quartierAffichage = QuartierAffichage.update(db, quartierAffichage)
            return QuartierAffichageSchema.from_orm(quartierAffichage)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    
    # update NomQuartier
    @classmethod
    def updateNomQuartier(cls, db: Session, quartierAffichage_id: int, nomQuartier: str) -> QuartierAffichageSchema:
        try:
            quartierAffichage = QuartierAffichage.get(db, quartierAffichage_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not quartierAffichage:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="QuartierAffichage not found")
        try:
            quartierAffichage.NomQuartier = nomQuartier
            db.add(quartierAffichage)
            db.commit()
            db.refresh(quartierAffichage)
            return QuartierAffichageSchema.from_orm(quartierAffichage)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # update SousQuartierAffich
    @classmethod
    def updateSousQuartierAffich(cls, db: Session, quartierAffichage_id: int, sousQuartierAffich: str) -> QuartierAffichageSchema:
        try:
            quartierAffichage = QuartierAffichage.get(db, quartierAffichage_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not quartierAffichage:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="QuartierAffichage not found")
        try:
            quartierAffichage.SousQuartierAffich = sousQuartierAffich
            db.add(quartierAffichage)
            db.commit()
            db.refresh(quartierAffichage)
            return QuartierAffichageSchema.from_orm(quartierAffichage)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # update ObservationsQuartier
    @classmethod
    def updateObservationsQuartier(cls, db: Session, quartierAffichage_id: int, observationsQuartier: str) -> QuartierAffichageSchema:
        try:
            quartierAffichage = QuartierAffichage.get(db, quartierAffichage_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not quartierAffichage:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="QuartierAffichage not found")
        try:
            quartierAffichage.ObservationsQuartier = observationsQuartier
            db.add(quartierAffichage)
            db.commit()
            db.refresh(quartierAffichage)
            return QuartierAffichageSchema.from_orm(quartierAffichage)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # update ArrondissementQuartier
    @classmethod
    def updateArrondissementQuartier(cls, db: Session, quartierAffichage_id: int, ArrondissementQuartier: str) -> QuartierAffichageSchema:
        try:
            quartierAffichage = QuartierAffichage.get(db, quartierAffichage_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not quartierAffichage:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="QuartierAffichage not found")
        try:
            quartierAffichage.ArrondissementQuartier = ArrondissementQuartier
            db.add(quartierAffichage)
            db.commit()
            db.refresh(quartierAffichage)
            return QuartierAffichageSchema.from_orm(quartierAffichage)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # delete
    @classmethod
    def delete(cls, db: Session, quartierAffichage_id: int) -> bool:
        quartierAffichage = QuartierAffichage.get(db, quartierAffichage_id)
        if not quartierAffichage:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="QuartierAffichage not found")
        try:
            return QuartierAffichage.delete(db, quartierAffichage_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        