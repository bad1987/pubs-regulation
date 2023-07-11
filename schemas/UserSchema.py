from pydantic import BaseModel, EmailStr
from typing import Text, List, Optional
from Enums.UserEnums import UserStatusEnum
from Enums.UserRoleEnum import UserRoleEnum
from Enums.LanguageEnum import LanguageEnum
from models.Models import User

class UserSchema(BaseModel):
    id: Optional[int]
    email: Optional[str]
    username: Optional[str]
    company_id: Optional[int]
    roles: Optional[UserRoleEnum] = None
    status: Optional[UserStatusEnum]
    permissions: Optional[List]
    firstname: Optional[str]
    lastname: Optional[str]
    default_language: Optional[LanguageEnum]
    
    
    class Config:
        orm_mode = True

    @classmethod
    def from_user(cls, user: User) -> 'UserSchema':
        return cls(
            id=user.id,
            email=user.email,
            username=user.username,
            company_id=user.company_id,
            roles=user.roles,
            status=user.status,
            permissions=[PermissionSchema(**{'id': perm.id, 'name': perm.name, 'description': perm.description}) for perm in user.permissions] if user.permissions else None,
            firstname=user.firstname,
            lastname=user.lastname,
            default_language=user.default_language,
        )

class PermissionSchema(BaseModel):
    id: Optional[int]
    name: Optional[str] 
    description: Optional[str]
    mode: Optional[str] 
    model_name: Optional[str] 

    class Config:
        orm_mode = True

class PermissionReturnModel(BaseModel):
    text: Optional[str]
    description: Optional[str]
    value: Optional[int]
        
class ApiSetting(BaseModel):
    api_token: Optional[str]

class UserCreateSchema(BaseModel):
    username: str
    email: EmailStr
    status: UserStatusEnum
    permissions: list | None = None
    roles: UserRoleEnum


class UserListSchema(BaseModel):
    users: List[UserSchema] = []
    permissions: List[PermissionReturnModel] = []