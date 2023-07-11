import json, time, datetime
from fastapi import Depends, HTTPException, Request, Response, status, APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from sqlalchemy.orm import Session
from rich.console import Console
from fastapi.encoders import jsonable_encoder
from App.core.auth.Configs.OAuth2PasswordBearerWithCookie import OAuth2PasswordBearerWithCookie
from App.core.auth.Configs.Settings import Settings
from App.core.use_cases.authentication_use_case import AuthenticationUsecase
from App.output_ports.db.Connexion import SessionLocal
from App.output_ports.models.Models import User
from typing import Dict, List, Optional
import i18n
from App.Http.Schema.UserSchema import UserSchema

from App.core.auth import LoginController

from dotenv import load_dotenv
import os

load_dotenv()
secure_cookie = os.getenv('COOKIE_SECURE')
# capitalize and convert secure_cookie to bool
if secure_cookie.lower() == 'true':
    secure_cookie = True
else:
    secure_cookie = False

# instantiate a new translator class
translator = i18n.Translator('languages/')

route = APIRouter(prefix='', tags=['Handle account users'], include_in_schema=False)
# templates = Jinja2Templates(directory="templates")
console = Console()

oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@route.post("token")
def login_for_access_token(
    request: Request,
    form_data: dict,
    db: Session = Depends(get_db)
) -> Dict[str, str]:
    
    auth_usecase = AuthenticationUsecase(db)
    result = auth_usecase.login_access_token(request=request, form_data=form_data)

    return result

@route.post("/auth/login")
async def login_post(request: Request, response: Response, db: Session = Depends(get_db)):
    credentials = json.loads(await request.body())
 
    res = login_for_access_token(request, credentials, db)
    res.update({'expired_at': Settings.ACCESS_TOKEN_EXPIRE_MINUTES})
    res.update({'cookie_name': Settings.COOKIE_NAME})

    # setting the cookie
    max_age = res['expired_at'] * 60
    response.set_cookie(Settings.COOKIE_NAME, res[Settings.COOKIE_NAME], domain='localhost', path='/', max_age=max_age, samesite='None', secure=secure_cookie)
    return jsonable_encoder(res)

# --------------------------------------------------------------------------
# Logout
# --------------------------------------------------------------------------
@route.delete("/auth/logout")
def logout(request: Request, response: Response):
    response.delete_cookie(Settings.COOKIE_NAME, domain='localhost', path='/', samesite='None', secure=secure_cookie)
    return {"message": "Logged out"}

@route.get('/auth/refresh')
async def refresh_token(request: Request, db: Session = Depends(get_db)):
    user = LoginController.get_current_user_from_cookie(request, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not logged in"
        )
    access_token = LoginController.create_access_token(data={"username": user.email})
    context = {Settings.COOKIE_NAME: access_token, "token_type": "bearer"}
    context.update({'expired_at': Settings.ACCESS_TOKEN_EXPIRE_MINUTES})
    context.update({'cookie_name': Settings.COOKIE_NAME})
    return jsonable_encoder(context)


@route.post("/forgot-password")
async def forgot_password(request: Request, db_local: Session = Depends(get_db)):
    auth_usecase = AuthenticationUsecase(db_local)
    return auth_usecase.forgotten_password(request)

@route.post("/reset-password/{token}")
async def reset_password(token: str, request: Request, db_local: Session = Depends(get_db)):
    auth_usecase = AuthenticationUsecase(db_local)
    return auth_usecase.reset_password(request=request, token=token)


@route.get("/login_as_vendor/{vendor_id}")
def login_as_vendor(request: Request, response: Response, vendor_id: int, db: Session = Depends(get_db)):
    response.delete_cookie(Settings.COOKIE_NAME, domain='localhost', path='/', samesite='None', secure=secure_cookie)
    
    auth_usecase = AuthenticationUsecase(db)
    res = auth_usecase.login_access_token_by_vendor(request, vendor_id)

    res.update({'expired_at': Settings.ACCESS_TOKEN_EXPIRE_MINUTES})
    res.update({'cookie_name': Settings.COOKIE_NAME})

    # setting the cookie
    max_age = res['expired_at'] * 60
    response.set_cookie(Settings.COOKIE_NAME, res[Settings.COOKIE_NAME], domain='localhost', path='/', max_age=max_age, samesite='None', secure=secure_cookie)
    return jsonable_encoder(res)