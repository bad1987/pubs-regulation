from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Float, Date
from db.Connexion import Base
from sqlalchemy.orm import Session

class RepartitionFrais(Base):
    __tablename__ = "RepartitionFrais"

    # Clé primaire, identifiant unique
    IDRepartitionFrais = Column(Integer, primary_key=True)

    # Entité intervenant dans la repartition
    IntervenantEntite = Column(String(15))

    # Taux de répartition
    TauxRepartition = Column(Float)

    # Année en cours.
    AnneeRepart = Column(Date)

    # UpdatedAt
    UpdatedAt = Column(DateTime)

    # CreatedAt
    CreatedAt = Column(DateTime)

    # get by id
    @classmethod
    def get(cls, db: Session, IDRepartitionFrais: int):
        return db.query(cls).filter_by(IDRepartitionFrais=IDRepartitionFrais).first()
    
    # get all
    @classmethod
    def get_all(cls, db: Session):
        return db.query(cls).all()
    
    # create
    @classmethod
    def create(cls, db: Session, rep_frais):
        # set CreatedAt and UpdatedAt
        rep_frais.CreatedAt = rep_frais.UpdatedAt = datetime.now()
        db.add(rep_frais)
        db.commit()
        db.refresh(rep_frais)
        return rep_frais
    
    # update
    @classmethod
    def update(cls, db: Session, rep_frais):
        # set UpdatedAt
        rep_frais.UpdatedAt = datetime.now()
        db.add(rep_frais)
        db.commit()
        db.refresh(rep_frais)
        return rep_frais
    
    # update IntervenantEntite
    @classmethod
    def updateIntervenantEntite(cls, db: Session, IDRepartitionFrais: int, IntervenantEntite: str):
        db.query(cls).filter_by(IDRepartitionFrais=IDRepartitionFrais).update({"IntervenantEntite": IntervenantEntite})
        db.commit()
        return cls.get(db, IDRepartitionFrais)
    
    # update TauxRepartition
    @classmethod
    def updateTauxRepartition(cls, db: Session, IDRepartitionFrais: int, TauxRepartition: float):
        db.query(cls).filter_by(IDRepartitionFrais=IDRepartitionFrais).update({"TauxRepartition": TauxRepartition})
        db.commit()
        return cls.get(db, IDRepartitionFrais)
    
    # update AnneeRepart
    @classmethod
    def updateAnneeRepart(cls, db: Session, IDRepartitionFrais: int, AnneeRepart: Date):
        db.query(cls).filter_by(IDRepartitionFrais=IDRepartitionFrais).update({"AnneeRepart": AnneeRepart})
        db.commit()
        return cls.get(db, IDRepartitionFrais)
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDRepartitionFrais: int):
        db.query(cls).filter_by(IDRepartitionFrais=IDRepartitionFrais).delete()
        db.commit()
        return True
