import sys
sys.path.append("..")
from controllers.users import UserController
from Enums.UserRoleEnum import UserRoleEnum
from Enums.UserEnums import UserStatusEnum
from schemas.UserSchema import UserCreateSchema, UserSchema, UserUpdateSchema
from models.users import Permission, User
from db.Connexion import SessionLocal

db = SessionLocal()
# Create admin data for user
permission = Permission(
    name="admin_all", mode="all", description="admin permissions permission", model_name="User"
)
db.add(permission)
user = User(
    email="admin@admin.com", username="admin", password="admin", firstname="admin", lastname="admin", roles=UserRoleEnum.ADMIN.value, status=UserStatusEnum.ACTIVE.value
)
user.set_password(user.password)
user.permissions.append(permission)

db.add(user)
db.commit()

print("Admin user created successfully")