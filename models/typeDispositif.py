from sqlalchemy import Column, Integer, String, SmallInteger, Binary, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import relationship
from db.Connexion import Base

class TypeDispositif(Base):
    __tablename__ = "TypeDispositif"

    # Clé primaire, identifiant unique
    IDTypeDispositif = Column(Integer, primary_key=True)

    # Clé unique
    CodeTypeDispositif = Column(String(6), nullable=False, unique=True)

    # Libellé
    LibelleTypeDispo = Column(String(25))

    # Relation avec la table DispositifPub
    dispositifs = relationship("DispositifPub", back_populates="type_dispositif")