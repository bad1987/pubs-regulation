from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base

class Reglement(Base):
    __tablename__ = "Reglement"

    # Clé primaire, identifiant unique
    IDReglement = Column(Integer, primary_key=True)

    # Clé unique, Numéro du reglèment
    NumReglt = Column(String(9), nullable=False, unique=True)

    # Date de règlement
    DateReglt = Column(Date)

    # Montant Réglé
    MontantRegle = Column(Integer)

    # Solde
    SoldeRglt = Column(Float)

    # Statut Règlement (Acompte, Soldé)
    StatutRglt = Column(String(2))

    # Mode règlement
    ModeRglt = Column(String(9))

    # Clé étrangère, identifiant unique du DocEntete associé
    IDDocEntete = Column(Integer, ForeignKey("DocEntete.IDDocEntete"))

    # Relation avec la table DocEntete
    doc_entete = relationship("DocEntete", backref="reglements")