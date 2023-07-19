from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base


class ProduitConcession(Base):
    __tablename__ = "ProduitConcession"

    # Clé primaire, identifiant unique 
    IDProduitConcession = Column(Integer, primary_key=True)

    # Clé unique, code du produit
    CodeProduitConcession = Column(String(6), nullable=False, unique=True)

    # Observations sur le produit
    ObservationsProduit = Column(String(254))

    # Clé étrangère, identifiant unique de la table TypDispositif
    IDDispositifPub = Column(Integer, ForeignKey("DispositifPub.IDDispositifPub", ondelete="CASCADE"))

    # Relation avec la table DispositifPub
    dispositif_pub = relationship("DispositifPub", backref="produits", lazy="joined", cascade="save-update, merge")