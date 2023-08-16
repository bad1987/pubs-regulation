from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from db.Connexion import Base

class TypeTiers(Base):
    __tablename__ = "TypeTiers"
    IDTypeTiers = Column(Integer, primary_key=True)
    LibelleTypeTiers = Column(String(255), unique=True)

    # get method
    @classmethod
    def get(cls, db: Session, IDTypeTiers: int):
        return db.query(cls).filter_by(IDTypeTiers=IDTypeTiers).first()
    
    # get all
    @classmethod
    def getAll(cls, db: Session):
        return db.query(cls).all()
    
    # create
    @classmethod
    def create(cls, db: Session, type_tiers):
        db.add(type_tiers)
        db.commit()
        db.refresh(type_tiers)
        return type_tiers
    
    # update libelle
    @classmethod
    def updateLibelleType(cls, db: Session, type_tiers: int, libelleType: str):
        query = db.query(cls).filter_by(IDTypeTiers=type_tiers).update({"LibelleTypeTiers": libelleType})
        db.commit()

        # Return the updated object
        return cls.get(db, type_tiers)
    
    # delete
    @classmethod
    def delete(cls, db: Session, type_tiers: int):
        query = db.query(cls).filter_by(IDTypeTiers=type_tiers).delete()
        db.commit()
        
        return True

class Tiers(Base):
    __tablename__ = "Tiers"

    # Clé primaire, identifiant unique de la table
    IDTiers = Column(Integer, primary_key=True)

    # Clé unique, Code Tiers
    CodeTiers = Column(String(20), nullable=False, unique=True)

    # Libelle tiers
    LibelleTiers = Column(String(64))

    # Adresse
    AdresseTiers = Column(String(128))

    # Téléphone
    TelephoneTiers = Column(Integer)

    # UpdatedAt
    UpdatedAt = Column(DateTime)

    # CreatedAt
    CreatedAt = Column(DateTime)

    # Type de tiers Cle etrangere (Régisseur, Régulateur, Annonceur, etc…)  
    IDTypeTiers = Column(Integer, ForeignKey("TypeTiers.IDTypeTiers", ondelete="CASCADE"))

    # N° Contribuable
    NumCont = Column(String(22))

    # Adresse E-mail
    EmailTiers = Column(String(65))

    # Logo du tiers, cas  des régisseurs
    Logo = Column(String(255), nullable=True)

    # Sigle
    SigleTiers = Column(String(20))

    # Relation avec la table TypeTiers
    type_tiers = relationship("TypeTiers", backref="tiers", lazy="joined", cascade="save-update, merge")

    # get method
    @classmethod
    def get(cls, db: Session, type_tiers_id: int):
        return db.query(cls).filter_by(IDTiers=type_tiers_id).first()
    
    # get by code method
    @classmethod
    def getByCode(cls, db: Session, codeTiers: str):
        return db.query(cls).filter_by(CodeTiers=codeTiers).first()

    # get all method
    @classmethod
    def getAll(cls, db: Session):
        return db.query(cls).all()
    
    # create method
    @classmethod
    def create(cls, db: Session, tiers):
        # set CreatedAt and UpdatedAt
        tiers.CreatedAt = tiers.UpdatedAt = datetime.now()
        db.add(tiers)
        db.commit()
        db.refresh(tiers)
        return tiers
    
    # delete method
    @classmethod
    def delete(cls, db: Session, tiers_id: int):
        # Create a query to retrieve all records in the table that have the given type_panneau_id
        query = db.query(cls).filter_by(IDTiers=tiers_id)
        
        # Execute the query and delete all the retrieved records
        deleted_count = query.delete()
        
        # Commit the changes to the database
        db.commit()
        
        # Return True to indicate that the delete was successful
        return True
    
    # update N° Contribuable method
    @classmethod
    def updateNumCont(cls, db: Session, tiers_id: int, numCont: str):
        # Create a query to retrieve all records in the table that have the given type_panneau_id
        query = db.query(cls).filter_by(IDTiers=tiers_id)
        
        # Execute the query and delete all the retrieved records
        updated_count = query.update({"NumCont": numCont})
        
        # Commit the changes to the database
        db.commit()
        
        # Return the updated tiers object
        return cls.get(db, tiers_id)
    
    # update LibelleTiers method
    @classmethod
    def updateLibelleTiers(cls, db: Session, tiers_id: int, libelleTiers: str):
        # Create a query to retrieve all records in the table that have the given type_panneau_id
        query = db.query(cls).filter_by(IDTiers=tiers_id)
        
        # Execute the query and delete all the retrieved records
        updated_count = query.update({"LibelleTiers": libelleTiers})
        
        # Commit the changes to the database
        db.commit()
        
        # Return the updated tiers object
        return cls.get(db, tiers_id)
    
    # update AdresseTiers method
    @classmethod
    def updateAdresseTiers(cls, db: Session, tiers_id: int, adresseTiers: str):
        # Create a query to retrieve all records in the table that have the given type_panneau_id
        query = db.query(cls).filter_by(IDTiers=tiers_id)
        
        # Execute the query and delete all the retrieved records
        updated_count = query.update({"AdresseTiers": adresseTiers})
        
        # Commit the changes to the database
        db.commit()
        
        # Return the updated tiers object
        return cls.get(db, tiers_id)
    
    # update SigleTiers method
    @classmethod
    def updateSigleTiers(cls, db: Session, tiers_id: int, sigleTiers: str):
        # Create a query to retrieve all records in the table that have the given type_panneau_id
        query = db.query(cls).filter_by(IDTiers=tiers_id)
        
        # Execute the query and delete all the retrieved records
        updated_count = query.update({"SigleTiers": sigleTiers})
        
        # Commit the changes to the database
        db.commit()
        
        # Return the updated tiers object
        return cls.get(db, tiers_id)
    
    # update logo method
    @classmethod
    def updateLogo(cls, db: Session, tiers_id: int, logo: str):
        # Create a query to retrieve all records in the table that have the given type_panneau_id
        query = db.query(cls).filter_by(IDTiers=tiers_id)
        
        # Execute the query and delete all the retrieved records
        updated_count = query.update({"Logo": logo})
        
        # Commit the changes to the database
        db.commit()
        
        # Return the updated tiers object
        return cls.get(db, tiers_id)

    # update method
    @classmethod
    def update(cls, db: Session, tiers):
        # set UpdatedAt
        tiers.UpdatedAt = datetime.now()
        db.add(tiers)
        db.commit()
        db.refresh(tiers)
        return tiers