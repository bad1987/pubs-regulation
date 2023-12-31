from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, SmallInteger, ForeignKey
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

    # UpdatedAt
    UpdatedAt = Column(DateTime)

    # CreatedAt
    CreatedAt = Column(DateTime)

    # get an instance of the class
    @classmethod
    def get(cls, db: Session, zoneAffichage_id: int):
        return db.query(cls).filter(cls.IDZoneAffichage == zoneAffichage_id).first()

    # get by CodeZone
    @classmethod
    def getByCodeZone(cls, db: Session, codeZone: str):
        return db.query(cls).filter(cls.CodeZone == codeZone).first()
    
    # get all
    @classmethod
    def getAll(cls, db: Session):
        return db.query(cls).all()

    # create an instance of the class
    @classmethod
    def create(cls, db: Session, zoneAffichage: 'ZoneAffichage'):
        # set CreatedAt and UpdatedAt
        zoneAffichage.CreatedAt = zoneAffichage.UpdatedAt = datetime.now()
        # Add the 'zoneAffichage' object to the database session
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
    
    # update
    @classmethod
    def update(cls, db: Session, zoneAffichage: 'ZoneAffichage'):
        # set UpdatedAt
        zoneAffichage.UpdatedAt = datetime.now()
        db.add(zoneAffichage)
        db.commit()
        db.refresh(zoneAffichage)
        return zoneAffichage

    # update libelleZone
    @classmethod
    def update_libelle_zone(cls, db: Session, zone_affichage_id: int, libelle_zone: str):
        # Retrieve the zone_affichage object from the database using the provided ID
        zone_affichage = cls.get(db, zone_affichage_id)

        # Check if the zone_affichage object exists
        if zone_affichage:
            # Update the LibelleZone attribute of the zone_affichage object with the provided libelle_zone value
            zone_affichage.LibelleZone = libelle_zone

            # Commit the changes to the database
            db.commit()

            # Return True to indicate that the update was successful
            return cls.get(db, zone_affichage_id)

        # Return False to indicate that the update was unsuccessful
        return None