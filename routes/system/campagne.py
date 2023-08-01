import asyncio
from fastapi import APIRouter, Depends, status
from fastapi.params import Body, Path, Query
from sqlalchemy.orm import Session
from dependencies.db_dependencies import get_db

from controllers.campagne import CampagnePubController
from schemas.CampagneProduitSchema import CampagnePubSchema, CampagnePubUpdateSchema, CampagnePubCreateSchema

router = APIRouter(
    tags=["Campagne"],
)

@router.get("/campagne/code", response_model=CampagnePubSchema, status_code=status.HTTP_200_OK, description="Get campagne by Code")
async def get_by_code(CodeCampagne: str = Query(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(CampagnePubController.getByCodeCampagne, db, CodeCampagne)

@router.get("/campagne/{IDCampagne}", response_model=CampagnePubSchema, status_code=status.HTTP_200_OK, description="Get campagne by ID")
async def get_by_ID(IDCampagne: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(CampagnePubController.get, db, IDCampagne)

@router.get("/campagne", response_model=list[CampagnePubSchema], status_code=status.HTTP_200_OK, description="Get all campagne")
async def get_all(db: Session = Depends(get_db)):
    return await asyncio.to_thread(CampagnePubController.getAll, db)

@router.post("/campagne", response_model=CampagnePubSchema, status_code=status.HTTP_201_CREATED, description="Create campagne")
async def create(campagne: CampagnePubCreateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(CampagnePubController.create, db, campagne)

@router.put("/campagne/{IDCampagne}", response_model=CampagnePubSchema, status_code=status.HTTP_200_OK, description="Update campagne")
async def update(IDCampagne: int = Path(...), campagne: CampagnePubUpdateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(CampagnePubController.update, db, campagne)

@router.delete("/campagne/{IDCampagne}", status_code=status.HTTP_204_NO_CONTENT, description="Delete campagne")
async def delete(IDCampagne: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(CampagnePubController.delete, db, IDCampagne)
