from pydantic import BaseModel, EmailStr
from typing import Text, List, Optional
from Enums.UserEnums import UserStatusEnum
from Enums.UserRoleEnum import UserRoleEnum
from Enums.LanguageEnum import LanguageEnum
from models.users import User

class UserSchema(BaseModel):
    id: Optional[int]
    email: Optional[str]
    username: Optional[str]
    roles: Optional[UserRoleEnum] = None
    status: Optional[UserStatusEnum]
    permissions: Optional[List]
    firstname: Optional[str]
    lastname: Optional[str]
    
    
    class Config:
        orm_mode = True
        from_attributes = True

    @classmethod
    def from_user(cls, user: User) -> 'UserSchema':
        return cls(
            id=user.id,
            email=user.email,
            username=user.username,
            roles=user.roles,
            status=user.status,
            permissions=[PermissionSchema(**{'id': perm.id, 'name': perm.name, 'description': perm.description}) for perm in user.permissions] if user.permissions else None,
            firstname=user.firstname,
            lastname=user.lastname,
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
    password: str
    status: UserStatusEnum
    permissions: List[int] = []
    roles: UserRoleEnum


class UserListSchema(BaseModel):
    users: List[UserSchema] = []
    permissions: List[PermissionReturnModel] = []