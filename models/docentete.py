from datetime import datetime
from sqlalchemy import Column, DateTime, Enum, Integer, String, Date, Float, ForeignKey, CHAR
from sqlalchemy.orm import relationship, Session
from Enums.TypeDocEnteteENum import TypeDocEnteteENum
from db.Connexion import Base

class DocEntete(Base):
    __tablename__ = "DocEntete"

    # Clé primaire, Identifiant unique de la table DocEntete
    IDDocEntete = Column(Integer, primary_key=True)

    # Type de document de type Integer, ici la codification peut être 1 pour l’Enrôlement, 2 pour la Commande, 3 pour une Facture Doit, 4 pour une Facture d’Avoir
    # Take its values from TypeDocEnteteENum
    TypeDocEntete = Column(Integer, nullable=False)

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

    # UpdatedAt
    UpdatedAt = Column(DateTime)

    # CreatedAt
    CreatedAt = Column(DateTime)

    # Clé étrangère, identifiant unique de la table Tiers
    IDTiers = Column(Integer, ForeignKey("Tiers.IDTiers", ondelete="CASCADE"))

    # Relation avec la table Tiers
    tiers = relationship("Tiers", backref="documents", lazy="joined", cascade="save-update, merge")

    """
    Generate NumDocEntete automatically.
    it should start with DOC, the next 2 digits should be the year's last 2 digits and theremaining 4 digits should be incremental starting from the last generated one plus one
    for the last part, given that it is 4 digits, i should have something like 0001,0002,0003,etc
    """
    @classmethod
    def generateNumDocEntete(cls, db: Session):
        # get the current year's last 2 digits
        year = str(datetime.now().year)[-2:]

        # Query the database to get the last generated NumDocEntete
        lastGeneratedNumDocEntete: DocEntete = db.query(cls).order_by(cls.IDDocEntete.desc()).first()

        # extract the last 5 digits from the last generated NumDocEntete
        if lastGeneratedNumDocEntete:
            # check if the year in the last generated code matches the current year
            if lastGeneratedNumDocEntete.NumDocEntete[2:4] == year:
                # increment the four digits by one
                lastGeneratedNumDocEntete = lastGeneratedNumDocEntete.NumDocEntete[-5:]
                lastGeneratedNumDocEntete = str(int(lastGeneratedNumDocEntete) + 1).zfill(5)
            else:
                # reset the four digits to "00001"
                lastGeneratedNumDocEntete = "00001"
        else:
            # use "00001" as the default value
            lastGeneratedNumDocEntete = "00001"
        
        return "DO" + year + lastGeneratedNumDocEntete

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
    def create(cls, db: Session, doc_entete: 'DocEntete') -> 'DocEntete':
        # Generate the NumDocEntete automatically
        doc_entete.NumDocEntete = cls.generateNumDocEntete(db)
        # set the DateDocEntete
        doc_entete.DateDocEntete = datetime.utcnow().isoformat()
        # set the UpdatedAt
        doc_entete.UpdatedAt = datetime.utcnow().isoformat()
        # set CreatedAt
        doc_entete.CreatedAt = datetime.utcnow().isoformat()
        db.add(doc_entete)
        db.commit()
        db.refresh(doc_entete)
        return doc_entete
    
    # update
    @classmethod
    def update(cls, db: Session, doc_entete):
        # set the UpdatedAt
        doc_entete.UpdatedAt = datetime.utcnow().isoformat()
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