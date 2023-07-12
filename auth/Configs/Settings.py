# --------------------------------------------------------------------------
# Setup FastAPI
# --------------------------------------------------------------------------
class Settings:
    SECRET_KEY: str = "833899475be6080f568858429c04f9212d10dbc1b93e0677a1e7e260f1e8352d"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 235465  # in mins 58000
    API_TOKEN_EXPIRE_DAYS = 30  # in days
    COOKIE_NAME = "access_token"