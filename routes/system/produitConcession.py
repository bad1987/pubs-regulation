import asyncio
from fastapi import APIRouter, Depends, status
from fastapi.params import Body, Path, Query
from sqlalchemy.orm import Session
from dependencies.db_dependencies import get_db

from controllers.produitConsession import ProduitConcessionController
from schemas.CampagneProduitSchema import ProduitConsessionSchema, ProduitConsessionUpdateSchema, ProduitConsessionCreateSchema

router = APIRouter(
    tags=["ProduitConcession"],
)

# get by CodeProduitConsession
@router.get("/produitConsession/code", response_model=ProduitConsessionSchema, status_code=status.HTTP_200_OK, description="Get produitConsession by CodeProduitConsession")
async def get_by_code(CodeProduitConsession: str = Query(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(ProduitConcessionController.get_by_code, db, CodeProduitConsession)

# get produitConsession by ID
@router.get("/produitConsession/{IDProduitConsession}", response_model=ProduitConsessionSchema, status_code=status.HTTP_200_OK, description="Get produitConsession by ID")
async def get_by_id(IDProduitConsession: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(ProduitConcessionController.get, db, IDProduitConsession)

# get all produitConsession
@router.get("/produitConsession", response_model=list[ProduitConsessionSchema], status_code=status.HTTP_200_OK, description="Get all produitConsession")
async def get_all(db: Session = Depends(get_db)):
    return await asyncio.to_thread(ProduitConcessionController.get_all, db)

# create produitConsession
@router.post("/produitConsession", response_model=ProduitConsessionSchema, status_code=status.HTTP_201_CREATED, description="Create produitConsession")
async def create(produitConcession: ProduitConsessionCreateSchema, db: Session = Depends(get_db)):
    return await asyncio.to_thread(ProduitConcessionController.create, db, produitConcession)

# update produitConsession
@router.put("/produitConsession/{IDProduitConsession}", response_model=ProduitConsessionSchema, status_code=status.HTTP_200_OK, description="Update produitConsession")
async def update(IDProduitConsession: int = Path(...), produitConcession: ProduitConsessionUpdateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(ProduitConcessionController.update, db, IDProduitConsession, produitConcession)

# delete produitConsession
@router.delete("/produitConsession/{IDProduitConsession}", status_code=status.HTTP_204_NO_CONTENT, description="Delete produitConsession")
async def delete(IDProduitConsession: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(ProduitConcessionController.delete, db, IDProduitConsession)