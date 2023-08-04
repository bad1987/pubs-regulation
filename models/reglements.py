from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base
from sqlalchemy.orm import Session

class Reglement(Base):
    __tablename__ = "Reglement"

    # Clé primaire, identifiant unique
    IDReglement = Column(Integer, primary_key=True)

    # Clé unique, Numéro du reglèment
    NumReglt = Column(String(9), nullable=False, unique=True)

    # Date de règlement
    DateReglt = Column(DateTime)

    # Montant Réglé
    MontantRegle = Column(Integer)

    # Solde
    SoldeRglt = Column(Float)

    # Statut Règlement (Acompte, Soldé)
    StatutRglt = Column(String(2))

    # Mode règlement
    ModeRglt = Column(String(9))

    # UpdatedAt
    UpdatedAt = Column(DateTime)

    # CreatedAt
    CreatedAt = Column(DateTime)

    # Clé étrangère, identifiant unique du DocEntete associé
    IDDocEntete = Column(Integer, ForeignKey("DocEntete.IDDocEntete", ondelete="CASCADE"))

    # Relation avec la table DocEntete
    doc_entete = relationship("DocEntete", backref="reglements", lazy="joined", cascade="save-update, merge")

    # Generate num reglement
    @classmethod
    def generateNumReglt(cls, db: Session) -> str:
        # get the current year's last 2 digits
        year = str(datetime.now().year)[-2:]
        # Query the database to get the last generated NumReglt
        lastGeneratedNumReglt: Reglement = db.query(cls).order_by(cls.IDReglement.desc()).first()
        # extract the last 5 digits from the last generated NumReglt
        if lastGeneratedNumReglt:
            # check if the year in the last generated NumReglt matches the current year
            if lastGeneratedNumReglt.NumReglt[2:4] == year:
                # increment the five digits by one
                lastGeneratedNumReglt = lastGeneratedNumReglt.NumReglt[-5:]
                lastGeneratedNumReglt = str(int(lastGeneratedNumReglt) + 1).zfill(5)
            else:
                # reset the five digits to "00001"
                lastGeneratedNumReglt = "00001"
        else:
            # use "00001" as the default value
            lastGeneratedNumReglt = "00001"
        return "RG" + year + lastGeneratedNumReglt
    
    # get by id
    @classmethod
    def get(cls, db: Session, IDReglement: int) -> 'Reglement':
        return db.query(cls).filter_by(IDReglement=IDReglement).first()
    
    # get by NumReglt
    @classmethod
    def getByNumReglt(cls, db: Session, NumReglt: str) -> 'Reglement':
        return db.query(cls).filter_by(NumReglt=NumReglt).first()
    
    # get all
    @classmethod
    def get_all(cls, db: Session) -> list['Reglement']:
        return db.query(cls).all()
    
    # create
    @classmethod
    def create(cls, db: Session, reglement: 'Reglement') -> 'Reglement':
        # Generate num reglement 
        reglement.NumReglt = Reglement.generateNumReglt(db)
        # set CreatedAt and UpdatedAt
        reglement.CreatedAt = reglement.UpdatedAt = datetime.now()
        db.add(reglement)
        db.commit()
        db.refresh(reglement)
        return reglement

    # update
    @classmethod
    def update(cls, db: Session, reglement: 'Reglement') -> 'Reglement':
        # set UpdatedAt
        reglement.UpdatedAt = datetime.now()
        db.add(reglement)
        db.commit()
        db.refresh(reglement)
        return reglement
    
    # update NumReglt
    @classmethod
    def updateNumReglt(cls, db: Session, IDReglement: int, NumReglt: str):
        db.query(cls).filter_by(IDReglement=IDReglement).update({"NumReglt": NumReglt})
        db.commit()
        return cls.get(db, IDReglement)
    
    # update DateReglt
    @classmethod
    def updateDateReglt(cls, db: Session, IDReglement: int, DateReglt: DateTime):
        db.query(cls).filter_by(IDReglement=IDReglement).update({"DateReglt": DateReglt})
        db.commit()
        return cls.get(db, IDReglement)
    
    # update MontantRegle
    @classmethod
    def updateMontantRegle(cls, db: Session, IDReglement: int, MontantRegle: int):
        db.query(cls).filter_by(IDReglement=IDReglement).update({"MontantRegle": MontantRegle})
        db.commit()
        return cls.get(db, IDReglement)
    
    # update SoldeRglt
    @classmethod
    def updateSoldeRglt(cls, db: Session, IDReglement: int, SoldeRglt: float):
        db.query(cls).filter_by(IDReglement=IDReglement).update({"SoldeRglt": SoldeRglt})
        db.commit()
        return cls.get(db, IDReglement)
    
    # update StatutRglt
    @classmethod
    def updateStatutRglt(cls, db: Session, IDReglement: int, StatutRglt: str):
        db.query(cls).filter_by(IDReglement=IDReglement).update({"StatutRglt": StatutRglt})
        db.commit()
        return cls.get(db, IDReglement)
    
    # update ModeRglt
    @classmethod
    def updateModeRglt(cls, db: Session, IDReglement: int, ModeRglt: str):
        db.query(cls).filter_by(IDReglement=IDReglement).update({"ModeRglt": ModeRglt})
        db.commit()
        return cls.get(db, IDReglement)
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDReglement: int) -> bool:
        db.query(cls).filter_by(IDReglement=IDReglement).delete()
        db.commit()
        return True