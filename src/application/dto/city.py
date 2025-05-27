from pydantic import BaseModel


class CityStatsDTO(BaseModel):
    name: str
    count: int
    