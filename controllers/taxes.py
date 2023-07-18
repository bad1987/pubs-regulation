from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.taxes import Taxes
from schemas.TaxesSchema import TaxesCreateSchema, TaxesSchema

class TaxesController:

    # get by id
    @classmethod
    def get(cls, db: Session, tax_id: int) -> TaxesSchema:
        try:
            # Query the database to get the tax with the specified ID
            tax = db.query(Taxes).filter_by(IDTaxes=tax_id).first()
            if not tax:
                # If tax is not found, raise an HTTPException with status code 404
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tax not found")
            # Convert the tax object to a schema and return it
            return TaxesSchema.from_orm(tax)
        except Exception as e:
            # If there's an exception, raise an HTTPException with status code 500 and the error message
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # get all
    @classmethod
    def getAll(cls, db: Session) -> list[TaxesSchema]:
        try:
            # Query the database to get all taxes
            taxes = db.query(Taxes).all()
            if not taxes:
                # If no taxes are found, raise an HTTPException with status code 404
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Taxes not found")
            # Convert each tax object to a schema and return a list of schemas
            return [TaxesSchema.from_orm(tax) for tax in taxes]
        except Exception as e:
            # If there's an exception, raise an HTTPException with status code 500 and the error message
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # get by CodeTaxe
    @classmethod
    def getByCodeTaxe(cls, db: Session, CodeTaxe: str) -> TaxesSchema:
        try:
            # Query the database to get the tax with the specified CodeTaxe
            tax = db.query(Taxes).filter_by(CodeTaxe=CodeTaxe).first()
            if not tax:
                # If tax is not found, raise an HTTPException with status code 404
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tax not found")
            # Convert the tax object to a schema and return it
            return TaxesSchema.from_orm(tax)
        except Exception as e:
            # If there's an exception, raise an HTTPException with status code 500 and the error message
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # create
    @classmethod
    def create(cls, db: Session, tax: TaxesCreateSchema) -> TaxesSchema:
        try:
            # Check that CodeTaxe is unique by calling the getByCodeTaxe method
            if Taxes.getByCodeTaxe(db, tax.CodeTaxe):
                # If a tax with the same CodeTaxe already exists, raise an HTTPException with status code 409
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="CodeTaxe already exists")
            # Create a new tax in the database using the create method of the Taxes model
            tax = Taxes.create(db, tax)
            # Convert the created tax object to a schema and return it
            return TaxesSchema.from_orm(tax)
        except Exception as e:
            # If there's an exception, raise an HTTPException with status code 500 and the error message
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # This method updates the LibelleTaxe of a tax record in the database
    @classmethod
    def updateLibelleTaxe(cls, db: Session, IDTaxes: int, LibelleTaxe: str) -> TaxesSchema:
        try:
            # Check if the tax record exists in the database
            if not Taxes.get(db, IDTaxes):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tax not found")

            # Update the LibelleTaxe of the tax record
            tax = Taxes.updateLibelleTaxe(db, IDTaxes, LibelleTaxe)            
            return TaxesSchema.from_orm(tax)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # This method updates the TauxTaxe of a tax record in the database
    @classmethod
    def updateTauxTaxe(cls, db: Session, IDTaxes: int, TauxTaxe: float) -> TaxesSchema:
        try:
            # Check if the tax record exists in the database
            if not Taxes.get(db, IDTaxes):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tax not found")

            # Update the TauxTaxe of the tax record
            tax = Taxes.updateTauxTaxe(db, IDTaxes, TauxTaxe)            
            return TaxesSchema.from_orm(tax)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # This method updates the CodeTaxe of a tax record in the database
    @classmethod
    def updateCodeTaxe(cls, db: Session, IDTaxes: int, CodeTaxe: str) -> TaxesSchema:
        try:
            # Check if the tax record exists in the database
            if not Taxes.get(db, IDTaxes):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tax not found")

            # Update the CodeTaxe of the tax record
            tax = Taxes.updateCodeTaxe(db, IDTaxes, CodeTaxe)            
            return TaxesSchema.from_orm(tax)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # This method deletes a tax record from the database
    @classmethod
    def delete(cls, db: Session, IDTaxes: int):
        try:
            # Check if the tax record exists in the database
            if not Taxes.get(db, IDTaxes):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tax not found")

            # Delete the tax record
            Taxes.delete(db, IDTaxes)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
