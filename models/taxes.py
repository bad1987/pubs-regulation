from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base

class Taxes(Base):
    __tablename__ = "Taxes"

    # Clé primaire, identifiant unique de la table Taxe
    IDTaxes = Column(Integer, primary_key=True)

    # Clé unique, Code Taxe
    CodeTaxe = Column(String(6), nullable=False, unique=True)

    # Libellé de la taxe
    LibelleTaxe = Column(String(25))

    # Taux de taxe
    TauxTaxe = Column(Float)

    # Relation avec la table TaxTiers
    tiers = relationship("TaxTiers", back_populates="taxe")
    taxes_doc_entete = relationship("TaxTiersDocEntete", back_populates="taxe")