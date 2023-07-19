from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import relationship
from db.Connexion import Base
from sqlalchemy.orm import Session

class TypeDispositif(Base):
    __tablename__ = "TypeDispositif"

    # Clé primaire, identifiant unique
    IDTypeDispositif = Column(Integer, primary_key=True)

    # Clé unique
    CodeTypeDispositif = Column(String(6), nullable=False, unique=True)

    # Libellé
    LibelleTypeDispo = Column(String(25))
    
    # get method
    @classmethod
    def get(cls, db: Session, type_dispositif_id: int):
        return db.query(cls).filter_by(IDTypeDispositif=type_dispositif_id).first()

    # get all method
    @classmethod
    def getAll(cls, db: Session):
        return db.query(cls).all()
    
    # get by codeTypeDispositif
    @classmethod
    def getByCode(cls, db: Session, codeTypeDispositif: str):
        return db.query(cls).filter_by(CodeTypeDispositif=codeTypeDispositif).first()

    # create method
    @classmethod
    def create(cls, db: Session, type_dispositif):
        # Begin a transaction with the database
        with db.begin():
            # Add the 'type_dispositif' object to the database session
            db.add(type_dispositif)
            # Flush the session to persist the changes to the database
            db.flush()
        # Return the 'type_dispositif' object
        return type_dispositif
    
    # delete method
    @classmethod
    def delete(cls, db: Session, type_dispositif_id: int):
        # Create a query to retrieve all records in the table that have the given type_dispositif_id
        query = db.query(cls).filter_by(IDTypeDispositif=type_dispositif_id)
        
        # Execute the query and delete all the retrieved records
        deleted_count = query.delete()
        
        # Commit the changes to the database
        db.commit()
        
        # Return True to indicate that the delete was successful
        return True
    
    # update LibelleTypeDispo method
    @classmethod
    def updateLibelleTypeDispo(cls, db: Session, type_dispositif_id: int, LibelleTypeDispo: str):
        # Use a single query to update the LibelleType for all records with the given type_dispositif_id
        updated_count = db.query(cls).filter_by(IDTypeDispositif=type_dispositif_id).update({"LibelleTypeDispo": LibelleTypeDispo})
        
        # Commit the changes to the database
        db.commit()
        
        # Return the updated object
        return cls.get(db, type_dispositif_id)