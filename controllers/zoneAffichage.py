from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.quartierAffichage import QuartierAffichage
from schemas.ZoneAffichage import ZoneAffichageCreateSchema, ZoneAffichageSchema, ZoneAffichageUpdateSchema
from models.zoneAffichage import ZoneAffichage


class ZoneAffichageController:

    # get zoneAffichage
    @classmethod
    def get(cls, db: Session, zoneAffichage_id: int) -> ZoneAffichageSchema:
        # if zoneAffichage does not exist, throw an error
        zoneAffichage = ZoneAffichage.get(db, zoneAffichage_id)
        if not zoneAffichage:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="ZoneAffichage not found")
        return ZoneAffichageSchema.model_validate(zoneAffichage)

    # get all zoneAffichage by CodeZone
    @classmethod
    def getByCodeZone(cls, db: Session, codeZone: str) -> ZoneAffichageSchema:
        # if zoneAffichage does not exist, throw an error
        zoneAffichage = ZoneAffichage.getByCodeZone(db, codeZone)
        if not zoneAffichage:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="ZoneAffichage not found")
        try:
            return ZoneAffichageSchema.model_validate(ZoneAffichage.getByCodeZone(db, codeZone))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
    
    # get all zoneAffichage
    @classmethod
    def getAll(cls, db: Session) -> list[ZoneAffichageSchema]:
        try:
            return [ZoneAffichageSchema.model_validate(zoneAffichage) for zoneAffichage in ZoneAffichage.getAll(db)]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))

    # create zoneAffichage
    @classmethod
    def create(cls, db: Session, zoneAffichage: ZoneAffichageCreateSchema) -> ZoneAffichageSchema:
        # check if CodeZone is unique
        if ZoneAffichage.getByCodeZone(db, zoneAffichage.CodeZone):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="ZoneAffichage already exists with CodeZone")

        try:
            zoneAffichage = ZoneAffichage(**zoneAffichage.model_dump())
            zoneAffichage = ZoneAffichage.create(db, zoneAffichage)
            return ZoneAffichageSchema.model_validate(zoneAffichage)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

    # delete zoneAffichage
    @classmethod
    def delete(cls, db: Session, zoneAffichage_id: int) -> bool:
        # if zoneAffichage does not exist, throw an error
        zoneAffichage = ZoneAffichage.get(db, zoneAffichage_id)
        if not zoneAffichage:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="ZoneAffichage not found")
        try:
            return ZoneAffichage.delete(db, zoneAffichage_id)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

    # update libelleZone
    @classmethod
    def updateLibelleZone(cls, db: Session, zoneAffichage_id: int, libelleZone: str) -> ZoneAffichageSchema:
        # if zoneAffichage does not exist, throw an error
        zoneAffichage = ZoneAffichage.get(db, zoneAffichage_id)
        if not zoneAffichage:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="ZoneAffichage not found")
        try:
            zoneAffichage = ZoneAffichage.update_libelle_zone(db, zoneAffichage_id, libelleZone)
            return ZoneAffichageSchema.model_validate(zoneAffichage)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

    # update
    @classmethod
    def update(cls, db: Session, zoneAffichage_id: int, updateZoneAffichage: ZoneAffichageUpdateSchema) -> ZoneAffichageSchema:
        # if zoneAffichage does not exist, throw an error
        zoneAffichage = ZoneAffichage.get(db, zoneAffichage_id)
        if not zoneAffichage:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="ZoneAffichage not found")
        try:
            update_data = updateZoneAffichage.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(zoneAffichage, key, value)
            zoneAffichage = ZoneAffichage.update(db, zoneAffichage)
            return ZoneAffichageSchema.model_validate(zoneAffichage)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )