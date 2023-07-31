from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.campagne import CampagnePub
from models.campagneProduit import CampagneProduit
from models.produitConcession import ProduitConcession

from schemas.CampagneProduitSchema import CampagneProduitSchema, CampagneProduitCreateSchema, CampagneProduitUpdateSchema

class CampagneProduitController:
    # get
    @classmethod
    def get(cls, db: Session, IDCampagneProduit: int) -> CampagneProduitSchema:
        try:
            campagne = CampagneProduit.get(db, IDCampagneProduit)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not campagne:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Campagne not found")
        return CampagneProduitSchema.from_orm(campagne)

    # get all by IDProduitConcession
    @classmethod
    def get_all_by_IDProduitConcession(cls, db: Session, IDProduitConcession: int) -> list[CampagneProduitSchema]:
        try:
            return [CampagneProduitSchema.from_orm(campagne) for campagne in CampagneProduit.get_all_by_IDProduitConcession(db, IDProduitConcession)]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # get all by IDCampagnePub
    @classmethod
    def get_all_by_IDCampagnePub(cls, db: Session, IDCampagnePub: int) -> list[CampagneProduitSchema]:
        try:
            return [CampagneProduitSchema.from_orm(campagne) for campagne in CampagneProduit.get_by_IDCampagnePub(db, IDCampagnePub)]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # create
    @classmethod
    def create(cls, db: Session, campagneProduit: CampagneProduitCreateSchema) -> CampagneProduitSchema:
        # check if IDProduitConcession and IDCampagnePub exist
        try:
            produit_concession = ProduitConcession.get(db, campagneProduit.IDProduitConcession)
            campagne_pub = CampagnePub.get(db, campagneProduit.IDCampagnePub)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not produit_concession:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid foreign key {campagneProduit.IDProduitConcession}")
        if not campagne_pub:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid foreign key {campagneProduit.IDCampagnePub}")
        try:
            campagneProduit = CampagneProduit(**campagneProduit.dict())
            campagneProduit = CampagneProduit.create(db, campagneProduit)
            return CampagneProduitSchema.from_orm(campagneProduit)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # update
    @classmethod
    def update(cls, db: Session, updateCampagneProduit: CampagneProduitUpdateSchema) -> CampagneProduitSchema:
        try:
            campagneProduit = CampagneProduit.get(db, updateCampagneProduit.IDCampagneProduit)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not campagneProduit:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="CampagneProduit not found")
        try:
            update_data = updateCampagneProduit.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(campagneProduit, key, value)
            campagneProduit = CampagneProduit.update(db, campagneProduit)
            return CampagneProduitSchema.from_orm(campagneProduit)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDCampagneProduit: int) -> bool:
        try:
            campagneProduit = CampagneProduit.get(db, IDCampagneProduit)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not campagneProduit:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="CampagneProduit not found")
        try:
            return CampagneProduit.delete(db, IDCampagneProduit)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))