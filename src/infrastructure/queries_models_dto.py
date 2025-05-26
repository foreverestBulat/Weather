from typing import Dict
from pydantic import BaseModel
from datetime import datetime


class GetWeatherForecastByCityDto(BaseModel):
    city: str
    latitude: float
    longitude: float
    time: list[datetime]
    temperature_2m: list[float]
    weathercode: list[int]

    @staticmethod
    def create(
            city: str,
            result: Dict, 
        ):
        return GetWeatherForecastByCityDto(
            city=city,
            latitude=result['latitude'],
            longitude=result['longitude'],
            time=result['hourly']['time'],
            temperature_2m=result['hourly']['temperature_2m'],
            weathercode=result['hourly']['weathercode']
        )
        