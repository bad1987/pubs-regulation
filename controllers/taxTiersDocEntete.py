from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.taxTiersDocEntete import TaxTiersDocEntete
from models.tiers import Tiers
from models.taxes import Taxes
from models.docentete import DocEntete

from schemas.TaxTiersDocEnteteSchema import TaxTiersDocEnteteSchema, TaxTiersDocEnteteUpdateSchema, TaxTiersDocEnteteCreateSchema

class TaxTiersDocEnteteController:
    # get
    @classmethod
    def get(cls, db: Session, IDTaxTiersDocEntete: int) -> TaxTiersDocEnteteSchema:
        try:
            tax_tiers_doc_entete = TaxTiersDocEntete.get(db, IDTaxTiersDocEntete)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not tax_tiers_doc_entete:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TaxTiersDocEntete not found")
        return TaxTiersDocEnteteSchema.from_orm(tax_tiers_doc_entete)
    
    # get by id tiers
    @classmethod
    def getByIDTiers(cls, db: Session, IDTiers: int) -> TaxTiersDocEnteteSchema:
        try:
            tax_tiers_doc_entete = TaxTiersDocEntete.getByIDTiers(db, IDTiers)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not tax_tiers_doc_entete:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TaxTiersDocEntete not found")
        return TaxTiersDocEnteteSchema.from_orm(tax_tiers_doc_entete)
    
    # get by id taxes
    @classmethod
    def getByIDTaxes(cls, db: Session, IDTaxes: int) -> TaxTiersDocEnteteSchema:
        try:
            tax_tiers_doc_entete = TaxTiersDocEntete.getByIDTaxes(db, IDTaxes)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not tax_tiers_doc_entete:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TaxTiersDocEntete not found")
        return TaxTiersDocEnteteSchema.from_orm(tax_tiers_doc_entete)
    
    # get all
    @classmethod
    def getAll(cls, db: Session) -> list[TaxTiersDocEnteteSchema]:
        try:
            tax_tiers_doc_entete = TaxTiersDocEntete.getAll(db)
            return [TaxTiersDocEnteteSchema.from_orm(tax_tiers_doc_entete) for tax_tiers_doc_entete in tax_tiers_doc_entete]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # create
    @classmethod
    def create(cls, db: Session, tax_tiers_doc_entete: TaxTiersDocEnteteCreateSchema) -> TaxTiersDocEnteteSchema:
        # check if IDTiers is valid
        tiers = Tiers.get(db, tax_tiers_doc_entete.IDTiers)
        if not tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid foreign key IDTiers: {tax_tiers_doc_entete.IDTiers}")
        # check if IDTaxes is valid
        taxes = Taxes.get(db, tax_tiers_doc_entete.IDTaxes)
        if not taxes:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid foreign key IDTaxes: {tax_tiers_doc_entete.IDTaxes}")
        # check if IDDocEntete is valid
        doc_entete = DocEntete.get(db, tax_tiers_doc_entete.IDDocEntete)
        if not doc_entete:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid foreign key IDDocEntete: {tax_tiers_doc_entete.IDDocEntete}")
        try:
            tax_tiers_doc_entete = TaxTiersDocEntete(**tax_tiers_doc_entete.dict())
            tax_tiers_doc_entete.tiers = tiers
            tax_tiers_doc_entete.taxe = taxes
            tax_tiers_doc_entete.doc_entete = doc_entete
            tax_tiers_doc_entete = TaxTiersDocEntete.create(db, tax_tiers_doc_entete)
            return TaxTiersDocEnteteSchema.from_orm(tax_tiers_doc_entete)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # update
    @classmethod
    def update(cls, db: Session, update_tax_tiers_doc_entete: TaxTiersDocEnteteUpdateSchema) -> TaxTiersDocEnteteSchema:
        try:
            tax_tiers_doc_entete = TaxTiersDocEntete.get(db, update_tax_tiers_doc_entete.IDTiersDocEntete)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not tax_tiers_doc_entete:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TaxTiersDocEntete not found")
        try:
            update_data = update_tax_tiers_doc_entete.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(tax_tiers_doc_entete, key, value)
            tax_tiers_doc_entete = TaxTiersDocEntete.update(db, tax_tiers_doc_entete)
            return TaxTiersDocEnteteSchema.from_orm(tax_tiers_doc_entete)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # delete
    @classmethod
    def delete(cls, db: Session, IDTaxTiersDocEntete: int) -> bool:
        try:
            return TaxTiersDocEntete.delete(db, IDTaxTiersDocEntete)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    