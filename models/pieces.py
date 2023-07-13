from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base

class Piece(Base):
    __tablename__ = "Piece"

    # Clé primaire, identifiant unique de la table
    IDPiece = Column(Integer, primary_key=True)

    # Clé unique numéro de la pièce
    NumPiece = Column(String(15), unique=True)

    # Date de création de la pièce
    DateEmmission = Column(Date)

    # type de pièce (Avis favorable, Quitus d’affichage, reçu de paiement etc…)
    TypePiece = Column(String(4))

    # Clé étrangère, identifiant unique de la table Règlement
    IDReglement = Column(Integer, ForeignKey("Reglement.IDReglement"))

    # Clé étrangère, clé unique de la table Règlement
    NumReglt = Column(String(9), ForeignKey("Reglement.NumReglt"))

    # Relation avec la table Reglement
    reglement = relationship("Reglement", back_populates="pieces")
