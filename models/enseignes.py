from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import Session, relationship
from db.Connexion import Base
from models.dispositifs import DispositifPub

class Enseigne(DispositifPub):
    __tablename__ = "Enseigne"
    
    # Clé primaire, identifiant unique
    IDEnseigne = Column(Integer, ForeignKey("DispositifPub.IDDispositifPub", ondelete="CASCADE"), primary_key=True)

    # Surface totale de l’Enseigne
    SurfaceEnseigne = Column(Float)

    # Clé unique code Panneau
    CodeEnseigne = Column(String(6), nullable=False, unique=True)

    # Nombre de face de l’Enseigne
    NbreFaceEnseigne = Column(Integer)

    # Spécidicité à la facturation, type Booléen. Cette spécificté est à prendre en compte à la facturation
    SpecificiteFacture = Column(Boolean)

    # Unité de facturation
    UniteFacturationEnseigne = Column(String(13))

    # UpdatedAt
    UpdatedAt = Column(DateTime)

    # CreatedAt
    CreatedAt = Column(DateTime)

    # Clé etrangère, identifiant unique de la table typeEnseigne
    IDTypeEnseigne = Column(Integer, ForeignKey("TypeEnseigne.IDTypeEnseigne", ondelete="CASCADE"))

    # Mapper argument for inheritance
    __mapper_args__ = {
        "polymorphic_identity": "Enseigne"
    }

    # Relation avec la table TypeEnseigne
    type_enseigne = relationship("TypeEnseigne", backref="enseignes", lazy="joined", cascade="save-update, merge")

    # get by id
    @classmethod
    def get(cls, db: Session, IDEnseigne: int):
        return db.query(cls).filter_by(IDEnseigne=IDEnseigne).first()
    
    # get by code
    @classmethod
    def getByCode(cls, db: Session, codeEnseigne: str):
        return db.query(cls).filter_by(CodeEnseigne=codeEnseigne).first()
    
    # get all
    @classmethod
    def getAll(cls, db: Session):
        return db.query(cls).all()
    
    # create
    @classmethod
    def create(cls, db: Session, dispositif_pub):
        # set CreatedAt and UpdatedAt
        dispositif_pub.CreatedAt = dispositif_pub.UpdatedAt = datetime.now().isoformat()
        db.add(dispositif_pub)
        db.commit()
        db.refresh(dispositif_pub)
        return  dispositif_pub
    
    # update
    @classmethod
    def update(cls, db: Session, dispositif_pub):
        # set UpdatedAt
        dispositif_pub.UpdatedAt = datetime.now().isoformat()
        db.add(dispositif_pub)
        db.commit()
        db.refresh(dispositif_pub)
        return  dispositif_pub
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDEnseigne: int):
        enseigne = db.query(cls).filter_by(IDEnseigne=IDEnseigne).first()
        if enseigne:
            db.delete(enseigne)
            db.commit()
            return True
        return False