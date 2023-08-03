from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.Connexion import Base
from models.dispositifs import DispositifPub
from sqlalchemy.orm import Session

from models.typePanneau import TypePanneau

class PanneauAffich(DispositifPub):
    __tablename__ = "PanneauAffich"
    
    # Clé primaire, identifiant unique de la table
    IDPanneauAffich = Column(Integer, ForeignKey("DispositifPub.IDDispositifPub", ondelete="CASCADE"), primary_key=True)

    # Clé unique code Panneau
    CodePanneau = Column(String(6), nullable=False, unique=True)

    # Surface totale du panneau
    SurfacePanneau = Column(Float)

    # Nombre de face du panneau
    NbreFacePanneau = Column(Integer)

    # Spécificité à la facturation
    SpecificiteFact = Column(Boolean)

    # Unité de facturation
    UniteFacturationPanneau = Column(String(13))

    # UpdatedAt
    UpdatedAt = Column(DateTime)

    # CreatedAt
    CreatedAt = Column(DateTime)

    # Clé etrangère, identifiant unique de la table TypePanneau
    IDTypePanneau = Column(Integer, ForeignKey("TypePanneau.IDTypePanneau", ondelete="CASCADE"), primary_key=True)

    # Mapper argument for inheritance
    __mapper_args__ = {
        "polymorphic_identity": "PanneauAffich"
    }

    # Relation avec la table TypePanneau
    type_panneau = relationship("TypePanneau", backref="panneaux", lazy="joined", cascade="save-update, merge")
    
    # get by ID
    @classmethod
    def get(cls, db: Session, IDPanneauAffich: int):
        return db.query(cls).filter_by(IDPanneauAffich=IDPanneauAffich).first()
    
    # get by CodePanneau
    @classmethod
    def getByCode(cls, db: Session, codePanneau: str):
        return db.query(cls).filter_by(CodePanneau=codePanneau).first()
    
    # get all
    @classmethod
    def getAll(cls, db: Session):
        return db.query(cls).all()
    
    # create
    @classmethod
    def create(cls, db: Session, panneauAffich):
        # set CreatedAt and UpdatedAt
        panneauAffich.CreatedAt = panneauAffich.UpdatedAt = datetime.now().isoformat()
        db.add(panneauAffich)
        db.commit()
        db.refresh(panneauAffich)
        return panneauAffich
    
    # update
    @classmethod
    def update(cls, db: Session, panneauAffich):
        # set UpdatedAt
        panneauAffich.UpdatedAt = datetime.now().isoformat()
        db.add(panneauAffich)
        db.commit()
        db.refresh(panneauAffich)
        return panneauAffich
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDPanneauAffich):
        # get the object
        panneauAffich = cls.get(db, IDPanneauAffich)
        if panneauAffich:
            db.delete(panneauAffich)
            db.commit()
            return True
        return False