from pydantic import BaseModel


class OpenMeteoResponse(BaseModel):
    """Модель для сырого ответа API"""
    
    latitude: float
    longitude: float
    hourly: dict[str, list]