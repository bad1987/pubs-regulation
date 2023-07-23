import asyncio
from fastapi import APIRouter, Depends, status
from fastapi.params import Body, Path, Query
from sqlalchemy.orm import Session
from dependencies.db_dependencies import get_db

from controllers.emplacementAffichage import EmplacementAffichageController
from schemas.EmplacementAffichageSchema import EmplacementAffichageSchema, EmplacementAffichageUpdateSchema, EmplacementAffichageCreateSchema

router = APIRouter(
    tags=["EmplacementAffichage"],
)

# get by CodeEmplacement
@router.get("/emplacementAffichage/code", response_model=EmplacementAffichageSchema, status_code=status.HTTP_200_OK, description="Get emplacementAffichage by CodeEmplacement")
async def get_by_code(CodeEmplacement: str = Query(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(EmplacementAffichageController.get_by_code, db, CodeEmplacement)

# get all by IDQuartierAffichage
@router.get("/emplacementAffichage/quartier", response_model=list[EmplacementAffichageSchema], status_code=status.HTTP_200_OK, description="Get all emplacementAffichage by IDQuartierAffichage")
async def get_all_by_IDQuartierAffichage(IDQuartierAffichage: int = Query(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(EmplacementAffichageController.get_all_by_IDQuartierAffichage, db, IDQuartierAffichage)

# get by ID
@router.get("/emplacementAffichage/{IDEmplacementAffichage}", response_model=EmplacementAffichageSchema, status_code=status.HTTP_200_OK, description="Get emplacementAffichage by ID")
async def get_by_ID(IDEmplacementAffichage: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(EmplacementAffichageController.get, db, IDEmplacementAffichage)

# get all
@router.get("/emplacementAffichage", response_model=list[EmplacementAffichageSchema], status_code=status.HTTP_200_OK, description="Get all emplacementAffichage")
async def get_all(db: Session = Depends(get_db)):
    return await asyncio.to_thread(EmplacementAffichageController.get_all, db)

# create
@router.post("/emplacementAffichage", response_model=EmplacementAffichageSchema, status_code=status.HTTP_201_CREATED, description="Create emplacementAffichage")
async def create(emplacementAffichage: EmplacementAffichageCreateSchema, db: Session = Depends(get_db)):
    return await asyncio.to_thread(EmplacementAffichageController.create, db, emplacementAffichage)

# update
@router.put("/emplacementAffichage/{IDEmplacementAffichage}", response_model=EmplacementAffichageSchema, status_code=status.HTTP_200_OK, description="Update emplacementAffichage")
async def update(IDEmplacementAffichage: int = Path(...), emplacementAffichage: EmplacementAffichageUpdateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(EmplacementAffichageController.update, db, emplacementAffichage)

# delete
@router.delete("/emplacementAffichage/{IDEmplacementAffichage}", status_code=status.HTTP_204_NO_CONTENT, description="Delete emplacementAffichage")
async def delete(IDEmplacementAffichage: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(EmplacementAffichageController.delete, db, IDEmplacementAffichage)
