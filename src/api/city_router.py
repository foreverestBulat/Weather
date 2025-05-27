from typing import Optional
from fastapi import APIRouter, Depends

from application.dto.city import CityStatsDTO
from application.dto.pagination import PaginatedResult
from application.services.city_service import CityService


city_router = APIRouter(tags=['city'], prefix='/city')


@city_router.get('/suggestions', response_model=list[str])
async def get_suggestions(
        search: str,
        service: CityService = Depends() 
    ) -> list[str]:
    """Возращает список городов начинающихся на search."""
    return await service.get_search_cities_async(search=search)

@city_router.get('/stats/one', response_model=Optional[CityStatsDTO])
async def get_stats_city(
        city: str,
        service: CityService = Depends()
    ) -> Optional[CityStatsDTO]:
    """Возращает город с его количеством запросов. В базе данных если нет города, то запросов по этому городу не было."""
    return await service.get_stats_async(city=city)

@city_router.get('/stats/page', response_model=PaginatedResult)
async def get_stats_list_city(
        number: int = 1, 
        size: int = 5,
        service: CityService = Depends()
    ) -> PaginatedResult:
    """Возращает список городов с их количеством запросов в формате для пагинации."""
    return await service.get_stats_page_async(number=number, size=size)
    
    