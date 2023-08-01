from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.docentete import DocEntete
from models.tiers import Tiers
from schemas.DocEnteteSchema import DocEnteteSchema, DocEnteteCreateSchema, DocEnteteUpdateSchema

class DocEnteteController:
    # get
    @classmethod
    def get(cls, db: Session, IDDocEntete: int) -> DocEnteteSchema:
        try:
            doc_entete = DocEntete.get(db, IDDocEntete)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not doc_entete:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DocEntete not found")
        return DocEnteteSchema.model_validate(doc_entete)
    
    # get by NumDocEntete
    @classmethod
    def getByNumDocEntete(cls, db: Session, NumDocEntete: str) -> DocEnteteSchema:
        try:
            doc_entete = DocEntete.getByNumDocEntete(db, NumDocEntete)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not doc_entete:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DocEntete not found")
        return DocEnteteSchema.model_validate(doc_entete)
    
    # get all
    @classmethod
    def getAll(cls, db: Session) -> list[DocEnteteSchema]:
        try:
            return [DocEnteteSchema.model_validate(doc_entete) for doc_entete in DocEntete.getAll(db)]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # create
    @classmethod
    def create(cls, db: Session, doc_entete: DocEnteteCreateSchema) -> DocEnteteSchema:
        # check if NumDocEntete is unique
        if DocEntete.getByNumDocEntete(db, doc_entete.NumDocEntete):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="DocEntete already exists")
        # check if IDTiers exists
        tiers = Tiers.get(db, doc_entete.IDTiers)
        if not tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid foreign key {doc_entete.IDTiers}")
        try:
            doc_entete = DocEntete(**doc_entete.model_dump())
            doc_entete.tiers = tiers
            doc_entete = DocEntete.create(db, doc_entete)
            return DocEnteteSchema.model_validate(doc_entete)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # update
    @classmethod
    def update(cls, db: Session, IDDocEntete: int, updateDocEntete: DocEnteteCreateSchema) -> DocEnteteSchema:
        try:
            doc_entete = DocEntete.get(db, IDDocEntete)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not doc_entete:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DocEntete not found")
        try:
            update_data = updateDocEntete.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(doc_entete, key, value)
            doc_entete = DocEntete.update(db, updateDocEntete)
            return DocEnteteSchema.model_validate(doc_entete)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDDocEntete: int) -> bool:
        try:
            doc_entete = DocEntete.get(db, IDDocEntete)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not doc_entete:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DocEntete not found")
        try:
            return DocEntete.delete(db, IDDocEntete)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))