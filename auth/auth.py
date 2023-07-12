from datetime import datetime, timedelta
import jwt
from jwt import InvalidTokenError
import os, dotenv
from fastapi import Depends, HTTPException, Request, Security, status
from fastapi.security import OAuth2PasswordBearer, HTTPBearer, HTTPAuthorizationCredentials
from auth.Configs import Settings
from models.users import User

dotenv.load_dotenv()
# Define a secret key for signing the tokens (use a more secure value in production)
SECRET_KEY = os.getenv('SECRET_KEY')

# Define an algorithm for encoding and decoding the tokens
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# Define a dependency for getting the token from the request header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

security = HTTPBearer()


def get_token(request: Request, authorization: str = Depends(oauth2_scheme)):
    # Try to extract the access token from the Authorization header
    token = authorization
    if token and token.startswith("Bearer "):
        # Remove the "Bearer" prefix
        token = token[7:]
        token = token.strip()
    if not token:
        # If the Authorization header is not set, try to extract the access token from the cookie
        token = request.cookies.get(Settings.COOKIE_NAME)
    if not token:
        # If neither the Authorization header nor the cookie is set, raise an exception
        raise HTTPException(status_code=401, detail="Not authenticated")
    return token

# Define a function that generates a token from a user id
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Define a function that verifies a token and returns a user id
def verify_token(token: str) -> str:
    # Decode the token with the secret key and the algorithm
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Return the user id from the payload
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        # Raise an exception if the token is expired
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError:
        # Raise an exception if the token is invalid
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
