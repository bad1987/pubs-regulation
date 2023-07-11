# --------------------------------------------------------------------------
# Setup FastAPI
# --------------------------------------------------------------------------
class Settings:
    SECRET_KEY: str = "secretApiSettingDinotech1234./*@#"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 235465  # in mins 58000
    API_TOKEN_EXPIRE_DAYS = 30  # in days
    COOKIE_NAME = "access_token"