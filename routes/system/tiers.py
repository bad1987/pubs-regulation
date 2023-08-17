import asyncio
from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.params import Body, Path, Query
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from dependencies.db_dependencies import get_db

from controllers.tiers import TiersController
from schemas.TiersSchema import TiersSchema, TiersCreateSchema, TiersUpdateSchema, TypeTiersSchema

router = APIRouter(
    tags=["Tiers"],
)

# get by codeTiers
@router.get("/tiers/code", response_model=TiersSchema, status_code=status.HTTP_200_OK)
async def get_tiers_by_code(CodeTiers: str = Query(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TiersController.getByCode, db, CodeTiers)

# get all type tiers
@router.get("/tiers/type", response_model=list[TypeTiersSchema], status_code=status.HTTP_200_OK)
async def get_all_type_tiers(db: Session = Depends(get_db)):
    return await asyncio.to_thread(TiersController.getAllTypeTiers, db)

# get tiers logo
@router.get("/tiers/{tiers_id}/logo", response_class=FileResponse, status_code=status.HTTP_200_OK)
async def get_tiers_logo(tiers_id: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TiersController.getLogo, db, tiers_id)

@router.get("/tiers/{tiers_id}", response_model=TiersSchema, status_code=status.HTTP_200_OK)
async def get_tiers_by_id(tiers_id: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TiersController.get, db, tiers_id)


@router.get("/tiers", response_model=list[TiersSchema], status_code=status.HTTP_200_OK)
async def get_all_tiers(db: Session = Depends(get_db)):
    return await asyncio.to_thread(TiersController.getAll, db)

@router.post("/tiers", response_model=TiersSchema, status_code=status.HTTP_201_CREATED)
async def create_tiers(tiers: TiersCreateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TiersController.create, db, tiers)

@router.put("/tiers/{tiers_id}", response_model=TiersSchema, status_code=status.HTTP_200_OK)
async def update_tiers(tiers_id: int = Path(...), tiers: TiersUpdateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TiersController.update, db, tiers_id, tiers)

# update Logo
@router.put("/tiers/{tiers_id}/logo", response_model=TiersSchema, status_code=status.HTTP_200_OK)
async def update_logo(tiers_id: int = Path(...), logo: UploadFile = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TiersController.updateLogo, db, tiers_id, logo)

@router.patch("/tiers/{tiers_id}", response_model=TiersSchema, status_code=status.HTTP_200_OK)
async def update_tiers(tiers_id: int = Path(...), tiers: TiersUpdateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TiersController.update, db, tiers_id, tiers)

@router.delete("/tiers/{tiers_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tiers(tiers_id: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(TiersController.delete, db, tiers_id)
