from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, Session
from db.Connexion import Base
from models.typeDispositif import TypeDispositif

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

    # UpdatedAt
    UpdatedAt = Column(DateTime)

    # CreatedAt
    CreatedAt = Column(DateTime)

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
    
    # get by CodeDispositifPub
    @classmethod
    def get_by_code(cls, db: Session, CodeDispositifPub: str):
        return db.query(cls).filter(cls.CodeDispositifPub == CodeDispositifPub).first()
    
    # get all
    @classmethod
    def get_all(cls, db: Session):
        return db.query(cls).all()
    
    # create
    @classmethod
    def create(cls, db:Session, dispositif_pub):
        # set CreatedAt and UpdatedAt
        dispositif_pub.CreatedAt = dispositif_pub.UpdatedAt = datetime.now().isoformat()
        db.add(dispositif_pub)
        db.commit()
        db.refresh(dispositif_pub)
        return dispositif_pub
    
    # update
    @classmethod
    def update(cls, db:Session, dispositif_pub):
        # set UpdatedAt
        dispositif_pub.UpdatedAt = datetime.now().isoformat()
        db.add(dispositif_pub)
        db.commit()
        db.refresh(dispositif_pub)
        return dispositif_pub
    
    # delete
    @classmethod
    def delete(cls, db:Session, IDDispositifPub):
        # get dispositif_pub
        dispositif_pub = cls.get(db, IDDispositifPub)
        if dispositif_pub:
            db.delete(dispositif_pub)
            db.commit()
            return True
        return False