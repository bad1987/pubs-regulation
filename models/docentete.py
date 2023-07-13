from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, CHAR
from sqlalchemy.orm import relationship
from db.Connexion import Base

class DocEntete(Base):
    __tablename__ = "DocEntete"

    # Clé primaire, Identifiant unique de la table DocEntete
    IDDocEntete = Column(Integer, primary_key=True)

    # Type de document de type Integer, ici la codification peut être 1 pour l’Enrôlement, 2 pour la Commande, 3 pour une Facture Doit, 4 pour une Facture d’Avoir
    TypeDocEntete = Column(Integer)

    # Numéro de document, Clé unique
    NumDocEntete = Column(String(9), nullable=False, unique=True)

    # Date de création du document, type date
    DateDocEntete = Column(Date)

    # Montant HT du document, Cas commande ou facture par exemple
    MontantHTDoc = Column(Integer)

    # Montant total des taxes, type réel
    MontantTaxeDoc = Column(Float)

    # Montant toutes taxes comprises du document
    MontantTTCDoc = Column(Float)

    # Statut du document, pour le cas d’une Commande, on a en attente de validation (AV), Validé (VA), pour une facture, on a Réglé (RG), Non Réglé (NR) 
    StatutDoc = Column(CHAR(2))

    # Pénalités pour le cas d’une commande
    PenalitesDoc = Column(Integer)

    # Clé étrangère, identifiant unique de la table Tiers
    IDTiers = Column(Integer, ForeignKey("TIERS.IDTiers"))

    # clé étrangère, clé unique de la table Tiers 
    CodeTiers = Column(String(9), ForeignKey("TIERS.CodeTiers"))

    # Relation avec la table Tiers
    tiers = relationship("TIERS", back_populates="documents")
    
    # Relation avec la table DocLigne
    lignes = relationship("DocLigne", back_populates="doc_entete")

    taxes_doc_entete = relationship("TaxTiersDocEntete", back_populates="doc_entete")

