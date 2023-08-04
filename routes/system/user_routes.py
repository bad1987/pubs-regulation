import asyncio
from fastapi import APIRouter, Depends, status
from fastapi.params import Body, Path, Query
from sqlalchemy.orm import Session
from dependencies.db_dependencies import get_db

from controllers.users import UserController
from schemas.UserSchema import UserCreateSchema, UserSchema, UserUpdateSchema

router = APIRouter(
    tags=["User"],
)

@router.get("/user/email", response_model=UserSchema, status_code=status.HTTP_200_OK, description="Get user by ID")
async def get_by_email(email: str = Query(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(UserController.get_user_by_email, db, email)

@router.get("/user/{IDUser}", response_model=UserSchema, status_code=status.HTTP_200_OK, description="Get user by ID")
async def get_by_ID(IDUser: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(UserController.get, db, IDUser)

@router.post("/user", response_model=UserSchema, status_code=status.HTTP_201_CREATED, description="Create user")
async def create(user: UserCreateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(UserController.create, db, user)

@router.put("/user/{IDUser}", response_model=UserSchema, status_code=status.HTTP_200_OK, description="Update user")
async def update(IDUser: int = Path(...), user: UserUpdateSchema = Body(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(UserController.update, db, IDUser, user)

@router.delete("/user/{IDUser}", status_code=status.HTTP_204_NO_CONTENT, description="Delete user")
async def delete(IDUser: int = Path(...), db: Session = Depends(get_db)):
    return await asyncio.to_thread(UserController.delete, db, IDUser)