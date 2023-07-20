from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, Session
from db.Connexion import Base

class DispositifPub(Base):
    __tablename__ = "DispositifPub"

    # Clé primaire identifiant unique d’un dispositifPublicitaire
    IDDispositifPub = Column(Integer, primary_key=True)

    # Clé unique de la table 
    CodeDispositifPub = Column(String(6), nullable=False, unique=True)

    # Libellé dispositif Publicitaire
    LibelleDispoPub = Column(String(64))

    # Surface du dispositif publiciatire
    SurfaceDispoPub = Column(Float)

    # Unité de facturation
    UniteFacturationDispoPub = Column(String(50))

    # Clé etrangère identifiant unique de la table TypeDispositif
    IDTypeDispositif = Column(Integer, ForeignKey("TypeDispositif.IDTypeDispositif", ondelete="CASCADE"))

    # Clé étrangère, identifiant unique de la table TIERS
    IDTiers = Column(Integer, ForeignKey("Tiers.IDTiers", ondelete="CASCADE"))

    # Clé étrangère, identifiant unique de la table EmplacementAffichage
    IDEmplacementAffichage = Column(Integer, ForeignKey("EmplacementAffichage.IDEmplacementAffichage", ondelete="CASCADE"))

    # Type column for inheritance
    type = Column(String(32), nullable=False)

    # Mapper argument for inheritance
    __mapper_args__ = {
        "polymorphic_identity": "dispositif_pub",
        "polymorphic_on": type,
        "with_polymorphic": "*"
    }

    # Relations avec les autres tables
    type_dispositif = relationship("TypeDispositif", backref="dispositifs", lazy="joined", cascade="save-update, merge")
    tiers = relationship("Tiers", backref="dispositifs", lazy="joined", cascade="save-update, merge")
    emplacement_affichage = relationship("EmplacementAffichage", backref="dispositifs", cascade="save-update, merge")

    # get method
    @classmethod
    def get(cls, db: Session, IDDispositifPub: int):
        return db.query(cls).filter(cls.IDDispositifPub == IDDispositifPub).first()