from enum import Enum

class UserRoleEnum(Enum):
    ADMIN = "Role_admin"
    REGI = "Role_regi"
    OPERATOR = "Role_operator"
    CLIENT = "Role_client"

class ModelNameEnum(Enum):
    USER_MODEL = 'user'
    SETTING_MODEL = "setting"