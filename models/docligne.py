from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base

class DocLigne(Base):
    __tablename__ = "DocLigne"

    # Clé primaire Identifiant unique de la table
    IDDocLigne = Column(Integer, primary_key=True)

    # Numéro de ligne pour un document.
    NumLigne = Column(Integer)

    # Montant Toutes taxes comprises pour la ligne
    MontantTTCLigne = Column(Float)

    # Surface facturée 
    SurfaceOccupeFact = Column(Float)

    # Montant des taxes de la ligne
    MontantTaxeLigne = Column(Float)

    # Montant Hors Taxes de la ligne
    MontantHTLigne = Column(Integer)

    # Clé etrangère, identifiant unique du Document entete
    IDDocEntete = Column(Integer, ForeignKey("DocEntete.IDDocEntete"))

    # Clé étrangère, clé unique de la table DocEntete
    NumDocEntete = Column(String(9), ForeignKey("DocEntete.NumDocEntete"))

    # Clé étrangère, identifiant unique de la table CampagnePub
    IDCampagnePub = Column(Integer, ForeignKey("CampagnePub.IDCampagnePub"))

    # Clé étrangère, clé unique de la table CampagnePub
    CodeCampagne = Column(String(9), ForeignKey("CampagnePub.CodeCampagne"))

    # Clé étrangère, identifiant unique de la table Produit    
    IDProduitConcession = Column(Integer, ForeignKey("Produit.IDProduitConcession"))

    # Clé étrangère, clé unique de la table Produit
    CodeProduitConcession = Column(String(6), ForeignKey("Produit.CodeProduitConcession"))

    # Relations avec les autres tables
    doc_entete = relationship("DocEntete", back_populates="lignes")
    campagne_pub = relationship("CampagnePub", back_populates="lignes")
    produit = relationship("Produit", back_populates="lignes")
