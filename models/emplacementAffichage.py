from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base

class EmplacementAffichage(Base):
    __tablename__ = "EmplacementAffichage"

    # Clé primaire, identifiant unique
    IDEmplacementAffichage = Column(Integer, primary_key=True)

    # Clé unique, Code de l’emplacement 
    CodeEmplacement = Column(String(3), unique=True)

    # Clé étrangère, identifiant unique de la table Quartier
    IDQuartierAffichage = Column(Integer, ForeignKey("Quartier.IDQuartierAffichage"))

    # Clé etrangère, clé unique de la table QuartierAffich
    NomQuartier = Column(String(25), ForeignKey("Quartier.NomQuartier"))

    # Relation avec la table Quartier
    quartier = relationship("Quartier", back_populates="emplacements")

    # Relation avec la table DispositifPub
    dispositifs = relationship("DispositifPub", back_populates="emplacement_affichage")
