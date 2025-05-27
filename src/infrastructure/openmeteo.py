from typing import Dict, Optional
from fastapi import Depends
import httpx

from config import OPENMETEO_API_URL
from infrastructure.openstreetmap import OpenStreetMapService


class OpenMeteoService:
    def __init__(
            self, 
            api_url: str=OPENMETEO_API_URL, 
            openstreetmap_service: OpenStreetMapService = Depends()
        ):
        self.api_url = api_url
        self.openstreetmap_service = openstreetmap_service
        
    async def get_weather_forecast_by_coordinates_async(
            self, 
            latitude: float, 
            longitude: float, 
            days: int=3
        ) -> Optional[Dict]:
        """Получение прогноза погоды по координатам"""
        
        params = {
            'latitude': latitude,
            'longitude': longitude,
            'hourly': "temperature_2m,weathercode",
            'forecast_days': days,
            'timezone': 'auto'
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(self.api_url, params=params)
            return response.json(), response.status_code
        
    async def get_weather_forecast_by_city_async(
            self, 
            city: str, 
            days: int=3, 
        ):
        """Получение прогноза погоды по названию города"""
        
        coordinates = await self.openstreetmap_service.get_city_coordinates_async(city=city)
        if not coordinates:
            return None
        
        result, code = await self.get_weather_forecast_by_coordinates_async(
            **coordinates, 
            days=days
        )
        
        return result, code