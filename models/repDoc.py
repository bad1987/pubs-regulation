from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base

class RepDoc(Base):
    __tablename__ = "RepDoc"

    # Clé primaire, identifiant unique de la table Taxe
    IDRepDoc = Column(Integer, primary_key=True)
    # Montant issue de la répartition
    MontantReparti = Column(Float)

    # Clé étrangère identifiant unique de la table DocEntete associé
    IDDocEntete = Column(Integer, ForeignKey("DocEntete.IDDocEntete"))

    # Clé étrangère, identifiant unique de la tables Repartition des frais
    IDRepartitionFrais = Column(Integer, ForeignKey("RepartitionFrais.IDRepartitionFrais"))

    # Relation avec la table DocEntete
    doc_entete = relationship("DocEntete", backref="repartitions")

    # Relation avec la table RepartitionFrais
    repartition_frais = relationship("RepartitionFrais", backref="repartitions")