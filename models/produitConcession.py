from sqlalchemy import Boolean, Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base
from sqlalchemy.orm import Session

from models.campagneProduit import CampagneProduit

class ProduitConcession(Base):
    __tablename__ = "ProduitConcession"

    # Clé primaire, identifiant unique 
    IDProduitConcession = Column(Integer, primary_key=True)

    # Clé unique, code du produit
    CodeProduitConcession = Column(String(6), nullable=False, unique=True)

    # Observations sur le produit
    ObservationsProduit = Column(String(254))

    # Duree minimale de facturation exprimee en nombre de jours
    DureeMinimaleFacturation = Column(Integer)

    # Le produit a des specificites de facturation
    HasSpecificiteFacturation = Column(Boolean, default=False)

    # Surface minimale de la specificite de facturation
    SurfaceMinSpecificiteFact = Column(Float, nullable=True)

    # Taux applicable de la specificite de facturation
    TauxApplicableSpecificiteFact = Column(Float, nullable=True)

    # Clé étrangère, identifiant unique de la table TypDispositif
    IDDispositifPub = Column(Integer, ForeignKey("DispositifPub.IDDispositifPub", ondelete="CASCADE"))

    # Relation avec la table DispositifPub
    dispositif_pub = relationship("DispositifPub", backref="produits", lazy="joined", cascade="save-update, merge")

    # Relation avec la table CampagnePub
    campagnes = relationship("CampagnePub", secondary="CampagneProduit", lazy="joined", cascade="save-update, merge")

    # get method
    @classmethod
    def get(cls, db: Session, produitConcession_id: int):
        return db.query(cls).filter(cls.IDProduitConcession == produitConcession_id).first()
    
    # get by CodeProduitConcession
    @classmethod
    def get_by_code(cls, db: Session, CodeProduitConcession: str):
        return db.query(cls).filter(cls.CodeProduitConcession == CodeProduitConcession).first()
    
    # get all
    @classmethod
    def get_all(cls, db: Session):
        return db.query(cls).all()
    
    # create
    @classmethod
    def create(cls, db: Session, produitConcession):
        db.add(produitConcession)
        db.commit()
        db.refresh(produitConcession)
        return produitConcession
    
    # delete
    @classmethod
    def delete(cls, db: Session, produitConcession_id: int):
        produitConcession = cls.get(db, produitConcession_id)
        if produitConcession:
            db.delete(produitConcession)
            db.commit()
            return True
        return False

    # update
    @classmethod
    def update(cls, db: Session, produitConcession):
        db.add(produitConcession)
        db.commit()
        db.refresh(produitConcession)
        return produitConcession