import json
from typing import Dict
from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy import and_
from sqlalchemy.orm import Session

s_user_route = APIRouter(prefix='/admin', tags=['Users system'], include_in_schema=False)

@s_user_route.get("/user", response_model= UserSchema | None)
def get_user(request: Request, db: Session = Depends(get_db)):
    user_usecase = UserUsecase(db)
    user = user_usecase.get_user(request=request)

    platform_data = db.query(Platform_Data).filter(Platform_Data.language == user.default_language.value).filter(Platform_Data.platform_id == user.platform.id).first() if user and user.platform else None

    user = UserSchema.from_user(user) if user else None

    if user:
        user.platform = PlatformSimpleSchema(**{'id': platform_data.platform.id, 'name': platform_data.name, 'language': user.default_language.value}) if (platform_data and platform_data.platform.status) else None

    return user

@s_user_route.post('/users', response_model= UserSchema | Dict[str, str], status_code=201)
@requires_permission('write', ModelNameEnum.USER_MODEL.value)
async def add_user(request: Request, model: UserCreateSchema, db: Session = Depends(get_db), _user: dict = Depends(is_authenticated)):
    user_usecase = UserUsecase(db)
    result = user_usecase.create_user(model=model)
    return result

@s_user_route.put('/users/{id}', response_model=UserSchema | Dict[str, str])
@requires_permission('write', ModelNameEnum.USER_MODEL.value)
async def update_user(id: int, model: UserSchema, request: Request,  db: Session = Depends(get_db), _user: dict = Depends(is_authenticated)):
    user_usecase = UserUsecase(db)
    result = user_usecase.update_user(model=model, id=id)

    return {
        "message": "User updated successfully"
    }

# Send password to user email
@s_user_route.post('/users/{id}/send-password', response_model=Dict[str, str])
@requires_permission('write', ModelNameEnum.USER_MODEL.value)
async def send_password(id: int, request: Request,  db: Session = Depends(get_db), _user: dict = Depends(is_authenticated)):
    user_usecase = UserUsecase(db)
    result = user_usecase.send_password(id=id)
    return result

# delete a user
@s_user_route.delete("/user/{id}")
@requires_permission('delete', ModelNameEnum.USER_MODEL.value)
async def delete_user(id: int, request: Request,  db_local: Session = Depends(get_db), _user: dict = Depends(is_authenticated)):
    user_usecase = UserUsecase(db_local)
    result = user_usecase.delete_user(id)

    return result