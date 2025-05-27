from typing import List
from application.dto.city import CityStatsDTO
from domain.entities import City


def map_city_to_stats_dto(city: City) -> CityStatsDTO:
    return CityStatsDTO(
        name=city.name,
        count=city.count
    )

def map_cities_to_stats_dto(cities: List[City]) -> List[CityStatsDTO]:
    return [
        CityStatsDTO(
            name=city.name,
            count=city.count
        )
        for city in cities
    ]