from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.quartierAffichage import QuartierAffichage
from schemas.ZoneAffichage import ZoneAffichageCreateSchema
from zoneAffichage import ZoneAffichage

class ZoneAffichageController:

    # get zoneAffichage
    @classmethod
    def get(cls, db: Session, zoneAffichage_id: int):
        # if zoneAffichage does not exist, throw an error
        zoneAffichage = ZoneAffichage.get(db, zoneAffichage_id)
        if not zoneAffichage:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ZoneAffichage not found")
        return zoneAffichage

    # get all zoneAffichage by quartier_id
    @classmethod
    def getAllByQuartiers(cls, db: Session, quartier_id: int):
        try:
            return ZoneAffichage.getAllByQuartiers(db, quartier_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # create zoneAffichage
    @classmethod
    def create(cls, db: Session, zoneAffichage: ZoneAffichageCreateSchema):
        # check if CodeZone is unique
        if ZoneAffichage.getByCodeZone(db, zoneAffichage.CodeZone):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ZoneAffichage already exists with CodeZone")

        try:
            zoneAffichage = ZoneAffichage(**zoneAffichage.model_dump())
            for quartier_id in zoneAffichage.quartiers:
                quartierAffichage = QuartierAffichage.get(db, quartier_id)
                if not quartierAffichage:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"QuartierAffichage with id {quartier_id} not found")
                zoneAffichage.quartiers.append(quartierAffichage)
            zoneAffichage = ZoneAffichage.create(db, zoneAffichage)
            return zoneAffichage
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )
    
    # delete zoneAffichage
    @classmethod
    def delete(cls, db: Session, zoneAffichage_id: int):
        # if zoneAffichage does not exist, throw an error
        zoneAffichage = ZoneAffichage.get(db, zoneAffichage_id)
        if not zoneAffichage:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ZoneAffichage not found")
        try:
            ZoneAffichage.delete(db, zoneAffichage_id)
            return True
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

    # update libelleZone
    @classmethod
    def updateLibelleZone(cls, db: Session, zoneAffichage_id: int, libelleZone: str):
        try:
            return ZoneAffichage.updateLibelleZone(db, zoneAffichage_id, libelleZone)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )