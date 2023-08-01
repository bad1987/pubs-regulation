from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.repDoc import RepDoc
from schemas.repDocSchema import RepDocSchema, RepDocCreateSchema

class RepDocController:
    # get
    @classmethod
    def get(cls, db: Session, IDRepDoc: int) -> RepDocSchema:
        try:
            rep_doc = RepDoc.get(db, IDRepDoc)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not rep_doc:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RepDoc not found")
        return RepDocSchema.model_validate(rep_doc)

    # get all
    @classmethod
    def getAll(cls, db: Session) -> list[RepDocSchema]:
        try:
            return [RepDocSchema.model_validate(rep_doc) for rep_doc in RepDoc.getAll(db)]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # create
    @classmethod
    def create(cls, db: Session, rep_doc: RepDocCreateSchema) -> RepDocSchema:
        try:
            rep_doc = RepDoc.create(db, RepDoc(**rep_doc.model_dump()))
            return RepDocSchema.model_validate(rep_doc)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # update montantReparti
    @classmethod
    def updateMontantReparti(cls, db: Session, IDRepDoc: int, MontantReparti: float) -> RepDocSchema:
        try:
            rep_doc = RepDoc.get(db, IDRepDoc)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not rep_doc:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RepDoc not found")
        try:
            rep_doc = RepDoc.updateMontantReparti(db, IDRepDoc, MontantReparti)
            return RepDocSchema.model_validate(rep_doc)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDRepDoc: int) -> bool:
        try:
            rep_doc = RepDoc.get(db, IDRepDoc)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not rep_doc:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RepDoc not found")
        try:
            return RepDoc.delete(db, IDRepDoc)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))