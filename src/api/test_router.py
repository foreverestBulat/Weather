from fastapi import APIRouter, Depends, Request

from infrastructure.openmeteo import OpenMeteoService


test_router = APIRouter(tags=['test'], prefix='/test')

@test_router.get('/weather')
async def main_page(
        request: Request,
        city: str,
        openmeteo_service: OpenMeteoService = Depends()
    ):
    return await openmeteo_service.get_weather_forecast_by_city_async(city=city)