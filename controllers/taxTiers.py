from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.taxTiers import TaxTiers
from models.tiers import Tiers
from models.taxes import Taxes

from schemas.TaxTiersSchema import TaxTiersSchema, TaxTiersUpdateSchema, TaxTiersCreateSchema

class TaxTiersController:
    # get by id
    @classmethod
    def get(cls, db: Session, IDTaxTiers: int) -> TaxTiersSchema:
        try:
            tax_tiers = TaxTiers.get(db, IDTaxTiers)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not tax_tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TaxTiers not found")
        return TaxTiersSchema.model_validate(tax_tiers)
    
    # get by id tiers and id taxes
    @classmethod
    def getByIDTiersAndIDTaxes(cls, db: Session, IDTiers: int, IDTaxes: int) -> TaxTiersSchema:
        try:
            tax_tiers = TaxTiers.getByIDTiersAndIDTaxes(db, IDTiers, IDTaxes)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not tax_tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TaxTiers not found")
        return TaxTiersSchema.model_validate(tax_tiers)
    
    # get all
    @classmethod
    def getAll(cls, db: Session) -> list[TaxTiersSchema]:
        try:
            tax_tiers = TaxTiers.getAll(db)
            return [TaxTiersSchema.model_validate(tax_tiers) for tax_tiers in tax_tiers]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # create
    @classmethod
    def create(cls, db: Session, tax_tiers: TaxTiersCreateSchema) -> TaxTiersSchema:
        # check if the couple of IDTiers and IDTaxes is unique
        if TaxTiers.getByIDTiersAndIDTaxes(db, tax_tiers.IDTiers, tax_tiers.IDTaxes):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="TaxTiers already exists")
        # check if IDTiers is valid
        tiers = Tiers.get(db, tax_tiers.IDTiers)
        if not tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid foreign key IDTiers: {tax_tiers.IDTiers}")
        # check if IDTaxes is valid
        taxes = Taxes.get(db, tax_tiers.IDTaxes)
        if not taxes:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid foreign key IDTaxes: {tax_tiers.IDTaxes}")
        try:
            tax_tiers = TaxTiers(**tax_tiers.model_dump())
            tax_tiers.tiers = tiers
            tax_tiers.taxe = taxes
            tax_tiers = TaxTiers.create(db, tax_tiers)
            return TaxTiersSchema.model_validate(tax_tiers) 
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDTaxTiers: int) -> bool:
        try:
            return TaxTiers.delete(db, IDTaxTiers)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    