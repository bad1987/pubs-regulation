from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.dispositifs import DispositifPub
from models.emplacementAffichage import EmplacementAffichage

from models.panneauAffiche import PanneauAffich
from models.tiers import Tiers
from models.typePanneau import TypePanneau
from models.typeDispositif import TypeDispositif

from schemas.PanneauAffich import PanneauAffichSchema, PanneauAffichUpdateSchema, PanneauAffichCreateSchema

class PanneauAffichController:
    # get
    @classmethod
    def get(cls, db: Session, IDPanneauAffich: int) -> PanneauAffichSchema:
        try:
            panneauAffich = PanneauAffich.get(db, IDPanneauAffich)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not panneauAffich:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PanneauAffich not found")
        return PanneauAffichSchema.from_orm(panneauAffich)
    
    # get by CodePanneau
    @classmethod
    def get_by_code(cls, db: Session, CodePanneau: str) -> PanneauAffichSchema:
        try:
            panneauAffich = PanneauAffich.get_by_code(db, CodePanneau)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not panneauAffich:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PanneauAffich not found")
        return PanneauAffichSchema.from_orm(panneauAffich)
    
    # get all
    @classmethod
    def get_all(cls, db: Session) -> list[PanneauAffichSchema]:
        try:
            panneauAffichs = PanneauAffich.get_all(db)
            return [PanneauAffichSchema.from_orm(panneauAffich) for panneauAffich in panneauAffichs]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # create
    @classmethod
    def create(cls, db: Session, panneauAffich: PanneauAffichCreateSchema) -> PanneauAffichSchema:
        # check if codePanneau is unique
        if PanneauAffich.get_by_code(db, panneauAffich.CodePanneau):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="CodePanneau already exists")
        # check CodeDispositifPub is unique
        if DispositifPub.get_by_code(db, panneauAffich.CodeDispositifPub):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="CodeDispositifPub already exists")
        # check if foreign key IDEmplacementAffichage is valid
        emplacementAffichage = EmplacementAffichage.get(db, panneauAffich.IDEmplacementAffichage)
        if not emplacementAffichage:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EmplacementAffichage not found")
        # check if foreign key IDTiers is valid
        tiers = Tiers.get(db, panneauAffich.IDTiers)
        if not tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tiers not found")
        # check if foreign key IDTypePanneau is valid
        typePanneau = TypePanneau.get(db, panneauAffich.IDTypePanneau)
        if not typePanneau:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TypePanneau not found")
        # check if the foreign key IDTypeDispositif is valid
        type_dispositif = TypeDispositif.get(db, panneauAffich.IDTypeDispositif)
        if not type_dispositif:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TypeDispositif not found")
        
        try:
            panneauAffich = PanneauAffich(**panneauAffich.dict())
            panneauAffich.tiers = tiers
            panneauAffich.emplacement_affichage = emplacementAffichage
            panneauAffich.type_panneau = typePanneau
            panneauAffich.type_dispositif = type_dispositif
            panneauAffich = PanneauAffich.create(db, panneauAffich)
            return PanneauAffichSchema.from_orm(panneauAffich)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # update
    @classmethod
    def update(cls, db: Session, updatePanneauAffich: PanneauAffichUpdateSchema) -> PanneauAffichSchema:
        try:
            panneauAffich = PanneauAffich.get(db, updatePanneauAffich.IDPanneauAffich)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not panneauAffich:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PanneauAffich not found")
        try:
            update_data = updatePanneauAffich.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(panneauAffich, key, value)
            panneauAffich = PanneauAffich.update(db, panneauAffich)
            return PanneauAffichSchema.from_orm(panneauAffich)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # delete
    @classmethod
    def delete(cls, db: Session, IDPanneauAffich: int) -> bool:
        try:
            panneauAffich = PanneauAffich.get(db, IDPanneauAffich)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not panneauAffich:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PanneauAffich not found")
        try:
            return PanneauAffich.delete(db, IDPanneauAffich)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))