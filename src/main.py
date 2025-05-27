from fastapi import FastAPI
from web.weather_router import weather_router
from api.city_router import city_router

from persistence.tables import *


app = FastAPI()

app.include_router(weather_router, prefix='/web')
app.include_router(city_router, prefix='/api')

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="127.0.0.1", port=8000)
