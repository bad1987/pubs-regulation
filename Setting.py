import pathlib

from starlette.config import Config

ROOT = pathlib.Path(__file__).resolve()
BASE_DIR = ROOT.parent

config = Config(BASE_DIR / ".env")


# CONNECTION LOCAL DATABASE
MARIADB_HOST = config("MARIADB_HOST", str)
MARIADB_PORT = config("MARIADB_PORT", int)
MARIADB_USER = config("MARIADB_USER", str)
MARIADB_PASSWORD = config("MARIADB_PASSWORD", str)
MARIADB_DB = config("MARIADB_DB", str)