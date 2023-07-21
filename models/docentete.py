from sqlalchemy import Column, DateTime, Integer, String, Date, Float, ForeignKey, CHAR
from sqlalchemy.orm import relationship, Session
from db.Connexion import Base

class DocEntete(Base):
    __tablename__ = "DocEntete"

    # Clé primaire, Identifiant unique de la table DocEntete
    IDDocEntete = Column(Integer, primary_key=True)

    # Type de document de type Integer, ici la codification peut être 1 pour l’Enrôlement, 2 pour la Commande, 3 pour une Facture Doit, 4 pour une Facture d’Avoir
    TypeDocEntete = Column(Integer)

    # Numéro de document, Clé unique
    NumDocEntete = Column(String(9), nullable=False, unique=True)

    # Date de création du document, type date
    DateDocEntete = Column(DateTime)

    # Montant HT du document, Cas commande ou facture par exemple
    MontantHTDoc = Column(Integer)

    # Montant total des taxes, type réel
    MontantTaxeDoc = Column(Float)

    # Montant toutes taxes comprises du document
    MontantTTCDoc = Column(Float)

    # Statut du document, pour le cas d’une Commande, on a en attente de validation (AV), Validé (VA), pour une facture, on a Réglé (RG), Non Réglé (NR) 
    StatutDoc = Column(CHAR(2))

    # Pénalités pour le cas d’une commande
    PenalitesDoc = Column(Integer)

    # Clé étrangère, identifiant unique de la table Tiers
    IDTiers = Column(Integer, ForeignKey("Tiers.IDTiers", ondelete="CASCADE"))

    # Relation avec la table Tiers
    tiers = relationship("Tiers", backref="documents", lazy="joined", cascade="save-update, merge")

    # get
    @classmethod
    def get(cls, db: Session, IDDocEntete: int):
        return db.query(cls).filter_by(IDDocEntete=IDDocEntete).first()
    
    # get by NumDocEntete
    @classmethod
    def getByNumDocEntete(cls, db: Session, NumDocEntete: str):
        return db.query(cls).filter_by(NumDocEntete=NumDocEntete).first()
    
    # get all
    @classmethod
    def getAll(cls, db: Session):
        return db.query(cls).all()
    
    # create
    @classmethod
    def create(cls, db: Session, doc_entete):
        db.add(doc_entete)
        db.commit()
        db.refresh(doc_entete)
        return doc_entete
    
    # update
    @classmethod
    def update(cls, db: Session, doc_entete):
        db.add(doc_entete)
        db.commit()
        db.refresh(doc_entete)
        return doc_entete
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDDocEntete: int):
        # get by IDDocEntete
        doc_entete = DocEntete.get(db, IDDocEntete)
        # delete if exists
        if doc_entete:
            db.delete(doc_entete)
            db.commit()
            return True
        return False