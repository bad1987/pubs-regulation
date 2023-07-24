# controller that implement all actions for DispositifPub model

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.emplacementAffichage import EmplacementAffichage
from models.dispositifs import DispositifPub
from models.typeDispositif import TypeDispositif
from models.tiers import Tiers

from schemas.DispositifPubSchema import DispositifPubSchema, DispositifPubCreateSchema, DispositifPubUpdateSchema

class DispositifPubController:
    def get(self, db: Session, IDDispositifPub: int) -> DispositifPubSchema:
        try:
            dispositifPub = DispositifPub.get(db, IDDispositifPub)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not dispositifPub:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DispositifPub not found")
        return DispositifPubSchema.from_orm(dispositifPub)
    
    def get_by_code(self, db: Session, CodeDispositifPub: str) -> DispositifPubSchema:
        try:
            dispositifPub = DispositifPub.get_by_code(db, CodeDispositifPub)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not dispositifPub:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DispositifPub not found")
        return DispositifPubSchema.from_orm(dispositifPub)
    
    def get_all(self, db: Session) -> list[DispositifPubSchema]:
        try:
            dispositifsPub = DispositifPub.get_all(db)
            return [DispositifPubSchema.from_orm(dispositifPub) for dispositifPub in dispositifsPub]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    def create(self, db: Session, dispositifPub: DispositifPubCreateSchema) -> DispositifPubSchema:
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
            dispositifPub = DispositifPub(**dispositifPub.dict())
            dispositifPub.tiers = tiers
            dispositifPub.emplacement_affichage = emplacementAffichage
            dispositifPub.type_dispositif = typeDispositif
            dispositifPub = DispositifPub.create(db, dispositifPub)
            return DispositifPubSchema.from_orm(dispositifPub)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    def update(self, db: Session, updateDispositifPub: DispositifPubUpdateSchema) -> DispositifPubSchema:
        try:
            dispositifPub = DispositifPub.get(db, updateDispositifPub.IDDispositifPub)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not dispositifPub:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DispositifPub not found")
        try:
            update_data = updateDispositifPub.dict(unset_unset=True)
            for key, value in update_data.items():
                setattr(dispositifPub, key, value)
            dispositifPub = DispositifPub.update(db, dispositifPub)
            return DispositifPubSchema.from_orm(dispositifPub)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    def delete(self, db: Session, IDDispositifPub: int) -> bool:
        try:
            dispositifPub = DispositifPub.get(db, IDDispositifPub)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not dispositifPub:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DispositifPub not found")
        try:
            return DispositifPub.delete(db, dispositifPub)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    