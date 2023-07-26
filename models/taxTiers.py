from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base
from sqlalchemy.orm import Session

class TaxTiers(Base):
    __tablename__ = "TaxTiers"

    # Clé primaire
    IDTaxTiers = Column(Integer, primary_key=True)

    # Clé Etrangère, identifiant unique de la table tiers
    IDTiers = Column(Integer, ForeignKey("Tiers.IDTiers", ondelete="CASCADE"))

    # Clé étrangère, identifiant unique de la table Taxes
    IDTaxes = Column(Integer, ForeignKey("Taxes.IDTaxes", ondelete="CASCADE"))

    # Relation avec la table TIERS
    tiers = relationship("Tiers", backref="taxes", lazy="joined", cascade="save-update, merge, delete-orphan")

    # Relation avec la table Taxes
    taxe = relationship("Taxes", backref="tiers", lazy="joined", cascade="save-update, merge, delete-orphan")

    # get by id
    @classmethod
    def get(cls, db: Session, IDTaxTiers: int):
        return db.query(cls).filter_by(IDTaxTiers=IDTaxTiers).first()
    
    # get by id tiers and id taxes
    @classmethod
    def getByIDTiersAndIDTaxes(cls, db: Session, IDTiers: int, IDTaxes: int):
        return db.query(cls).filter_by(IDTiers=IDTiers, IDTaxes=IDTaxes).first()
    
    # get All
    @classmethod
    def getAll(cls, db: Session):
        return db.query(cls).all()

    # create
    @classmethod
    def create(cls, db: Session, tax_tiers):
        db.add(tax_tiers)
        db.commit()
        db.refresh(tax_tiers)
        return tax_tiers
    
    # update
    @classmethod
    def update(cls, db: Session, tax_tiers):
        db.add(tax_tiers)
        db.commit()
        db.refresh(tax_tiers)
        return tax_tiers
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDTaxTiers: int):
        # get tax_tiers
        tax_tiers = cls.get(db, IDTaxTiers)
        if tax_tiers:
            db.delete(tax_tiers)
            db.commit()
            return True
        return False