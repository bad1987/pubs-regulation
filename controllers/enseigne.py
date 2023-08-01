
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.enseignes import Enseigne
from models.typeEnseigne import TypeEnseigne
from models.dispositifs import DispositifPub
from models.typeDispositif import TypeDispositif
from models.emplacementAffichage import EmplacementAffichage
from models.tiers import Tiers

from schemas.EnseigneSchema import EnseigneSchema, EnseigneUpdateSchema, EnseigneCreateSchema

class EnseigneController:
    # get
    @classmethod
    def get(cls, db: Session, IDEnseigne: int) -> EnseigneSchema:
        try:
            enseigne = Enseigne.get(db, IDEnseigne)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not enseigne:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Enseigne not found")
        return EnseigneSchema.model_validate(enseigne)
    
    # get by CodeEnseigne
    @classmethod
    def get_by_code(cls, db: Session, CodeEnseigne: str) -> EnseigneSchema:
        try:
            enseigne = Enseigne.get_by_code(db, CodeEnseigne)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not enseigne:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Enseigne not found")
        return EnseigneSchema.model_validate(enseigne)
    
    # get all
    @classmethod
    def get_all(cls, db: Session) -> list[EnseigneSchema]:
        try:
            enseignes = Enseigne.get_all(db)
            return [EnseigneSchema.model_validate(enseigne) for enseigne in enseignes]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # create
    @classmethod
    def create(cls, db: Session, enseigne: EnseigneCreateSchema) -> EnseigneSchema:
        # check if codeEnseigne is unique
        if Enseigne.get_by_code(db, enseigne.CodeEnseigne):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="CodeEnseigne already exists")
        # check CodeDispositifPub is unique
        if DispositifPub.get_by_code(db, enseigne.CodeDispositifPub):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="CodeDispositifPub already exists")
        # check if foreign key IDEmplacementAffichage is valid
        emplacementAffichage = EmplacementAffichage.get(db, enseigne.IDEmplacementAffichage)
        if not emplacementAffichage:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EmplacementAffichage not found")
        # check if foreign key IDTiers is valid
        tiers = Tiers.get(db, enseigne.IDTiers)
        if not tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tiers not found")
        # check if the foreign key IDTypeEnseigne is valid
        typeEnseigne = TypeEnseigne.get(db, enseigne.IDTypeEnseigne)
        if not typeEnseigne:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TypeEnseigne not found")
        # check if the foreign key IDTypeDispositif is valid
        type_dispositif = TypeDispositif.get(db, enseigne.IDTypeDispositif)
        if not type_dispositif:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TypeDispositif not found")
        
        try:
            enseigne = Enseigne(**enseigne.model_dump())
            enseigne.type_dispositif = type_dispositif
            enseigne.type_enseigne = typeEnseigne
            enseigne.emplacement_affichage = emplacementAffichage
            enseigne.tiers = tiers
            enseigne = Enseigne.create(db, enseigne)
            return EnseigneSchema.model_validate(enseigne)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # update
    @classmethod
    def update(cls, db: Session, updateEnseigne: EnseigneUpdateSchema) -> EnseigneSchema:
        enseigne = Enseigne.get(db, updateEnseigne.IDEnseigne)
        if not enseigne:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Enseigne not found")
        try:
            update_data = updateEnseigne.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(enseigne, key, value)
            enseigne = Enseigne.update(db, enseigne)
            return EnseigneSchema.model_validate(enseigne)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # delete
    @classmethod
    def delete(cls, db: Session, IDEnseigne: int) -> bool:
        try:
            enseigne = Enseigne.get(db, IDEnseigne)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not enseigne:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Enseigne not found")
        try:
            return Enseigne.delete(db, IDEnseigne)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        