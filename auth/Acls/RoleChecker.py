
from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from App.core.auth.LoginController import get_current_user_from_cookie

class Role_checker:
    def __init__(self, allowed_roles: list = []) -> None:
        self.allowed_roles = allowed_roles
        self.admin_roles = ['Role_admin']
        self.direct_sale_roles = ['Role_direct_sale']
        self.affiliate_roles = ['Role_affiliate']
    
    def __call__(self, request: Request, db: Session):
        user = get_current_user_from_cookie(request, db)
        if (not user) or (user.roles not in self.allowed_roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Operation not permitted"
            )
        return user
    
    def setRoles(self, roles):
        if isinstance(roles, list):
            for r in roles:
                if r not in self.allowed_roles:
                    self.allowed_roles.append(r)
    
    def admin_access(self, roles: str) -> bool:
        if not roles:
            return False
        roles = roles.split(',')
        for role in roles:
            if role in self.admin_roles:
                return True
        return False

    def affiliate_access(self, roles: str) -> bool:
        if not roles:
            return False
        roles = roles.split(',')
        for role in roles:
            if role in self.affiliate_roles:
                return True
        return False


    def direct_sale_access(self, roles: str) -> bool:
        if not roles:
            return False
        roles = roles.split(',')
        for role in roles:
            if role in self.direct_sale_roles:
                return True
        return False
    

    def vendors_access(self, roles: str) -> bool:
        combined_roles = self.affiliate_roles + self.direct_sale_roles
        if not roles:
            return False
        roles = roles.split(',')
        for role in roles:
            if role in combined_roles:
                return True
        return False
