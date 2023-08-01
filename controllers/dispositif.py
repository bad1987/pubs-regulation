# controller that implement all actions for DispositifPub model

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.emplacementAffichage import EmplacementAffichage
from models.dispositifs import DispositifPub
from models.typeDispositif import TypeDispositif
from models.tiers import Tiers

from schemas.DispositifPubSchema import DispositifPubSchema, DispositifPubCreateSchema, DispositifPubUpdateSchema

class DispositifPubController:

    @classmethod
    def get(cls, db: Session, IDDispositifPub: int) -> DispositifPubSchema:
        try:
            dispositifPub = DispositifPub.get(db, IDDispositifPub)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not dispositifPub:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DispositifPub not found")
        return DispositifPubSchema.model_validate(dispositifPub)
    
    @classmethod
    def get_by_code(cls, db: Session, CodeDispositifPub: str) -> DispositifPubSchema:
        try:
            dispositifPub = DispositifPub.get_by_code(db, CodeDispositifPub)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not dispositifPub:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DispositifPub not found")
        return DispositifPubSchema.model_validate(dispositifPub)
    
    @classmethod
    def get_all(cls, db: Session) -> list[DispositifPubSchema]:
        try:
            dispositifsPub = DispositifPub.get_all(db)
            return [DispositifPubSchema.model_validate(dispositifPub) for dispositifPub in dispositifsPub]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    @classmethod
    def create(cls, db: Session, dispositifPub: DispositifPubCreateSchema) -> DispositifPubSchema:
        # check if CodeDispositifPub is unique
        if DispositifPub.get_by_code(db, dispositifPub.CodeDispositifPub):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="CodeDispositifPub already exists")
        # check if the foreign key IDTiers is valid
        tiers = Tiers.get(db, dispositifPub.IDTiers)
        if not tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tiers not found")
        # check if the foreign key IDEmplacementAffichage is valid
        emplacementAffichage = EmplacementAffichage.get(db, dispositifPub.IDEmplacementAffichage)
        if not emplacementAffichage:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EmplacementAffichage not found")
        # check if the foreign key IDTypeDispositif is valid
        typeDispositif = TypeDispositif.get(db, dispositifPub.IDTypeDispositif)
        if not typeDispositif:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TypeDispositif not found")
        try:
            dispositifPub = DispositifPub(**dispositifPub.model_dump())
            dispositifPub.tiers = tiers
            dispositifPub.emplacement_affichage = emplacementAffichage
            dispositifPub.type_dispositif = typeDispositif
            dispositifPub = DispositifPub.create(db, dispositifPub)
            return DispositifPubSchema.model_validate(dispositifPub)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    @classmethod
    def update(cls, db: Session, updateDispositifPub: DispositifPubUpdateSchema) -> DispositifPubSchema:
        try:
            dispositifPub = DispositifPub.get(db, updateDispositifPub.IDDispositifPub)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not dispositifPub:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DispositifPub not found")
        try:
            update_data = updateDispositifPub.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(dispositifPub, key, value)
            dispositifPub = DispositifPub.update(db, dispositifPub)
            return DispositifPubSchema.model_validate(dispositifPub)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    @classmethod
    def delete(cls, db: Session, IDDispositifPub: int) -> bool:
        try:
            dispositifPub = DispositifPub.get(db, IDDispositifPub)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not dispositifPub:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DispositifPub not found")
        try:
            return DispositifPub.delete(db, IDDispositifPub)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    