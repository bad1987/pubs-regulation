from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base

class ZoneAffichage(Base):
     __tablename__ = "ZoneAffichage"

     # clé primaire, Identifiant unique
     IDZoneAffichage = Column(Integer, primary_key=True)

     # Clé unique
     CodeZone = Column(String(6), nullable=False, unique=True)

     # Libellé
     LibelleZone = Column(String(64))

     # Relation avec la table QuartierAffichage
     quartiers = relationship("QuartierAffichage", back_populates="zone_affichage")