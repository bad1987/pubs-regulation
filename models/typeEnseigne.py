from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from db.Connexion import Base

class TypeEnseigne(Base):
    __tablename__ = "TypeEnseigne"

    # Clé primaire, identifiant unique
    IDTypeEnseigne = Column(Integer, primary_key=True)

    # Clé unique
    CodeTypeEnseigne = Column(String(9), nullable=False, unique=True)

    # Libellé
    LibelleTypeEnseigne = Column(String(64))

    # get method
    @classmethod
    def get(cls, db: Session, type_enseigne_id: int):
        return db.query(cls).filter_by(IDTypeEnseigne=type_enseigne_id).first()
    
    # get all method
    @classmethod
    def getAll(cls, db: Session):
        return db.query(cls).all()
    
    # get by codeTypeEnseigne
    @classmethod
    def getByCode(cls, db: Session, codeTypeEnseigne: str):
        return db.query(cls).filter_by(CodeTypeEnseigne=codeTypeEnseigne).first()
    
    # create method
    @classmethod
    def create(cls, db: Session, type_enseigne):
        # Begin a transaction with the database
        with db.begin():
            # Add the 'type_enseigne' object to the database session
            db.add(type_enseigne)
            # Flush the session to persist the changes to the database
            db.flush()
        # Return the 'type_enseigne' object
        return type_enseigne
    
    # delete method
    @classmethod
    def delete(cls, db: Session, type_enseigne_id: int):
        # Create a query to retrieve all records in the table that have the given type_enseigne_id
        query = db.query(cls).filter_by(IDTypeEnseigne=type_enseigne_id)
        
        # Execute the query and delete all the retrieved records
        deleted_count = query.delete()
        
        # Commit the changes to the database
        db.commit()
        
        # Return True to indicate that the delete was successful
        return True
    
    # update LibelleTypeEnseigne method
    @classmethod
    def updateLibelleTypeEnseigne(cls, db: Session, type_enseigne_id: int, LibelleTypeEnseigne: str):
        # Use a single query to update the LibelleType for all records with the given type_enseigne_id
        updated_count = db.query(cls).filter_by(IDTypeEnseigne=type_enseigne_id).update({"LibelleTypeEnseigne": LibelleTypeEnseigne})
        
        # Commit the changes to the database
        db.commit()
        
        # Return the updated object
        return cls.get(db, type_enseigne_id)
    
    # to string method
    def __repr__(self):
        return f"TypeEnseigne(IDTypeEnseigne={self.IDTypeEnseigne}, CodeTypeEnseigne={self.CodeTypeEnseigne}, LibelleTypeEnseigne={self.LibelleTypeEnseigne})"
    