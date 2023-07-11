from fastapi import HTTPException, status
from App.Http.Controllers.UserController import UserController
from fastapi.encoders import jsonable_encoder

from App.input_ports.schemas.UserSchema import PermissionSchema, UserSchema


class PermissionChecker:
    def __init__(self, user:UserSchema):
        self.user = self.to_user_schema(user)
        self.user_controller = UserController()
        self.permissions = []
    
    def to_user_schema(self, user: UserSchema) -> UserSchema:
        user_dict = jsonable_encoder(user)
        user_dict.pop('permissions', None)
        permissions = [PermissionSchema(**jsonable_encoder(p)) for p in user.permissions]
        return UserSchema(**user_dict, permissions=permissions)
        
    def has_read_permission(self, model_name: str) -> bool:
        self.permissions = self.user_controller.getPermissions('R', model_name.lower().strip())
        # if self.permissions and model_name == 'user':
        #     self.permissions = self.filter_user_permissions(self.permissions, self.user)
        return self.check_permissions(self.permissions, self.user.permissions)

    def has_write_permission(self, model_name: str) -> bool:
        self.permissions = self.user_controller.getPermissions('W', model_name.lower().strip())
        # if self.permissions and model_name == 'user':
        #     self.permissions = self.filter_user_permissions(self.permissions, self.user)
        return self.check_permissions(self.permissions, self.user.permissions)

    def has_delete_permission(self, model_name: str) -> bool:
        self.permissions = self.user_controller.getPermissions('D', model_name.lower().strip())
        # if self.permissions and model_name == 'user':
        #     self.permissions = self.filter_user_permissions(self.permissions, self.user)
        return self.check_permissions(self.permissions, self.user.permissions)

    def check_permissions(self, permissions: list[PermissionSchema], user_permissions: list[PermissionSchema]) -> bool:
        if not permissions:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="No permissions found"
            )
        permission_names = [p.name for p in permissions]
        user_permission_names = [p.name for p in user_permissions]
        return any(p in user_permission_names for p in permission_names)

    def filter_user_permissions(self, permissions: list[PermissionSchema], user: UserSchema) -> list[PermissionSchema]:
        pattern = 'Acl_admin' if user.roles == 'Role_admin' else 'Acl_vendor'
        return [p for p in permissions if p.name.startswith(pattern)]