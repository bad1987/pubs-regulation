from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base
from sqlalchemy.orm import Session

from models.taxes import Taxes

class TaxTiers(Base):
    __tablename__ = "TaxTiers"

    # Clé primaire
    IDTaxTiers = Column(Integer, primary_key=True)

    # Clé Etrangère, identifiant unique de la table tiers
    IDTiers = Column(Integer, ForeignKey("Tiers.IDTiers"))

    # Clé étrangère, identifiant unique de la table Taxes
    IDTaxes = Column(Integer, ForeignKey("Taxes.IDTaxes"))

    # Relation avec la table TIERS
    tiers = relationship("Tiers", back_populates="taxes")

    # Relation avec la table Taxes
    taxe = relationship(Taxes.__name__, back_populates="tiers")

    # create
    @classmethod
    def create(cls, db: Session, tax_tiers):
        db.add(tax_tiers)
        db.commit()
        db.refresh(tax_tiers)
        return tax_tiers