from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
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
    DateReglt = Column(Date)

    # Montant Réglé
    MontantRegle = Column(Integer)

    # Solde
    SoldeRglt = Column(Float)

    # Statut Règlement (Acompte, Soldé)
    StatutRglt = Column(String(2))

    # Mode règlement
    ModeRglt = Column(String(9))

    # Clé étrangère, identifiant unique du DocEntete associé
    IDDocEntete = Column(Integer, ForeignKey("DocEntete.IDDocEntete", ondelete="CASCADE"))

    # Relation avec la table DocEntete
    doc_entete = relationship("DocEntete", backref="reglements", lazy="joined", cascade="save-update, merge")

    # get by id
    @classmethod
    def get_by_id(cls, IDReglement: int):
        return cls.query.filter_by(IDReglement=IDReglement).first()
    
    # get all
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    # create
    @classmethod
    def create(cls, db: Session, reglement):
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
    def updateDateReglt(cls, db: Session, IDReglement: int, DateReglt: Date):
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
    def delete(cls, db: Session, IDReglement: int):
        db.query(cls).filter_by(IDReglement=IDReglement).delete()
        db.commit()
        return True