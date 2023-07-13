from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base

class CampagnePub(Base):
    __tablename__ = "CampagnePub"

    # Clé primaire identifiant unique d’une campagne
    IDCampagnePub = Column(Integer, primary_key=True)

    # Clé unique de la campagne
    CodeCampagne = Column(String(9), nullable=False, unique=True)

    # libellé de la campagne
    LibeleCampagne = Column(String(254))

    # date de début de la campagne
    DateDeb = Column(Date)

    # date de fin de la campagne
    DateFin = Column(Date)

    # Surface à occuper
    SurfaceDispoitif = Column(Float)

    # Clé étrangère identifiant unique de la table Produit
    IDProduitConcession = Column(Integer, ForeignKey("Produit.IDProduitConcession"))

    # Clé étrangère clé unique ProduitConcession
    CodeProduitConcession = Column(String(6), ForeignKey("Produit.CodeProduitConcession"))

    # Relation avec la table Produit
    produit = relationship("Produit", back_populates="campagnes")
