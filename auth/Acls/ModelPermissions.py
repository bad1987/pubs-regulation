
from App.Http.Schema.UserSchema import PermissionSchema, UserSchema
from fastapi.encoders import jsonable_encoder


class ModelPermissions:
    def __init__(self, user:UserSchema) -> None:
        self.user = self.to_user_schema(user)
        
    def to_user_schema(self, user: UserSchema) -> UserSchema:
        user_dict = jsonable_encoder(user)
        user_dict.pop('permissions', None)
        permissions = [PermissionSchema(**jsonable_encoder(p)) for p in user.permissions]
        return UserSchema(**user_dict, permissions=permissions)
    
    def can_read_user_vendors(self):
        permissions = ['Acl_vendor_read', 'Acl_admin_read']
        user_permissions:list[PermissionSchema] = self.user.permissions
        for p in user_permissions:
            if p.name in permissions:
                return True
        return False
    
    def can_read_user_admins(self):
        permissions = ['Acl_admin_read']
        user_permissions:list[PermissionSchema] = self.user.permissions
        for p in user_permissions:
            if p.name in permissions:
                return True
        return False
    
    def can_update_user_vendors(self):
        permissions = ['Acl_vendor_write', 'Acl_admin_write']
        user_permissions:list[PermissionSchema] = self.user.permissions
        for p in user_permissions:
            if p.name in permissions:
                return True
        return False
    
    def can_update_user_admins(self):
        permissions = ['Acl_admin_write']
        user_permissions:list[PermissionSchema] = self.user.permissions
        for p in user_permissions:
            if p.name in permissions:
                return True
        return False
        
    def can_delete_user_vendors(self):
        permissions = ['Acl_vendor_delete', 'Acl_admin_delete']
        user_permissions:list[PermissionSchema] = self.user.permissions
        for p in user_permissions:
            if p.name in permissions:
                return True
        return False
    
    def can_delete_user_admins(self):
        permissions = ['Acl_admin_delete']
        user_permissions:list[PermissionSchema] = self.user.permissions
        for p in user_permissions:
            if p.name in permissions:
                return True
        return False
    