from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.Connexion import Base
from sqlalchemy.orm import Session

class TaxTiersDocEntete(Base):
    __tablename__ = "TaxTiersDocEntete"

    # Clé primaire
    IDTiersDocEntete = Column(Integer, primary_key=True)

    # Taux de taxe du tiers sur le document Entete
    TauxTaxeTiersDocEnt = Column(Float)

    # Clé Etrangère, identifiant unique de la table tiers
    IDTiers = Column(Integer, ForeignKey("Tiers.IDTiers"))

    # Clé étrangère, identifiant unique de la table Taxes
    IDTaxes = Column(Integer, ForeignKey("Taxes.IDTaxes"))

    # Clé étrangère, identifiant unique du DocEntete associé
    IDDocEntete = Column(Integer, ForeignKey("DocEntete.IDDocEntete"))

    # Relation avec la table TIERS
    tiers = relationship("Tiers", backref="taxes_doc_entete", lazy="joined")

    # Relation avec la table Taxes
    taxe = relationship("Taxes", backref="taxes_doc_entete", lazy="joined")

    # Relation avec la table DocEntete
    doc_entete = relationship("DocEntete", backref="taxes_doc_entete", lazy="joined")

    # get 
    @classmethod
    def get(cls, db: Session, IDTiersDocEntete: int):
        return db.query(cls).filter(cls.IDTiersDocEntete == IDTiersDocEntete).first()
    
    # get All
    @classmethod
    def getAll(cls, db: Session):
        return db.query(cls).all()
    
    # get By IDTiers
    @classmethod
    def getByIDTiers(cls, db: Session, IDTiers: int):
        return db.query(cls).filter_by(IDTiers=IDTiers).first()
    
    # get By IDTaxes
    @classmethod
    def getByIDTaxes(cls, db: Session, IDTaxes: int):
        return db.query(cls).filter_by(IDTaxes=IDTaxes).first()
    
    # create
    @classmethod
    def create(cls, db: Session, tax_tiers_doc_entete):
        db.add(tax_tiers_doc_entete)
        db.commit()
        db.refresh(tax_tiers_doc_entete)
        return tax_tiers_doc_entete
    
    # update
    @classmethod
    def update(cls, db: Session, tax_tiers_doc_entete_id: int, taux_tax_tiers_doc_entete: float):
        db.query(cls).filter(cls.IDTiersDocEntete == tax_tiers_doc_entete_id).update({"TauxTaxeTiersDocEnt": taux_tax_tiers_doc_entete})
        db.commit()

        return cls.get(db, tax_tiers_doc_entete_id)
    
    # delete
    @classmethod
    def delete(cls, db: Session, tax_tiers_doc_entete_id: int):
        db.query(cls).filter(cls.IDTiersDocEntete == tax_tiers_doc_entete_id).delete()
        db.commit()

        return True