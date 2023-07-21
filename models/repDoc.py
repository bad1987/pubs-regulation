from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base
from sqlalchemy.orm import Session

class RepDoc(Base):
    __tablename__ = "RepDoc"

    # Clé primaire, identifiant unique de la table Taxe
    IDRepDoc = Column(Integer, primary_key=True)
    # Montant issue de la répartition
    MontantReparti = Column(Float)

    # Clé étrangère identifiant unique de la table DocEntete associé
    IDDocEntete = Column(Integer, ForeignKey("DocEntete.IDDocEntete", ondelete="CASCADE"))

    # Clé étrangère, identifiant unique de la tables Repartition des frais
    IDRepartitionFrais = Column(Integer, ForeignKey("RepartitionFrais.IDRepartitionFrais", ondelete="CASCADE"))

    # Relation avec la table DocEntete
    doc_entete = relationship("DocEntete", backref="repartitions", lazy="joined", cascade="save-update, merge")

    # Relation avec la table RepartitionFrais
    repartition_frais = relationship("RepartitionFrais", backref="repartitions", lazy="joined", cascade="save-update, merge")

    # get by id
    @classmethod
    def get(cls, db: Session, IDRepDoc: int):
        return db.query(cls).get(IDRepDoc)
    
    # get all
    @classmethod
    def getAll(cls, db: Session):
        return db.query(cls).all()
    
    # create
    @classmethod
    def create(cls, db: Session, rep_doc):
        db.add(rep_doc)
        db.commit()
        db.refresh(rep_doc)
        return rep_doc
    
    # update
    @classmethod
    def update(cls, db: Session, rep_doc):
        db.add(rep_doc)
        db.commit()
        db.refresh(rep_doc)
        return rep_doc
    
    # update MontantReparti
    @classmethod
    def updateMontantReparti(cls, db: Session, IDRepDoc: int, MontantReparti: float):
        db.query(cls).filter_by(IDRepDoc=IDRepDoc).update({"MontantReparti": MontantReparti})
        db.commit()
        return cls.get(db, IDRepDoc)
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDRepDoc: int):
        db.query(cls).filter_by(IDRepDoc=IDRepDoc).delete()
        db.commit()