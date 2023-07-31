from sqlalchemy import Column, DateTime, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship, Session
from db.Connexion import Base

class CampagneProduit(Base):
    __tablename__ = "CampagneProduit"

    # Clé primaire identifiant unique de la table
    IDCampagneProduit = Column(Integer, primary_key=True)

    # surface facturable
    SurfaceFacturable = Column(Float, nullable=True)

    # Clé étrangère identifiant unique de la table Produit
    IDProduitConcession = Column(Integer, ForeignKey("ProduitConcession.IDProduitConcession", ondelete="CASCADE"))

    # Clé étrangère, identifiant unique de la table CampagnePub
    IDCampagnePub = Column(Integer, ForeignKey("CampagnePub.IDCampagnePub", ondelete="SET NULL"))
