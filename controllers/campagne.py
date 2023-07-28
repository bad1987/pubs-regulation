from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.campagne import CampagnePub
from models.produitConcession import ProduitConcession

from schemas.CampagneSchema import CampagnePubSchema, CampagnePubCreateSchema, CampagnePubUpdateSchema

class CampagnePubController:
    # get
    @classmethod
    def get(cls, db: Session, IDCampagnePub: int) -> CampagnePubSchema:
        try:
            campagne = CampagnePub.get(db, IDCampagnePub)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not campagne:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Campagne not found")
        return CampagnePubSchema.from_orm(campagne)

    # get by CodeCampagne
    @classmethod
    def getByCodeCampagne(cls, db: Session, CodeCampagne: str) -> CampagnePubSchema:
        try:
            campagne = CampagnePub.get_by_code(db, CodeCampagne)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not campagne:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Campagne not found")
        return CampagnePubSchema.from_orm(campagne)
    
    # get all
    @classmethod
    def getAll(cls, db: Session) -> list[CampagnePubSchema]:
        try:
            return [CampagnePubSchema.from_orm(campagne) for campagne in CampagnePub.get_all(db)]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # create
    @classmethod
    def create(cls, db: Session, campagne: CampagnePubCreateSchema) -> CampagnePubSchema:
        # check if IDProduitConcession exists
        produit_concession = ProduitConcession.get(db, campagne.IDProduitConcession)
        if not produit_concession:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid foreign key {campagne.IDProduitConcession}")
        try:
            campagne = CampagnePub(**campagne.dict())
            campagne.produit = produit_concession
            campagne = CampagnePub.create(db, campagne)
            return CampagnePubSchema.from_orm(campagne)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # update
    @classmethod
    def update(cls, db: Session, updateCampagne: CampagnePubUpdateSchema) -> CampagnePubSchema:
        try:
            campagne = CampagnePub.get(db, updateCampagne.IDCampagnePub)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not campagne:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Campagne not found")
        try:
            update_data = updateCampagne.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(campagne, key, value)
            campagne = CampagnePub.update(db, campagne)
            return CampagnePubSchema.from_orm(campagne)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDCampagnePub: int) -> bool:
        # Try to get the campagne with the given IDCampagnePub from the database
        try:
            campagne = CampagnePub.get(db, IDCampagnePub)
        except Exception as e:
            # If there is an error, raise an HTTPException with a 500 status code
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        # If the campagne is not found in the database, raise an HTTPException with a 404 status code
        if not campagne:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Campagne not found")

        # Try to delete the campagne from the database
        try:
            return CampagnePub.delete(db, IDCampagnePub)
        except Exception as e:
            # If there is an error, raise an HTTPException with a 500 status code
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
