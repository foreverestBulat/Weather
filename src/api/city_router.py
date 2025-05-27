from fastapi import APIRouter, Depends

from application.services.city_service import CityService


city_router = APIRouter(tags=['city'], prefix='/city')


@city_router.get('/suggestions')
async def get_suggestions(
        search: str,
        service: CityService = Depends() 
    ):
    return await service.get_search_cities_async(search=search)

@city_router.get('/stats/one')
async def get_stats_city(
        city: str,
        service: CityService = Depends()
    ):
    return await service.get_stats_async(city=city)

@city_router.get('/stats/page')
async def get_stats_list_city(
    number: int = 1, 
    size: int = 5,
    service: CityService = Depends()
):
    return await service.get_stats_page_async(number=number, size=size)
    
    