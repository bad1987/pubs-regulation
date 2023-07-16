from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy import LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy.orm import relationship
from db.Connexion import Base

from models.docentete import DocEntete
from models.taxTiers import TaxTiers
from models.taxTiersDocEntete import TaxTiersDocEntete

class Tiers(Base):
    __tablename__ = "Tiers"

    # Clé primaire, identifiant unique de la table
    IDTiers = Column(Integer, primary_key=True)

    # Clé unique, Code Tiers
    CodeTiers = Column(String(9), nullable=False, unique=True)

    # Libelle tiers
    LibelleTiers = Column(String(64))

    # Adresse
    AdresseTiers = Column(String(128))

    # Téléphone
    TelephoneTiers = Column(SmallInteger)

    # Type de tiers (Régisseur, Régulateur, Annonceur, etc…)  
    TypeTiers = Column(Integer)

    # N° Contribuable
    NumCont = Column(String(22))

    # Adresse E-mail
    EmailTiers = Column(String(65))

    # Logo du tiers, cas  des régisseurs
    Logo = Column(LargeBinary)

    # Sigle
    SigleTiers = Column(String(2))

    # Relation avec la table DispositifPub
    dispositifs = relationship("DispositifPub", back_populates="tiers", lazy="joined", cascade="save-update, merge")

    # Relation avec la table DocEntete
    documents = relationship(DocEntete.__name__, back_populates="tiers")

    # Relation avec la table TaxTiers
    taxes = relationship(TaxTiers.__name__, back_populates="tiers")

    # Relation avec la table TaxTiersDocEntete
    taxes_doc_entete = relationship(TaxTiersDocEntete.__name__, back_populates="tiers")