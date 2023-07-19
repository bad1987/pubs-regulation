from sqlalchemy import Column, Integer, String, ForeignKey
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
    ArrondissementQaurtier = Column(String(65))

    # Clé étrangère, Identifiant unique de la table ZoneAffichage 
    IDZoneAffichage = Column(Integer, ForeignKey("ZoneAffichage.IDZoneAffichage", ondelete="CASCADE"))

    # Relation avec la table ZoneAffichage
    zone_affichage = relationship("ZoneAffichage", backref="quartiers")

    # get an instance of the class
    @classmethod
    def get(cls, db: Session, quartierAffichage_id: int):
        return db.query(cls).filter(cls.IDQuartierAffichage == quartierAffichage_id).first()

    # create an instance of the class
    @classmethod
    def create(cls, db: Session, quartierAffichage):
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
    
    