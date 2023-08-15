import os
from fastapi import HTTPException, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from pathlib import Path

from models.tiers import Tiers, TypeTiers
from schemas.TiersSchema import TiersCreateSchema, TiersSchema, TypeTiersSchema

# set the path to the directory where the logo images will be stored
LOGO_DIR = Path(__file__).parent / "logos"

class TiersController:

    # get by id
    @classmethod
    def get(cls, db: Session, tiers_id: int) -> TiersSchema:
        tiers = Tiers.get(db, tiers_id)
        if not tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tiers not found")
        try:
            return TiersSchema.model_validate(tiers)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # get all
    @classmethod
    def getAll(cls, db: Session) -> list[TiersSchema]:
        try:
            return [TiersSchema.model_validate(tiers) for tiers in Tiers.getAll(db)]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # get by code
    @classmethod
    def getByCode(cls, db: Session, codeTiers: str) -> TiersSchema:
        tiers = Tiers.getByCode(db, codeTiers)
        if not tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tiers not found")
        try:
            return TiersSchema.model_validate(tiers)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # get the logo of a Tiers
    @classmethod
    def getLogo(cls, db: Session, tiers_id: int) -> FileResponse:
        try:
            tiers = Tiers.get(db, tiers_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tiers not found")
        try:
            logo_filename = tiers.Logo
            logo_path = LOGO_DIR / logo_filename
            return FileResponse(logo_path)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # create
    @classmethod
    def create(cls, db: Session, tiers: TiersCreateSchema) -> TiersSchema:
        # check if TypeTiers exist
        type_tiers = TypeTiers.get(db, tiers.IDTypeTiers)
        if not type_tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid TypeTiers")
        # check if CodeTiers is unique
        if Tiers.getByCode(db, tiers.CodeTiers):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="CodeTiers already exists")
        try:
            tiers_data = tiers.model_dump()
            if tiers.Logo is not None:
                # validate the uploaded logo file
                # check the file size (max 2MB)
                if tiers.Logo.size > 2*1024*1024:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Logo file size must be less than 2MB")
                # check the file extension
                allowed_extensions = [".png", ".jpg", ".jpeg"]
                _,ext = os.path.splitext(tiers.Logo.filename)
                if ext.lower() not in allowed_extensions:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid logo file extension")
                # save the uploaded logo file to the LOGO_DIR directory
                logo_filename = f"{tiers.CodeTiers}_{tiers.Logo.filename}"
                logo_path = LOGO_DIR / logo_filename
                with open(logo_path, "wb") as f:
                    f.write(tiers.Logo.read())
                tiers_data["Logo"] = logo_filename
            tiers = Tiers(**tiers_data)
            tiers.type_tiers = type_tiers
            tiers = Tiers.create(db, tiers)
            return TiersSchema.model_validate(tiers)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # update
    @classmethod
    def update(cls, db: Session, tiers_id: int, updateTiers: TiersCreateSchema) -> TiersSchema:
        try:
            tiers = Tiers.get(db, tiers_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tiers not found")
        try:
            update_data = updateTiers.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(tiers, key, value)
            tiers = Tiers.update(db, tiers)
            return TiersSchema.model_validate(tiers)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # update N° Contribuable method
    @classmethod
    def updateNumCont(cls, db: Session, tiers_id: int, numCont: str) -> TiersSchema:
        tiers = Tiers.get(db, tiers_id)
        if not tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tiers not found")
        try:
            tiers = Tiers.updateNumCont(db, tiers_id, numCont)
            return TiersSchema.model_validate(tiers)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # update LibelleTiers method
    @classmethod
    def updateLibelleTiers(cls, db: Session, tiers_id: int, libelleTiers: str) -> TiersSchema:
        tiers = Tiers.get(db, tiers_id)
        if not tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tiers not found")
        try:
            tiers = Tiers.updateLibelleTiers(db, tiers_id, libelleTiers)
            return TiersSchema.model_validate(tiers)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # update AdresseTiers method
    @classmethod
    def updateAdresseTiers(cls, db: Session, tiers_id: int, adresseTiers: str) -> TiersSchema:
        tiers = Tiers.get(db, tiers_id)
        if not tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tiers not found")
        try:
            tiers = Tiers.updateAdresseTiers(db, tiers_id, adresseTiers)
            return TiersSchema.model_validate(tiers)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # update SigleTiers method
    @classmethod
    def updateSigleTiers(cls, db: Session, tiers_id: int, sigleTiers: str)-> TiersSchema:
        tiers = Tiers.get(db, tiers_id)
        if not tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tiers not found")
        try:
            tiers = Tiers.updateSigleTiers(db, tiers_id, sigleTiers)
            return TiersSchema.model_validate(tiers)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # update Logo method
    @classmethod
    def updateLogo(cls, db: Session, tiers_id: int, logo: str) -> TiersSchema:
        tiers = Tiers.get(db, tiers_id)
        if not tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tiers not found")
        try:
            tiers = Tiers.updateLogo(db, tiers_id, logo)
            return TiersSchema.model_validate(tiers)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # delete
    @classmethod
    def delete(cls, db: Session, tiers_id: int) -> bool:
        tiers = Tiers.get(db, tiers_id)
        if not tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tiers not found")
        try:
            Tiers.delete(db, tiers_id)
            return True
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # get typeTiers by id
    @classmethod
    def getTypeTiers(cls, db: Session, typeTiers_id: int) -> TypeTiersSchema:
        type_tiers = TypeTiers.get(db, typeTiers_id)
        if not type_tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TypeTiers not found")
        try:
            return TiersSchema.model_validate(type_tiers)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # get all typeTiers
    @classmethod
    def getAllTypeTiers(cls, db: Session) -> list[TypeTiersSchema]:
        try:
            return [TypeTiersSchema.model_validate(type_tiers) for type_tiers in TypeTiers.getAll(db)]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    # create typeTiers
    @classmethod
    def createTypeTiers(cls, db: Session, type_tiers: TypeTiersSchema) -> TypeTiersSchema:
        try:
            type_tiers = TypeTiers.create(db, type_tiers)
            return TiersSchema.model_validate(type_tiers)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # delete typeTiers
    @classmethod
    def deleteTypeTiers(cls, db: Session, typeTiers_id: int) -> bool:
        type_tiers = TypeTiers.get(db, typeTiers_id)
        if not type_tiers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TypeTiers not found")
        try:
            TypeTiers.delete(db, typeTiers_id)
            return True
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    
    @classmethod
    def cleanup_logos(db: Session):
        # Get a list of all logo file names that are currently referenced by Tiers records
        referenced_logos = db.query(Tiers.Logo).filter(Tiers.Logo != None).all()
        referenced_logos = [logo[0] for logo in referenced_logos]

        # Get a list of all logo files stored on the server
        stored_logos = [f.name for f in LOGO_DIR.glob("*")]

        # Delete any logo files on the server that are not in the list of referenced file names
        for logo in stored_logos:
            if logo not in referenced_logos:
                (LOGO_DIR / logo).unlink()