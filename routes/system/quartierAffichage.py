import asyncio
from fastapi import APIRouter, Depends, status
from fastapi.params import Body, Path, Query
from sqlalchemy.orm import Session
from controllers.quartierAffichage import QuartierAffichageController
from dependencies.db_dependencies import get_db

from schemas.QuartierAffichageSchema import QuartierAffichageSchema, QuartierAffichageCreateSchema, QuartierAffichageUpdateSchema

router = APIRouter(
    tags=["QuartierAffichage"],
)

@router.get("/quartierAffichages", response_model=list[QuartierAffichageSchema], status_code=status.HTTP_200_OK)
async def get_all_quartier_affichages(db: Session = Depends(get_db)):
    return await asyncio.to_thread(QuartierAffichageController.getAll, db)

# get by NomQuartier
@router.get("/quartierAffichages/nomQuartier", response_model=QuartierAffichageSchema, status_code=status.HTTP_200_OK)
async def get_quartier_affichage_by_nom_quartier(NomQuartier: str = Query(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(QuartierAffichageController.get_by_nom_quartier, db, NomQuartier)

@router.get("/quartierAffichages/{quartierAffichage_id}", response_model=QuartierAffichageSchema, status_code=status.HTTP_200_OK)
async def get_quartier_affichage_by_id(quartierAffichage_id: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(QuartierAffichageController.get, db, quartierAffichage_id)


@router.post("/quartierAffichages", response_model=QuartierAffichageSchema, status_code=status.HTTP_201_CREATED)
async def create_quartier_affichage(NomQuartier: str = Body(...), SousQuartierAffich: str = Body(...), ObservationsQuartier: str = Body(...), ArrondissementQuartier: str = Body(...), IDZoneAffichage: int = Body(...), db: Session = Depends(get_db)):
    quartierAffichage = QuartierAffichageCreateSchema(NomQuartier=NomQuartier, SousQuartierAffich=SousQuartierAffich, ObservationsQuartier=ObservationsQuartier, ArrondissementQuartier=ArrondissementQuartier, IDZoneAffichage=IDZoneAffichage)
    return await asyncio.to_thread(QuartierAffichageController.create, db, quartierAffichage)

@router.put("/quartierAffichages/{quartierAffichage_id}", response_model=QuartierAffichageSchema, status_code=status.HTTP_200_OK)
async def update_quartier_affichage(quartierAffichage_id: int = Path(...), quartier: QuartierAffichageUpdateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(QuartierAffichageController.update, db, quartierAffichage_id, quartier)

@router.patch("/quartierAffichages/{quartierAffichage_id}", response_model=QuartierAffichageSchema, status_code=status.HTTP_200_OK)
async def update_quartier_affichage(quartierAffichage_id: int = Path(...), quartier: QuartierAffichageUpdateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(QuartierAffichageController.update, db, quartierAffichage_id, quartier)

@router.delete("/quartierAffichages/{quartierAffichage_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_quartier_affichage(quartierAffichage_id: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(QuartierAffichageController.delete, db, quartierAffichage_id)