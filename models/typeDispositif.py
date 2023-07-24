from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
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
            db.refresh(type_dispositif)
        # Return the 'type_dispositif' object
        return type_dispositif
    
    # delete method
    @classmethod
    def delete(cls, db: Session, type_dispositif_id: int):
        # Get the type_dispositif
        type_dispositif = cls.get(db, type_dispositif_id)
        if type_dispositif:
            db.delete(type_dispositif)
            db.commit()
            return True
        return False

    # update LibelleTypeDispo method
    @classmethod
    def updateLibelleTypeDispo(cls, db: Session, type_dispositif_id: int, LibelleTypeDispo: str):
        # Use a single query to update the LibelleType for all records with the given type_dispositif_id
        updated_count = db.query(cls).filter_by(IDTypeDispositif=type_dispositif_id).update({"LibelleTypeDispo": LibelleTypeDispo})
        
        # Commit the changes to the database
        db.commit()
        
        # Return the updated object
        return cls.get(db, type_dispositif_id)
    
    # update
    @classmethod
    def update(cls, db: Session, type_dispositif):
        # Add the new type_dispositif to the database session
        db.add(type_dispositif)
        # Commit the changes to the database
        db.commit()
        # Refresh the type_dispositif object with the latest data from the database
        db.refresh(type_dispositif)
        # Return the updated type_dispositif object
        return type_dispositif
