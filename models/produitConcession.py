from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, ForeignKey
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

    # UpdatedAt
    UpdatedAt = Column(DateTime)

    # CreatedAt
    CreatedAt = Column(DateTime)

    # Clé étrangère, identifiant unique de la table TypDispositif
    IDDispositifPub = Column(Integer, ForeignKey("DispositifPub.IDDispositifPub", ondelete="CASCADE"))

    # Relation avec la table DispositifPub
    dispositif_pub = relationship("DispositifPub", backref="produits", lazy="joined", cascade="save-update, merge")

    # Relation avec la table CampagnePub
    campagnes = relationship("CampagneProduit", lazy="joined", back_populates="produit_concession")

    # Generate code produit concession
    @classmethod
    def generateCodeProduitConcession(cls, db: Session) -> str:
        # get the current year's last 2 digits
        year = str(datetime.now().year)[-2:]
        # Query the database to get the last generated CodeProduitConcession
        lastGeneratedCodeProduitConcession: ProduitConcession = db.query(cls).order_by(cls.IDProduitConcession.desc()).first()
        # extract the last 5 digits from the last generated CodeProduitConcession
        if lastGeneratedCodeProduitConcession:
            # check if the year in the last generated code matches the current year
            if lastGeneratedCodeProduitConcession.CodeProduitConcession[2:4] == year:
                # increment the five digits by one
                lastGeneratedCodeProduitConcession = lastGeneratedCodeProduitConcession.CodeProduitConcession[-5:]
                lastGeneratedCodeProduitConcession = str(int(lastGeneratedCodeProduitConcession) + 1).zfill(5)
            else:
                # reset the five digits to "00001"
                lastGeneratedCodeProduitConcession = "00001"
        else:
            # use "00001" as the default value
            lastGeneratedCodeProduitConcession = "00001"
        return "PC" + year + lastGeneratedCodeProduitConcession


    # get method
    @classmethod
    def get(cls, db: Session, produitConcession_id: int) -> 'ProduitConcession':
        return db.query(cls).filter(cls.IDProduitConcession == produitConcession_id).first()
    
    # get by CodeProduitConcession
    @classmethod
    def get_by_code(cls, db: Session, CodeProduitConcession: str) -> 'ProduitConcession':
        return db.query(cls).filter(cls.CodeProduitConcession == CodeProduitConcession).first()
    
    # get all
    @classmethod
    def get_all(cls, db: Session) -> list['ProduitConcession']:
        return db.query(cls).all()
    
    # create
    @classmethod
    def create(cls, db: Session, produitConcession: 'ProduitConcession') -> 'ProduitConcession':
        # Generate the CodeProduitConcession automatically
        produitConcession.CodeProduitConcession = cls.generateCodeProduitConcession(db)
        # set CreatedAt and UpdatedAt
        produitConcession.CreatedAt = produitConcession.UpdatedAt = datetime.now().isoformat()
        db.add(produitConcession)
        db.commit()
        db.refresh(produitConcession)
        return produitConcession
    
    # delete
    @classmethod
    def delete(cls, db: Session, produitConcession_id: int) -> bool:
        produitConcession = cls.get(db, produitConcession_id)
        if produitConcession:
            db.delete(produitConcession)
            db.commit()
            return True
        return False

    # update
    @classmethod
    def update(cls, db: Session, produitConcession: 'ProduitConcession') -> 'ProduitConcession':
        # set UpdatedAt
        produitConcession.UpdatedAt = datetime.now().isoformat()
        db.add(produitConcession)
        db.commit()
        db.refresh(produitConcession)
        return produitConcession