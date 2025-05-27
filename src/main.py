from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from infrastructure.openmeteo import OpenMeteoService
from web.weather_router import weather_router
from api.test_router import test_router

from persistence.tables import *

app = FastAPI()
# app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(weather_router, prefix='/web')

app.include_router(test_router, prefix='/api')