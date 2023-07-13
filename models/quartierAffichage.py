from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base

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
    IDZoneAffichage = Column(Integer, ForeignKey("ZoneAffichage.IDZoneAffichage"))

    # clé étrangère, clé unique de la table ZoneAffichage
    CodeZone = Column(String(6), ForeignKey("ZoneAffichage.CodeZone"))

    # Relation avec la table ZoneAffichage
    zone_affichage = relationship("ZoneAffichage", back_populates="quartiers")

    # Relation avec la table EmplacementAffichage
    emplacements = relationship("EmplacementAffichage", back_populates="quartier")
