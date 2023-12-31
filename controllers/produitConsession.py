from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.produitConcession import ProduitConcession
from models.dispositifs import DispositifPub
from schemas.CampagneProduitSchema import ProduitConsessionCreateSchema, ProduitConsessionSchema, ProduitConsessionUpdateSchema

class ProduitConcessionController:
    # get
    @classmethod
    def get(cls, db: Session, produitConcession_id: int) -> ProduitConsessionSchema:
        try:
            produitConcession = ProduitConcession.get(db, produitConcession_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not produitConcession:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ProduitConcession not found")
        return ProduitConsessionSchema.model_validate(produitConcession)
    
    # get by CodeProduitConcession
    @classmethod
    def get_by_code(cls, db: Session, CodeProduitConcession: str) -> ProduitConsessionSchema:
        try:
            produitConcession = ProduitConcession.get_by_code(db, CodeProduitConcession)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not produitConcession:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ProduitConcession not found")
        return ProduitConsessionSchema.model_validate(produitConcession)
    
    # get all
    @classmethod
    def get_all(cls, db: Session) -> list[ProduitConsessionSchema]:
        try:
            produitConcessions = ProduitConcession.get_all(db)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not produitConcessions:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ProduitConcessions not found")
        return [ProduitConsessionSchema.model_validate(produitConcession) for produitConcession in produitConcessions]
    
    # create
    @classmethod
    def create(cls, db: Session, produitConcession: ProduitConsessionCreateSchema) -> ProduitConsessionSchema:
        # check if codeProduitConcession is unique
        if ProduitConcession.get_by_code(db, produitConcession.CodeProduitConcession):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="CodeProduitConcession already exists")
        # check if the foreign key IDDispositifPub is valid
        dispositifPub = DispositifPub.get(db, produitConcession.IDDispositifPub)
        if not dispositifPub:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid foreign key {produitConcession.IDDispositifPub}")
        try:
            produitConcession = ProduitConcession(**produitConcession.model_dump())
            produitConcession.dispositif_pub = dispositifPub
            produitConcession = ProduitConcession.create(db, produitConcession)
            return ProduitConsessionSchema.model_validate(produitConcession)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # update
    @classmethod
    def update(cls, db: Session, produitConcession_id: int, produitConcession: ProduitConsessionUpdateSchema) -> ProduitConsessionSchema:
        try:
            produitConcession_to_update = ProduitConcession.get(db, produitConcession_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not produitConcession:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ProduitConcession not found")
        try:
            # extract the fields to update
            update_data = produitConcession.model_dump(exclude_unset=True)
            # update the fields with a loop
            for key, value in update_data.items():
                setattr(produitConcession_to_update, key, value)
            ProduitConcession.update(db, produitConcession_to_update)
            return ProduitConsessionSchema.model_validate(produitConcession_to_update)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # delete
    @classmethod
    def delete(cls, db: Session, produitConcession_id: int) -> bool:
        try:
            produitConcession = ProduitConcession.get(db, produitConcession_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not produitConcession:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ProduitConcession not found")
        try:
            return ProduitConcession.delete(db, produitConcession_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))