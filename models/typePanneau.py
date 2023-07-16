from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base
from sqlalchemy.orm import Session

from models.panneauAffiche import PanneauAffich

class TypePanneau(Base):
    __tablename__ = "TypePanneau"

    # Clé primaire, Identifiant Unique
    IDTypePanneau = Column(Integer, primary_key=True)

    # Clé unique
    CodeTypePanneau = Column(String(6), nullable=False, unique=True)

    # Libelle 
    LibelleType = Column(String(64))

    # Relation avec la table PanneauAffich
    panneaux = relationship(PanneauAffich.__name__, back_populates="type_panneau", lazy="joined", cascade="save-update, merge")

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
        # Begin a transaction with the database
        with db.begin():
            # Add the 'type_panneau' object to the database session
            db.add(type_panneau)
            # Flush the session to persist the changes to the database
            db.flush()
        # Return the 'type_panneau' object
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
