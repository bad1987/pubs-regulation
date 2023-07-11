
from fastapi import HTTPException, Request, status
from auth.Acls.Permissions import PermissionChecker
from auth.Acls.RoleChecker import Role_checker
from functools import wraps

roles_checker = Role_checker()

def requires_permission(permission_type: str, model_name: str):
    def wrapper(func):
        @wraps(func)
        async def wrapped(*args, **kwargs):
            user = kwargs.get('_user')  # get the user object from the first argument
            if not user or not hasattr(user, 'roles') or not hasattr(user, 'id'):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized')

            # check if the user has the required permission for the model
            permission_checker = PermissionChecker(user)
            has_permission = getattr(permission_checker, f'has_{permission_type}_permission')(model_name)
            if not has_permission:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Forbidden')

            return await func(*args, **kwargs)

        return wrapped

    return wrapper
