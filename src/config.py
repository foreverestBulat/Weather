import os
import pathlib

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from dotenv import load_dotenv

os.environ.clear()
load_dotenv()


OPENMETEO_API_URL = os.environ.get('OPENMETEO_URL')
OPENSTREETMAP_API_URL = os.environ.get('OPENSTREETMAP_URL')

DATABASES = {
    'PostgreSQL': {
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'NAME': os.environ.get('DB_NAME'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
DB_POSTGRESQL = DATABASES['PostgreSQL']
ASYNC_DB_POSTGRESQL_URL = DATABASE_URL = f'postgresql+asyncpg://{DB_POSTGRESQL["USER"]}:{DB_POSTGRESQL["PASSWORD"]}@{DB_POSTGRESQL["HOST"]}/{DB_POSTGRESQL["NAME"]}'
SYNC_DB_POSTGRESQL_URL = DATABASE_URL = f'postgresql+psycopg2://{DB_POSTGRESQL["USER"]}:{DB_POSTGRESQL["PASSWORD"]}@{DB_POSTGRESQL["HOST"]}/{DB_POSTGRESQL["NAME"]}'



REDIS_URL = os.environ.get('REDIS_URL')


BASE_DIR = pathlib.Path(__file__).parent
templates = Jinja2Templates(directory=[
    BASE_DIR / 'web' / 'templates',
])

# print(templates)
# print(DATABASES)
# print(OPENMETEO_API_URL)