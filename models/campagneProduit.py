from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship, Session
from db.Connexion import Base

# from models.campagne import CampagnePub

class CampagneProduit(Base):
    __tablename__ = "CampagneProduit"

    # Clé primaire identifiant unique de la table
    IDCampagneProduit = Column(Integer, primary_key=True)

    # surface facturable
    SurfaceFacturable = Column(Float, nullable=True)

    # UpdatedAt
    UpdatedAt = Column(DateTime)

    # CreatedAt
    CreatedAt = Column(DateTime)

    # Clé étrangère identifiant unique de la table Produit
    IDProduitConcession = Column(Integer, ForeignKey("ProduitConcession.IDProduitConcession", ondelete="CASCADE"), nullable=False)

    # Clé étrangère, identifiant unique de la table CampagnePub
    IDCampagnePub = Column(Integer, ForeignKey("CampagnePub.IDCampagnePub", ondelete="CASCADE"), nullable=False)

    # Relation avec la table Campagne
    campagne_pub = relationship("CampagnePub", back_populates="produits", lazy="joined")

    # Relation avec la table ProduitConcession
    produit_concession = relationship("ProduitConcession", back_populates="campagnes", lazy="joined")


    # get by id
    @classmethod
    def get(cls, db: Session, IDCampagneProduit: int):
        return db.query(cls).filter(cls.IDCampagneProduit == IDCampagneProduit).first()
    
    # get all by IDProduitConcession
    @classmethod
    def get_all_by_IDProduitConcession(cls, db: Session, IDProduitConcession: int):
        return db.query(cls).filter(cls.IDProduitConcession == IDProduitConcession).all()
    
    # get by IDCampagnePub
    @classmethod
    def get_by_IDCampagnePub(cls, db: Session, IDCampagnePub: int):
        return db.query(cls).filter(cls.IDCampagnePub == IDCampagnePub).all()
    
    # get all
    @classmethod
    def get_all(cls, db: Session):
        return db.query(cls).all()

    # create
    @classmethod
    def create(cls, db: Session, campagne_produit):
        # set CreatedAt and UpdatedAt
        campagne_produit.CreatedAt = campagne_produit.UpdatedAt = datetime.now().isoformat()
        db.add(campagne_produit)
        db.commit()
        db.refresh(campagne_produit)
        return campagne_produit
    
    # update
    @classmethod
    def update(cls, db: Session, campagne_produit):
        # set UpdatedAt
        campagne_produit.UpdatedAt = datetime.now().isoformat()
        db.add(campagne_produit)
        db.commit()
        db.refresh(campagne_produit)
        return campagne_produit
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDCampagneProduit: int):
        campagne_produit = CampagneProduit.get(db, IDCampagneProduit)
        if campagne_produit:
            db.delete(campagne_produit)
            db.commit()
            return True
        return False