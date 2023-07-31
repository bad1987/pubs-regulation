from sqlalchemy import Column, DateTime, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship, Session
from db.Connexion import Base

class CampagnePub(Base):
    __tablename__ = "CampagnePub"

    # Clé primaire identifiant unique d’une campagne
    IDCampagnePub = Column(Integer, primary_key=True)

    # Clé unique de la campagne
    CodeCampagne = Column(String(9), nullable=False, unique=True)

    # libellé de la campagne
    LibelleCampagne = Column(String(254))

    # date de début de la campagne
    DateDeb = Column(Date)

    # date de fin de la campagne
    DateFin = Column(Date)

    # Surface à occuper
    SurfaceDispoitif = Column(Float)

    # Relation avec la table Produit
    produits = relationship("ProduitConcession", secondary="CampagneProduit", lazy="joined", cascade="save-update, merge")

    # get by ID
    @classmethod
    def get(cls, db: Session, IDCampagnePub: int):
        return db.query(cls).filter(cls.IDCampagnePub == IDCampagnePub).first()
    
    # get by CodeCampagne
    @classmethod
    def get_by_code(cls, db: Session, CodeCampagne: str):
        return db.query(cls).filter(cls.CodeCampagne == CodeCampagne).first()
    
    # get all
    @classmethod
    def get_all(cls, db: Session):
        return db.query(cls).all()
    
    # create
    @classmethod
    def create(cls, db: Session, campagne):
        db.add(campagne)
        db.commit()
        db.refresh(campagne)
        return campagne
    
    # update
    @classmethod
    def update(cls, db:Session, campagne):
        db.add(campagne)
        db.commit()
        db.refresh(campagne)
        return campagne
    
    # delete
    @classmethod
    def delete(cls, db:Session, IDCampagnePub):
        # get campagne_pub
        campagne_pub = cls.get(db, IDCampagnePub)
        if campagne_pub:
            db.delete(campagne_pub)
            db.commit()
            return True
        return False