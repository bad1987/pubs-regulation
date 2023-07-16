from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import relationship
from db.Connexion import Base

class TypeEnseigne(Base):
    __tablename__ = "TypeEnseigne"

    # Clé primaire, identifiant unique
    IDTypeEnseigne = Column(Integer, primary_key=True)

    # Clé unique
    CodeTypeEnseigne = Column(String(9), nullable=False, unique=True)

    # Libellé
    LibelleTypeEnseigne = Column(String(64))

    # Relation avec la table Enseigne
    enseignes = relationship("Enseigne", back_populates="type_enseigne", lazy="joined", cascade="save-update, merge")