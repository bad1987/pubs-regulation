from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base

class TaxTiersDocEntete(Base):
    __tablename__ = "TaxTiersDocEntete"

    # Taux de taxe du tiers sur le document Entete
    TauxTaxeTiersDocEnt = Column(Float)

    # Clé Etrangère, identifiant unique de la table tiers
    IDTiers = Column(Integer, ForeignKey("TIERS.IDTiers"), primary_key=True)

    # Clé étrangère, clé unique de la table Tiers
    CodeTiers = Column(String(9), ForeignKey("TIERS.CodeTiers"), primary_key=True)

    # Clé étrangère, identifiant unique de la table Taxes
    IDTaxes = Column(Integer, ForeignKey("Taxes.IDTaxes"), primary_key=True)

    # Clé étrangère, clé unique de la table Taxes
    CodeTaxe = Column(String(6), ForeignKey("Taxes.CodeTaxe"), primary_key=True)

    # Clé étrangère, identifiant unique du DocEntete associé
    IDDocEntete = Column(Integer, ForeignKey("DocEntete.IDDocEntete"), primary_key=True)

    # Clé étrangère, clé unique du DocEntete
    NumDocEntete = Column(String(9), ForeignKey("DocEntete.NumDocEntete"), primary_key=True)

    # Relation avec la table TIERS
    tiers = relationship("TIERS", back_populates="taxes_doc_entete")

    # Relation avec la table Taxes
    taxe = relationship("Taxes", back_populates="taxes_doc_entete")

    # Relation avec la table DocEntete
    doc_entete = relationship("DocEntete", back_populates="taxes_doc_entete")
