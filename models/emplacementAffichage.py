from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Session
from db.Connexion import Base

class EmplacementAffichage(Base):
    __tablename__ = "EmplacementAffichage"

    # Clé primaire, identifiant unique
    IDEmplacementAffichage = Column(Integer, primary_key=True)

    # Clé unique, Code de l’emplacement 
    CodeEmplacement = Column(String(3), unique=True)

    # UpdatedAt
    UpdatedAt = Column(DateTime)

    # CreatedAt
    CreatedAt = Column(DateTime)

    # Clé étrangère, identifiant unique de la table Quartier
    IDQuartierAffichage = Column(Integer, ForeignKey("QuartierAffichage.IDQuartierAffichage", ondelete="CASCADE"))

    # Relation avec la table Quartier
    quartier = relationship("QuartierAffichage", backref="emplacements", cascade="save-update, merge")

    # get
    @classmethod
    def get(cls, db: Session, IDEmplacementAffichage: int):
        return db.query(cls).filter(cls.IDEmplacementAffichage == IDEmplacementAffichage).first()
    
    # get by CodeEmplacement
    @classmethod
    def get_by_code(cls, db: Session, CodeEmplacement: str):
        return db.query(cls).filter(cls.CodeEmplacement == CodeEmplacement).first()
    
    # get all by IDQuartierAffichage
    @classmethod
    def get_all_by_id_quartier(cls, db: Session, IDQuartierAffichage: int):
        return db.query(cls).filter(cls.IDQuartierAffichage == IDQuartierAffichage).all()

    # get all
    @classmethod
    def get_all(cls, db: Session):
        return db.query(cls).all()
    
    # create
    @classmethod
    def create(cls, db: Session, emplacementAffichage):
        # set CreatedAt and UpdatedAt
        emplacementAffichage.CreatedAt = emplacementAffichage.UpdatedAt = datetime.now().isoformat()
        db.add(emplacementAffichage)
        db.commit()
        db.refresh(emplacementAffichage)
        return emplacementAffichage
    
    # update
    @classmethod
    def update(cls, db: Session, emplacementAffichage):
        # set UpdatedAt
        emplacementAffichage.UpdatedAt = datetime.now().isoformat()
        db.add(emplacementAffichage)
        db.commit()
        db.refresh(emplacementAffichage)
        return emplacementAffichage
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDEmplacementAffichage: int):
        emplacementAffichage = EmplacementAffichage.get(db, IDEmplacementAffichage)
        if emplacementAffichage:
            db.delete(emplacementAffichage)
            db.commit()
            return True
        return False