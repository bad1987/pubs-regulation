from pydantic import BaseModel
from auth.Configs.Settings import Settings
from schemas.UserSchema import UserSchema 


class LoginAccessTokenResponseSchema(BaseModel):
    Settings.COOKIE_NAME: str
    token_type: str
    user: UserSchema