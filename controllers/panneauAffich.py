from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.panneauAffiche import PanneauAffich
from models.typePanneau import TypePanneau

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

