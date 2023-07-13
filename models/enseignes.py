from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.Connexion import Base

class Enseigne(Base):
    __tablename__ = "Enseigne"

    # Clé primaire, identifiant unique
    IDEnseigne = Column(Integer, primary_key=True)

    # Clé unique, Code Enseigne
    CodeEnseigne = Column(String(6), nullable=False, unique=True)

    # Surface totale de l’Enseigne
    SurfaceEnseigne = Column(Float)

    # Nombre de face de l’Enseigne
    NbreFaceEnseigne = Column(Integer)

    # Spécidicité à la facturation, type Booléen. Cette spécificté est à prendre en compte à la facturation
    SpecificiteFacture = Column(Boolean)

    # Unité de facturation
    UniteFacturationEnseigne = Column(String(13))

    # Clé etrangère, identifiant unique de la table typeEnseigne
    IDTypeEnseigne = Column(Integer, ForeignKey("TypeEnseigne.IDTypeEnseigne"))

    # Clé étrangère, clé unique de la table TypeEnseigne 
    CodeTypeEnseigne = Column(String(9), ForeignKey("TypeEnseigne.CodeTypeEnseigne"))

    # Relation avec la table TypeEnseigne
    type_enseigne = relationship("TypeEnseigne", back_populates="enseignes")

    # Relation avec la table DispositifPub
    dispositifs = relationship("DispositifPub", back_populates="enseigne")
