from fastapi import FastAPI
from web.weather_router import weather_router
from api.city_router import city_router

from persistence.tables import *


app = FastAPI()

app.include_router(weather_router, prefix='/web')
app.include_router(city_router, prefix='/api')

from fastapi.responses import RedirectResponse
@app.exception_handler(404)
async def custom_404_handler(_, __):
    return RedirectResponse("/web/weather/main")
