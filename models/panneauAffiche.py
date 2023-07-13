from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.Connexion import Base

class PanneauAffich(Base):
    __tablename__ = "PanneauAffich"

    # Clé primaire, identifiant unique de la table
    IDPanneauAffich = Column(Integer, primary_key=True)

    # Clé unique code Panneau
    CodePanneau = Column(String(6), nullable=False, unique=True)

    # Surface totale du panneau
    SuerfacePanneau = Column(Float)

    # Nombre de face du panneau
    NbreFacePanneau = Column(Integer)

    # Spécificité à la facturation
    SpecificiteFact = Column(Boolean)

    # Unité de facturation
    UniteFacturationPanneau = Column(String(13))

    # Clé etrangère, identifiant unique de la table TypePanneau
    IDTypePanneau = Column(Integer, ForeignKey("TypePanneau.IDTypePanneau"))

    # Clé étrangère, clé unique de la table TypePanneau 
    CodeTypePanneau = Column(String(6), ForeignKey("TypePanneau.CodeTypePanneau"))

    # Relation avec la table TypePanneau
    type_panneau = relationship("TypePanneau", back_populates="panneaux")

    # Relation avec la table DispositifPub
    dispositifs = relationship("DispositifPub", back_populates="panneau_affich")
