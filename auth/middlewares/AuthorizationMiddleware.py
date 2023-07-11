from fastapi import HTTPException, Request, status, Response
from fastapi.responses import RedirectResponse, JSONResponse
import datetime, time

from fastapi import Request, HTTPException
from App.core.auth.auth import validate_token
from App.output_ports.db.Connexion import SessionLocal
from App.core.auth.Acls.RoleChecker import Role_checker
from App.output_ports.models.Models import Login_Attempt

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def orders_permissions(request: Request, call_next):
    permission = Role_checker(['Role_affiliate', 'Role_direct_sale', 'Role_admin'])
    # check if the user has the permissions
    if request.url.path.startswith("/orders"):
        db = SessionLocal()
        try:
            permission(request, db)
            db.close()
        except HTTPException as e:
            print(str(e.detail), e.status_code)
            db.close()
            return RedirectResponse("/errors/403")
        
    response = await call_next(request)
    return response

async def block_ip_middleware(request: Request, call_next):
    try:
        # Récupération de l'adresse IP du client
        ip_address = request.client.host
        now = datetime.datetime.now()

        timestamp = time.mktime(now.timetuple())

        # Vérification si l'adresse IP est bloquée
        session = SessionLocal()
        attempt = session.query(Login_Attempt).filter(
            Login_Attempt.ip == ip_address
        ).first()
        if attempt != None and attempt.count >= 3 and attempt.timestamp >= timestamp:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Your ip is blocked")

        if attempt != None:
            attempt.count = 0
            session.commit()

        # Si l'adresse IP n'est pas bloquée, on continue le traitement de la requête
        response = await call_next(request)
        
        return response
    except HTTPException as e:
        return JSONResponse(content={'detail': 'Your ip is blocked'}, status_code=status.HTTP_401_UNAUTHORIZED)
    

class TokenMiddleware:
    def __init__(self, app):
        self.app = app
    
    async def __call__(self, request: Request, *args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            raise HTTPException(status_code=401, detail="Missing authorization header")
        token = auth_header.split(" ")[1]
        token = token.removeprefix("Bearer").strip()
        if not validate_token(token):
            raise HTTPException(status_code=401, detail="Invalid token")
        response = await self.app(request, *args, **kwargs)
        return response

async def token_middleware(request: Request, call_next):
    auth_header = request.headers.get("Authorization")
    print("inside middleware")
    if not auth_header:
        raise HTTPException(status_code=401, detail="Missing authorization header")
    token = auth_header.split(" ")[1]
    token = token.removeprefix("Bearer").strip()
    if not validate_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    response = await call_next(request)
    # try:
    #     ...
    # except Exception as e:
    #     raise e
    return response