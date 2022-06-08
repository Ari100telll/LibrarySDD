from pathlib import Path

import environ

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

env = environ.Env()
env.read_env(str(ROOT_DIR / ".env"))

DATABASE_URL = env("DATABASE_URL")
DB_NAME = env("DB_NAME")
DB_USER = env("DB_USER")
DB_PASSWORD = env("DB_PASSWORD")
DB_HOST = env("DB_HOST")
DB_PORT = env("DB_PORT")

DATABASE_URL = f"{DATABASE_URL}{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

CONFIGS = [("SQLALCHEMY_DATABASE_URI", DATABASE_URL)]
