from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base
from sqlalchemy.orm import Session

class TypePanneau(Base):
    __tablename__ = "TypePanneau"

    # Clé primaire, Identifiant Unique
    IDTypePanneau = Column(Integer, primary_key=True)

    # Clé unique
    CodeTypePanneau = Column(String(6), nullable=False, unique=True)

    # Libelle 
    LibelleType = Column(String(64))

    # UpdatedAt
    UpdatedAt = Column(DateTime)

    # CreatedAt
    CreatedAt = Column(DateTime)

    # get method
    @classmethod
    def get(cls, db: Session, type_panneau_id: int):
        return db.query(cls).filter_by(IDTypePanneau=type_panneau_id).first()

    # get all method
    @classmethod
    def getAll(cls, db: Session):
        return db.query(cls).all()
   
    # get by codeTypePanneau
    @classmethod
    def getByCode(cls, db: Session, codeTypePanneau: str):
        return db.query(cls).filter_by(CodeTypePanneau=codeTypePanneau).first()
    
    # create method
    @classmethod
    def create(cls, db: Session, type_panneau):
        # set CreatedAt and UpdatedAt
        type_panneau.CreatedAt = type_panneau.UpdatedAt = datetime.now()
        # Add the 'type_panneau' object to the database session
        db.add(type_panneau)
        db.commit()
        db.refresh(type_panneau)
        return type_panneau

    # update
    @classmethod
    def update(cls, db: Session, type_panneau: 'TypePanneau'):
        # set UpdatedAt
        type_panneau.UpdatedAt = datetime.now()
        # Add the 'type_panneau' object to the database session
        db.add(type_panneau)
        db.commit()
        db.refresh(type_panneau)
        return type_panneau

    # delete method
    @classmethod
    def delete(cls, db: Session, type_panneau_id: int):
        # Create a query to retrieve all records in the table that have the given type_panneau_id
        query = db.query(cls).filter_by(IDTypePanneau=type_panneau_id)
        
        # Execute the query and delete all the retrieved records
        deleted_count = query.delete()
        
        # Commit the changes to the database
        db.commit()

        # Return True to indicate that the delete was successful
        return True

    # update method
    @classmethod
    def updateLibelleType(cls, db: Session, type_panneau_id: int, libelleType: str):
        # Use a single query to update the LibelleType for all records with the given type_panneau_id
        updated_count = db.query(cls).filter_by(IDTypePanneau=type_panneau_id).update({"LibelleType": libelleType})

        # Commit the changes to the database
        db.commit()

        # Return the updated object
        return cls.get(db, type_panneau_id)
