from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.Connexion import Base
from models.dispositifs import DispositifPub

class Enseigne(DispositifPub):
    __tablename__ = "Enseigne"
    
    # Clé primaire, identifiant unique
    IDEnseigne = Column(Integer, ForeignKey("DispositifPub.IDDispositifPub"), primary_key=True)

    # Surface totale de l’Enseigne
    SurfaceEnseigne = Column(Float)

    # Nombre de face de l’Enseigne
    NbreFaceEnseigne = Column(Integer)

    # Spécidicité à la facturation, type Booléen. Cette spécificté est à prendre en compte à la facturation
    SpecificiteFacture = Column(Boolean)

    # Unité de facturation
    UniteFacturationEnseigne = Column(String(13))

    # Clé etrangère, identifiant unique de la table typeEnseigne
    IDTypeEnseigne = Column(Integer, ForeignKey("TypeEnseigne.IDTypeEnseigne", ondelete="CASCADE"))

    # Mapper argument for inheritance
    __mapper_args__ = {
        "polymorphic_identity": "Enseigne"
    }

    # Relation avec la table TypeEnseigne
    type_enseigne = relationship("TypeEnseigne", backref="enseignes", lazy="joined", cascade="save-update, merge")
