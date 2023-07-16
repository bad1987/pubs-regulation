from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base

class TypePanneau(Base):
    __tablename__ = "TypePanneau"

    # Clé primaire, Identifiant Unique
    IDTypePanneau = Column(Integer, primary_key=True)

    # Clé unique
    CodeTypePanneau = Column(String(6), nullable=False, unique=True)

    # Libelle 
    LibelleType = Column(String(64))

    # Relation avec la table PanneauAffich
    panneaux = relationship("PanneauAffich", back_populates="type_panneau", lazy="joined", cascade="save-update, merge")
