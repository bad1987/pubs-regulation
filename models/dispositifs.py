from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base

class DispositifPub(Base):
    __tablename__ = "DispositifPub"

    # Clé primaire identifiant unique d’un dispositifPublicitaire
    IDDispositifPub = Column(Integer, primary_key=True)

    # Clé unique de la table 
    CodeDispositifPub = Column(String(6), nullable=False, unique=True)

    # Libellé dispositif Publicitaire
    LibelleDispoPub = Column(String(64))

    # Surface du dispositif publiciatire
    SurfaceDispoPub = Column(Float)

    # Unité de facturation
    UniteFacturationDispoPub = Column(String(50))

    # Clé etrangère identifiant unique de la table TypeDispositif
    IDTypeDispositif = Column(Integer, ForeignKey("TypeDispositif.IDTypeDispositif"))

    # Clé étrangère table Enseigne
    IDEnseigne = Column(Integer, ForeignKey("Enseigne.IDEnseigne"))

    # Clé étrangère table Panneau d’affichage
    IDPanneauAffich = Column(Integer, ForeignKey("PanneauAffich.IDPanneauAffich"))

    # Clé étrangère, identifiant unique de la table TIERS
    IDTiers = Column(Integer, ForeignKey("TIERS.IDTiers"))

    # Clé étrangère, identifiant unique de la table EmplacementAffichage
    IDEmplacementAffichage = Column(Integer, ForeignKey("EmplacementAffichage.IDEmplacementAffichage"))

    # Relations avec les autres tables
    type_dispositif = relationship("TypeDispositif", back_populates="dispositifs")
    enseigne = relationship("Enseigne", back_populates="dispositifs")
    panneau_affich = relationship("PanneauAffich", back_populates="dispositifs")
    tiers = relationship("TIERS", back_populates="dispositifs")
    emplacement_affichage = relationship("EmplacementAffichage", back_populates="dispositifs")
