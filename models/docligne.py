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
    IDDocEntete = Column(Integer, ForeignKey("DocEntete.IDDocEntete", ondelete="CASCADE"))

    # Clé étrangère, identifiant unique de la table CampagnePub
    IDCampagnePub = Column(Integer, ForeignKey("CampagnePub.IDCampagnePub", ondelete="CASCADE"))

    # Clé étrangère, identifiant unique de la table Produit    
    IDProduitConcession = Column(Integer, ForeignKey("ProduitConcession.IDProduitConcession", ondelete="CASCADE"))

    # Relations avec les autres tables
    doc_entete = relationship("DocEntete", backref="lignes", lazy="joined", cascade="save-update, merge")
    campagne_pub = relationship("CampagnePub", backref="lignes", lazy="joined", cascade="save-update, merge")
    produit = relationship("ProduitConcession", backref="lignes", lazy="joined", cascade="save-update, merge")
