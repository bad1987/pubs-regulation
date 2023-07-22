import asyncio
from fastapi import APIRouter, Depends, status
from fastapi.params import Body, Path, Query
from sqlalchemy.orm import Session
from dependencies.db_dependencies import get_db

from controllers.zoneAffichage import ZoneAffichageController
from schemas.ZoneAffichage import ZoneAffichageCreateSchema, ZoneAffichageSchema, ZoneAffichageUpdateSchema

router = APIRouter(
    tags=["ZoneAffichage"],
)

@router.get("/zoneAffichages", response_model=list[ZoneAffichageSchema], status_code=status.HTTP_200_OK)
async def get_all_zone_affichages(db: Session = Depends(get_db)):
    return await asyncio.to_thread(ZoneAffichageController.getAll, db)

@router.get("/zoneAffichages/codeZone", response_model=ZoneAffichageSchema, status_code=status.HTTP_200_OK)
async def get_zone_affichage_by_codeZone(codeZone: str = Query(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(ZoneAffichageController.getByCodeZone, db, codeZone)

@router.get("/zoneAffichages/{IDZoneAffichage}", response_model=ZoneAffichageSchema, status_code=status.HTTP_200_OK)
async def get_zone_affichage(IDZoneAffichage: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(ZoneAffichageController.get, db, IDZoneAffichage)

@router.post("/zoneAffichages", response_model=ZoneAffichageSchema, status_code=status.HTTP_201_CREATED)
async def create_zone_affichage(zoneAffichage: ZoneAffichageCreateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(ZoneAffichageController.create, db, zoneAffichage)

@router.put("/zoneAffichages/{IDZoneAffichage}", response_model=ZoneAffichageSchema, status_code=status.HTTP_200_OK)
async def update_zone_affichage(IDZoneAffichage: int = Path(...), zoneAffichage: ZoneAffichageUpdateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(ZoneAffichageController.update, db, IDZoneAffichage, zoneAffichage)

@router.delete("/zoneAffichages/{IDZoneAffichage}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_zone_affichage(IDZoneAffichage: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(ZoneAffichageController.delete, db, IDZoneAffichage)