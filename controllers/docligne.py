from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.docligne import DocLigne
from models.produitConcession import ProduitConcession
from models.campagne import CampagnePub

from schemas.DocLigneSchema import DocLigneSchema, DocLigneCreateSchema, DocLigneUpdateSchema

class DocLigneController:
    # get
    @classmethod
    def get(cls, db: Session, IDDocLigne: int) -> DocLigneSchema:
        try:
            docligne = DocLigne.get(db, IDDocLigne)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not docligne:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DocLigne not found")
        return DocLigneSchema.model_validate(docligne)
    
    # get by IDDocEntete
    @classmethod
    def getByIDDocEntete(cls, db: Session, IDDocEntete: int) -> list[DocLigneSchema]:
        try:
            docligne = DocLigne.get_by_id_doc_entete(db, IDDocEntete)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not docligne:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DocLigne not found")
        return DocLigneSchema.model_validate(docligne)
    
    # get all
    @classmethod
    def getAll(cls, db: Session) -> list[DocLigneSchema]:
        try:
            return [DocLigneSchema.model_validate(docligne) for docligne in DocLigne.get_all(db)]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # create
    @classmethod
    def create(cls, db: Session, docligne: DocLigneCreateSchema) -> DocLigneSchema:
        # check if IDDocEntete exists
        docentete = DocLigne.get_by_id_doc_entete(db, docligne.IDDocEntete)
        if not docentete:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid foreign key {docligne.IDDocEntete}")
        # check if IDCampagnePub exists
        campagne_pub = CampagnePub.get(db, docligne.IDCampagnePub)
        if not campagne_pub:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid foreign key {docligne.IDCampagnePub}")
        # check if IDProduitConcession exists
        produit_concession = ProduitConcession.get(db, docligne.IDProduitConcession)
        if not produit_concession:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid foreign key {docligne.IDProduitConcession}")
        try:
            docligne = DocLigne(**docligne.model_dump())
            docligne.doc_entete = docentete
            docligne.campagne_pub = campagne_pub
            docligne.produit = produit_concession
            docligne = DocLigne.create(db, docligne)
            return DocLigneSchema.model_validate(docligne)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # update
    @classmethod
    def update(cls, db: Session, updateDocLigne: DocLigneUpdateSchema) -> DocLigneSchema:
        # check if IDDocLigne exists
        try:
            doc_ligne = DocLigne.get(db, updateDocLigne.IDDocLigne)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not doc_ligne:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"DocLigne not found")
        try:
            update_data = updateDocLigne.model_dump(exclude_unset=True)
            for key,value in update_data.items():
                setattr(doc_ligne, key, value)
            doc_ligne = DocLigne.update(db, doc_ligne)
            return DocLigneSchema.model_validate(doc_ligne)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # delete
    @classmethod
    def delete(cls, db: Session, IDDocLigne: int) -> bool:
        try:
            doc_ligne = DocLigne.get(db, IDDocLigne)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not doc_ligne:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"DocLigne not found")
        try:
            return DocLigne.delete(db, IDDocLigne)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    