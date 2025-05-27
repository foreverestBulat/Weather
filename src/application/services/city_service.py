from typing import Optional
from fastapi import Depends
from application.dto.city import CityStatsDTO
from application.dto.pagination import PaginatedResult
from application.mappers.city import map_cities_to_stats_dto, map_city_to_stats_dto
from persistence.repositories.city_repository import CityRepository


class CityService:
    def __init__(
            self,
            city_repository: CityRepository = Depends()
        ):
        self.city_repository = city_repository
        
    async def get_search_cities_async(self, search: str) -> list[str]:
        """Получить список городов начинающихся на search"""
        return await self.city_repository.get_list_by_str_async(q=search)
    
    async def get_stats_async(self, city: str) -> Optional[CityStatsDTO]:
        result = await self.city_repository.get_by_name_async(name=city)
        if not result:
            return None
        return map_city_to_stats_dto(result)
    
    async def get_stats_page_async(self, number, size) -> PaginatedResult:
        result, total = await self.city_repository.get_page_async(number=number, size=size)
        return PaginatedResult.create(result=map_cities_to_stats_dto(result), number=number, size=size, total_count=total)
        