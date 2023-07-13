from sqlalchemy import Column, Integer, String, Float, Date
from db.Connexion import Base

class RepartitionFrais(Base):
    __tablename__ = "RepartitionFrais"

    # Clé primaire, identifiant unique
    IDRepartitionFrais = Column(Integer, primary_key=True)

    # Entité intervenant dans la repartition
    IntervenantEntite = Column(String(15))

    # Taux de répartition
    TauxRepartition = Column(Float)

    # Année en cours.
    AnneeRepart = Column(Date)
