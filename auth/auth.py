from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
from App.core.auth import LoginController

from App.core.auth.Configs.Settings import Settings
from sqlalchemy.orm import Session

from App.core.dependencies.db_dependencies import get_db

security = HTTPBearer()

async def validate_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    # validate token
    try:
        payload = jwt.decode(str(credentials.credentials.removeprefix("Bearer").strip()), Settings.SECRET_KEY, algorithms=Settings.ALGORITHM)
        return True if payload else False
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
#check if user is connected
async def is_authenticated(request: Request, db: Session = Depends(get_db)):
    user = LoginController.get_current_user_from_cookie(request, db)

    if not user:
        user = LoginController.get_current_user_from_api_token(request, db)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated"
        )
    return user