from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.Connexion import Base
from models.dispositifs import DispositifPub

class PanneauAffich(DispositifPub):
    
    # Clé primaire, identifiant unique de la table
    IDPanneauAffich = Column(Integer, ForeignKey("DispositifPub.IDDispositifPub"), primary_key=True)

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

    # Mapper argument for inheritance
    __mapper_args__ = {
        "polymorphic_identity": "panneau_affich"
    }

    # Relation avec la table TypePanneau
    type_panneau = relationship("TypePanneau", back_populates="panneaux")