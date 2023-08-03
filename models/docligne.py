from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, Session
from db.Connexion import Base

class DocLigne(Base):
    __tablename__ = "DocLigne"

    # Clé primaire Identifiant unique de la table
    IDDocLigne = Column(Integer, primary_key=True)

    # Numéro de ligne pour un document.
    NumLigne = Column(Integer)

    # Montant Toutes taxes comprises pour la ligne
    MontantTTCLigne = Column(Float)

    # Surface facturée 
    SurfaceOccupeFact = Column(Float)

    # Montant des taxes de la ligne
    MontantTaxeLigne = Column(Float)

    # Montant Hors Taxes de la ligne
    MontantHTLigne = Column(Integer)

    # UpdatedAt
    UpdatedAt = Column(DateTime)

    # CreatedAt
    CreatedAt = Column(DateTime)

    # Clé etrangère, identifiant unique du Document entete
    IDDocEntete = Column(Integer, ForeignKey("DocEntete.IDDocEntete", ondelete="CASCADE"))

    # Clé étrangère, identifiant unique de la table CampagneProduit
    IDCampagneProduit = Column(Integer, ForeignKey("CampagneProduit.IDCampagneProduit", ondelete="CASCADE"), unique=True)

    # Relations avec les autres tables
    doc_entete = relationship("DocEntete", backref="lignes", lazy="joined", cascade="save-update, merge")
    campagne_produit = relationship("CampagneProduit", uselist=False, backref="ligne", lazy="joined", cascade="save-update, merge")

    # get by id
    @classmethod
    def get(cls, db: Session, IDDocLigne: int):
        return db.query(cls).filter(cls.IDDocLigne == IDDocLigne).first()
    
    
    # get by IDDocEntete
    @classmethod
    def get_by_id_doc_entete(cls, db: Session, IDDocEntete: int):
        return db.query(cls).filter(cls.IDDocEntete == IDDocEntete).first()
    
    # get all
    @classmethod
    def get_all(cls, db: Session):
        return db.query(cls).all()
    
    # create
    @classmethod
    def create(cls, db: Session, doc_ligne):
        # set CreatedAt and UpdatedAt
        doc_ligne.CreatedAt = doc_ligne.UpdatedAt = datetime.now().isoformat()
        db.add(doc_ligne)
        db.commit()
        db.refresh(doc_ligne)
        return doc_ligne
    
    # update
    @classmethod
    def update(cls, db:Session, doc_ligne):
        # set UpdatedAt
        doc_ligne.UpdatedAt = datetime.now().isoformat()
        db.add(doc_ligne)
        db.commit()
        db.refresh(doc_ligne)
        return doc_ligne
    
    # delete
    @classmethod
    def delete(cls, db:Session, IDDocLigne):
        # get doc_ligne
        doc_ligne = cls.get(db, IDDocLigne)
        if doc_ligne:
            db.delete(doc_ligne)
            db.commit()
            return True
        return False