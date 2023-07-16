from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base

class TaxTiers(Base):
    __tablename__ = "TaxTiers"

    # Clé Etrangère, identifiant unique de la table tiers
    IDTiers = Column(Integer, ForeignKey("Tiers.IDTiers"), primary_key=True)

    # Clé étrangère, identifiant unique de la table Taxes
    IDTaxes = Column(Integer, ForeignKey("Taxes.IDTaxes"), primary_key=True)

    # Relation avec la table TIERS
    tiers = relationship("Tiers", back_populates="taxes")

    # Relation avec la table Taxes
    taxe = relationship("Taxes", back_populates="tiers")