from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base
from sqlalchemy.orm import Session

# Define the Taxes class which inherits from the Base class
class Taxes(Base):
    # Set the table name for the Taxes class
    __tablename__ = "Taxes"

    # Define the primary key column, IDTaxes
    IDTaxes = Column(Integer, primary_key=True)

    # Define the CodeTaxe column which is a unique string of length 6
    CodeTaxe = Column(String(6), nullable=False, unique=True)

    # Define the LibelleTaxe column which is a string of length 25
    LibelleTaxe = Column(String(25))

    # Define the TauxTaxe column which is a floating-point number
    TauxTaxe = Column(Float)

    # UpdatedAt
    UpdatedAt = Column(DateTime)

    # CreatedAt
    CreatedAt = Column(DateTime)

    # Define a class method to get a Taxes object by its IDTaxes
    @classmethod
    def get(cls, db: Session, IDTaxes: int):
        return db.query(cls).get(IDTaxes)

    # Define a class method to get all Taxes objects
    @classmethod
    def getAll(cls, db: Session):
        return db.query(cls).all()

    # Define a class method to get a Taxes object by its CodeTaxe
    @classmethod
    def getByCodeTaxe(cls, db: Session, CodeTaxe: str):
        return db.query(cls).filter_by(CodeTaxe=CodeTaxe).first()

    # Define a class method to create a new Taxes object
    @classmethod
    def create(cls, db: Session, tax_tiers):
        # set CreatedAt and UpdatedAt
        tax_tiers.CreatedAt = tax_tiers.UpdatedAt = datetime.now()
        db.add(tax_tiers)
        db.commit()
        db.refresh(tax_tiers)
        return tax_tiers
    
    # update
    @classmethod
    def update(cls, db: Session, tax_tiers):
        # set UpdatedAt
        tax_tiers.UpdatedAt = datetime.now()
        db.add(tax_tiers)
        db.commit()
        db.refresh(tax_tiers)
        return tax_tiers

    # Define a class method to update the LibelleTaxe of a Taxes object
    @classmethod
    def updateLibelleTaxe(cls, db: Session, IDTaxes: int, LibelleTaxe: str):
        db.query(cls).filter_by(IDTaxes=IDTaxes).update({"LibelleTaxe": LibelleTaxe})
        db.commit()
        return cls.get(db, IDTaxes)

    # Define a class method to update the TauxTaxe of a Taxes object
    @classmethod
    def updateTauxTaxe(cls, db: Session, IDTaxes: int, TauxTaxe: float):
        db.query(cls).filter_by(IDTaxes=IDTaxes).update({"TauxTaxe": TauxTaxe})
        db.commit()
        return cls.get(db, IDTaxes)

    # Define a class method to update the CodeTaxe of a Taxes object
    @classmethod
    def updateCodeTaxe(cls, db: Session, IDTaxes: int, CodeTaxe: str):
        db.query(cls).filter_by(IDTaxes=IDTaxes).update({"CodeTaxe": CodeTaxe})
        db.commit()
        return cls.get(db, IDTaxes)

    # Define a class method to delete a Taxes object by its IDTaxes
    @classmethod
    def delete(cls, db: Session, tax_tiers_id: int):
        db.query(cls).filter_by(IDTaxes=tax_tiers_id).delete()
        db.commit()
        return True
