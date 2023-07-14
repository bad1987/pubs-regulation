from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base
from sqlalchemy.orm import Session

class ZoneAffichage(Base):
     __tablename__ = "ZoneAffichage"

     # clé primaire, Identifiant unique
     IDZoneAffichage = Column(Integer, primary_key=True)

     # Clé unique
     CodeZone = Column(String(6), nullable=False, unique=True)

     # Libellé
     LibelleZone = Column(String(64))

     # Relation avec la table QuartierAffichage
     quartiers = relationship("QuartierAffichage", back_populates="zone_affichage",lazy="joined")

     # get an instance of the class
     @classmethod
     def get(cls, db: Session, zoneAffichage_id: int):
         return db.query(cls).filter(cls.IDZoneAffichage == zoneAffichage_id).first()

     # get by CodeZone
     @classmethod
     def getByCodeZone(cls, db: Session, codeZone: str):
         return db.query(cls).filter(cls.CodeZone == codeZone).first()

     # create an instance of the class
     @classmethod
     def create(cls, db: Session, zoneAffichage):
         db.add(zoneAffichage)
         db.commit()
         db.refresh(zoneAffichage)
         return zoneAffichage
     
     # delete an instance of the class
     @classmethod
     def delete(cls, db: Session, zoneAffichage_id: int):
         zoneAffichage = cls.get(db, zoneAffichage_id)
         if zoneAffichage:
             db.delete(zoneAffichage)
             db.commit()
             return True
         return False
     
     # get all instances of the class where quarter_id is in  quartiers
     @classmethod
     def getAllByQuartiers(cls, db: Session, quartier_id: int):
         return db.query(cls).filter(cls.quartiers.any(quartier_id)).all()
     
     # update libelleZone
     @classmethod
     def updateLibelleZone(cls, db: Session, zoneAffichage_id: int, libelleZone: str):
         zoneAffichage = cls.get(db, zoneAffichage_id)
         if zoneAffichage:
             zoneAffichage.LibelleZone = libelleZone
             db.commit()
             return True
         return False