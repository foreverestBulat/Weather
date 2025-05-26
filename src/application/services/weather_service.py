from typing import Optional
from fastapi import Depends
from application.dto.weather import WeatherForecastDTO
from infrastructure.mappers.weather import WeatherMapper
from infrastructure.models.openmeteo_response import OpenMeteoResponse
from infrastructure.openmeteo import OpenMeteoService


class WeatherService:
    def __init__(self, openmeteo_service: OpenMeteoService = Depends()):
        self.weather_service = openmeteo_service

    async def get_forecast_async(self, city: str):# -> Optional[WeatherForecastDTO]:
        """Получение прогноза по городу"""
    
        raw_data = await self.weather_service.get_weather_forecast_by_city_async(city=city)
        if not raw_data:
            return None
        validated_data = OpenMeteoResponse(**raw_data)
        return WeatherMapper.map_openmeteo_to_dto(city, validated_data)
    