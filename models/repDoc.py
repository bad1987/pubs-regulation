from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base

class RepDoc(Base):
    __tablename__ = "RepDoc"

    # Montant issue de la répartition
    MontantReparti = Column(Float)

    # Clé étrangère identifiant unique de la table DocEntete associé
    IDDocEntete = Column(Integer, ForeignKey("DocEntete.IDDocEntete"))

    # Clé étrangère, clé unique de la table DocEntente associé
    NumDocEntete = Column(String(9), ForeignKey("DocEntete.NumDocEntete"))

    # Clé étrangère, identifiant unique de la tables Repartition des frais
    IDRepartitionFrais = Column(Integer, ForeignKey("RepartitionFrais.IDRepartitionFrais"))

    # Relation avec la table DocEntete
    doc_entete = relationship("DocEntete", back_populates="repartitions")

    # Relation avec la table RepartitionFrais
    repartition_frais = relationship("RepartitionFrais", back_populates="repartitions")