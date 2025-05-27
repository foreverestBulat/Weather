from datetime import datetime

from pydantic import BaseModel


class WeatherForecastDTO(BaseModel):
    """DTO для конечного ответа API"""
    
    city: str
    latitude: float
    longitude: float
    time: list[datetime]
    temperature: list[float]
    weather_str:  list[str]
    count: int