from datetime import datetime
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
    SurfaceDispositif = Column(Float)

    # UpdatedAt
    UpdatedAt = Column(DateTime)

    # CreatedAt
    CreatedAt = Column(DateTime)

    # Relation avec la table Produit
    produits = relationship("CampagneProduit", lazy="joined", back_populates="campagne_pub")

    # Generate code campagne
    @classmethod
    def generateCodeCampagne(cls, db: Session) -> str:
        # get the current year's last 2 digits
        year = str(datetime.now().year)[-2:]
        # Query the database to get the last generated CodeCampagne
        lastGeneratedCodeCampagne: CampagnePub = db.query(cls).order_by(cls.IDCampagnePub.desc()).first()
        # extract the last 5 digits from the last generated CodeCampagne
        if lastGeneratedCodeCampagne:
            # check if the year in the last generated code matches the current year
            if lastGeneratedCodeCampagne.CodeCampagne[2:4] == year:
                # increment the four digits by one
                lastGeneratedCodeCampagne = lastGeneratedCodeCampagne.CodeCampagne[-5:]
                lastGeneratedCodeCampagne = str(int(lastGeneratedCodeCampagne) + 1).zfill(5)
            else:
                # reset the four digits to "00001"
                lastGeneratedCodeCampagne = "00001"
        else:
            # use "00001" as the default value
            lastGeneratedCodeCampagne = "00001"
        return "CA" + year + lastGeneratedCodeCampagne

    # get by ID
    @classmethod
    def get(cls, db: Session, IDCampagnePub: int) -> 'CampagnePub':
        return db.query(cls).filter(cls.IDCampagnePub == IDCampagnePub).first()
    
    # get by CodeCampagne
    @classmethod
    def get_by_code(cls, db: Session, CodeCampagne: str) -> 'CampagnePub':
        return db.query(cls).filter(cls.CodeCampagne == CodeCampagne).first()
    
    # get all
    @classmethod
    def get_all(cls, db: Session) -> list['CampagnePub']:
        return db.query(cls).all()
    
    # create
    @classmethod
    def create(cls, db: Session, campagne: 'CampagnePub') -> 'CampagnePub':
        # Generate the CodeCampagne automatically
        campagne.CodeCampagne = cls.generateCodeCampagne(db)
        # set CreatedAt and UpdatedAt
        campagne.CreatedAt = campagne.UpdatedAt = datetime.now().isoformat()
        db.add(campagne)
        db.commit()
        db.refresh(campagne)
        return campagne
    
    # update
    @classmethod
    def update(cls, db:Session, campagne: 'CampagnePub') -> 'CampagnePub':
        # set UpdatedAt
        campagne.UpdatedAt = datetime.now().isoformat()
        db.add(campagne)
        db.commit()
        db.refresh(campagne)
        return campagne
    
    # delete
    @classmethod
    def delete(cls, db:Session, IDCampagnePub: int) -> bool:
        # get campagne_pub
        campagne_pub = cls.get(db, IDCampagnePub)
        if campagne_pub:
            db.delete(campagne_pub)
            db.commit()
            return True
        return False