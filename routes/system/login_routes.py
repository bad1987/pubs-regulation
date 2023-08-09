import json, time, datetime
from fastapi import Depends, HTTPException, Request, Response, status, APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from sqlalchemy.orm import Session
from rich.console import Console
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm

from dotenv import load_dotenv
import os
from auth.Configs.Settings import Settings
from auth.auth import create_access_token, get_token, verify_token

from dependencies.db_dependencies import get_db
from models.users import User
from schemas.UserSchema import UserSchema

load_dotenv()
secure_cookie = os.getenv('COOKIE_SECURE')
# capitalize and convert secure_cookie to bool
if secure_cookie.lower() == 'true':
    secure_cookie = True
else:
    secure_cookie = False

route = APIRouter(prefix='', tags=['Handle user accounts'], include_in_schema=False)
# templates = Jinja2Templates(directory="templates")
console = Console()

@route.post("/login")
def login(response: Response, form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Authenticate the user
    print(f"username: {form_data.username} password: {form_data.password}")
    user = User.authenticate(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    # Create an access token for the user
    access_token = create_access_token({"sub": user.email})

    # Set the access token as an HTTP-only cookie
    max_age = Settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    response.set_cookie(key=Settings.COOKIE_NAME, value=access_token, domain='localhost', path='/', max_age=max_age, samesite='None', secure=secure_cookie)

    # Return the access token
    user = UserSchema.model_validate(user).model_dump()
    return {Settings.COOKIE_NAME: access_token, "token_type": "bearer", "user":user}

# --------------------------------------------------------------------------
# Logout
# --------------------------------------------------------------------------
@route.delete("/logout")
def logout(request: Request, response: Response):
    response.delete_cookie(Settings.COOKIE_NAME, domain='localhost', path='/', samesite='None', secure=secure_cookie)
    return {"message": "Logged out"}

@route.get("/user/token")
def get_user_from_token(token: str = Depends(get_token), db: Session = Depends(get_db)):
    # Decode the access token to get the user's email
    email = verify_token(token)
    # Retrieve the user from the database
    user = User.get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


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
