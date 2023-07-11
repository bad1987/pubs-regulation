from enum import Enum

class UserRoleEnum(Enum):
    ADMIN = "Role_admin"

class ModelNameEnum(Enum):
    USER_MODEL = 'user'
    SETTING_MODEL = "setting"