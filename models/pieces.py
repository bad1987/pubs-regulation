from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Session
from db.Connexion import Base

class TypePiece(Base):
    __tablename__ = "TypePiece"

    IDTypePiece = Column(Integer, primary_key=True)
    LibelleTypePiece = Column(String(255))

    # get by ID
    @classmethod
    def get(cls, db: Session, IDTypePiece: int):
        return db.query(cls).filter_by(IDTypePiece=IDTypePiece).first()
    
    # get all
    @classmethod
    def getAll(cls, db: Session):
        return db.query(cls).all()
    
    # create
    @classmethod
    def create(cls, db: Session, type_piece):
        db.add(type_piece)
        db.commit()
        db.refresh(type_piece)
        return type_piece
    
    # update
    @classmethod
    def update(cls, db: Session, type_piece):
        db.add(type_piece)
        db.commit()
        db.refresh(type_piece)
        return type_piece
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDTypePiece):
        # get the object
        type_piece = cls.get(db, IDTypePiece)
        if type_piece:
            db.delete(type_piece)
            db.commit()
            return True
        return False

class Piece(Base):
    __tablename__ = "Piece"

    # Clé primaire, identifiant unique de la table
    IDPiece = Column(Integer, primary_key=True)

    # Clé unique numéro de la pièce
    NumPiece = Column(String(15), unique=True)

    # Date de création de la pièce
    DateEmmission = Column(DateTime)

    # UpdatedAt
    UpdatedAt = Column(DateTime)

    # CreatedAt
    CreatedAt = Column(DateTime)

    # Clé étrangère, identifiant unique de la table Règlement
    IDReglement = Column(Integer, ForeignKey("Reglement.IDReglement", ondelete="CASCADE"))

    # Clé etrangère, identifiant unique de la table TypePiece
    IDTypePiece = Column(Integer, ForeignKey("TypePiece.IDTypePiece", ondelete="CASCADE"))

    # Relation avec la table Reglement
    reglement = relationship("Reglement", backref="pieces", lazy="joined", cascade="save-update, merge")
    type_piece = relationship("TypePiece", backref="pieces", lazy="joined", cascade="save-update, merge")

    # get by ID
    @classmethod
    def get(cls, db: Session, IDPiece: int):
        return db.query(cls).filter_by(IDPiece=IDPiece).first()

    # get by NumPiece
    @classmethod
    def getByNum(cls, db: Session, NumPiece: str):
        return db.query(cls).filter_by(NumPiece=NumPiece).first()
    
    # get all
    @classmethod
    def getAll(cls, db: Session):
        return db.query(cls).all()
    
    # create
    @classmethod
    def create(cls, db: Session, piece):
        # set CreatedAt and UpdatedAt
        piece.CreatedAt = piece.UpdatedAt = datetime.now().isoformat()
        # set DateEmmission
        piece.DateEmmission = datetime.now().isoformat()
        db.add(piece)
        db.commit()
        db.refresh(piece)
        return piece
    
    # update
    @classmethod
    def update(cls, db: Session, piece):
        # set UpdatedAt
        piece.UpdatedAt = datetime.now().isoformat()
        db.add(piece)
        db.commit()
        db.refresh(piece)
        return piece
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDPiece):
        # get the object
        piece = cls.get(db, IDPiece)
        if piece:
            db.delete(piece)
            db.commit()
            return True
        return False