from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base
from sqlalchemy.orm import Session

class QuartierAffichage(Base):
    __tablename__ = "QuartierAffichage"

    # Clé primaire, identifiant unique
    IDQuartierAffichage = Column(Integer, primary_key=True)

    # Clé unique, Code du Quartier
    NomQuartier = Column(String(25), nullable=False, unique=True)

    # Sous-Quatier
    SousQuartierAffich = Column(String(65))

    # Observations
    ObservationsQuartier = Column(String(254))

    # Arrondissement
    ArrondissementQuartier = Column(String(65))

    # UpdatedAt
    UpdatedAt = Column(DateTime)

    # CreatedAt
    CreatedAt = Column(DateTime)

    # Clé étrangère, Identifiant unique de la table ZoneAffichage 
    IDZoneAffichage = Column(Integer, ForeignKey("ZoneAffichage.IDZoneAffichage", ondelete="CASCADE"))

    # Relation avec la table ZoneAffichage
    zone_affichage = relationship("ZoneAffichage", backref="quartiers", lazy="joined", cascade="save-update, merge")

    # get an instance of the class
    @classmethod
    def get(cls, db: Session, quartierAffichage_id: int):
        return db.query(cls).filter(cls.IDQuartierAffichage == quartierAffichage_id).first()

    # get by NomQuartier
    @classmethod
    def get_by_nom_quartier(cls, db: Session, NomQuartier: str):
        return db.query(cls).filter(cls.NomQuartier == NomQuartier).first()

    # get all
    @classmethod
    def get_all(cls, db: Session):
        return db.query(cls).all()

    # create an instance of the class
    @classmethod
    def create(cls, db: Session, quartierAffichage):
        # set CreatedAt and UpdatedAt
        quartierAffichage.CreatedAt = quartierAffichage.UpdatedAt = datetime.now()
        db.add(quartierAffichage)
        db.commit()
        db.refresh(quartierAffichage)
        return quartierAffichage
    
    # delete an instance of the class
    @classmethod
    def delete(cls, db: Session, quartierAffichage_id: int):
        quartierAffichage = cls.get(db, quartierAffichage_id)
        if quartierAffichage:
            db.delete(quartierAffichage)
            db.commit()
            return True
        return False
    
    # update
    @classmethod
    def update(cls, db: Session, quartierAffichage):
        # set UpdatedAt
        quartierAffichage.UpdatedAt = datetime.now()
        db.add(quartierAffichage)
        db.commit()
        db.refresh(quartierAffichage)
        return quartierAffichage