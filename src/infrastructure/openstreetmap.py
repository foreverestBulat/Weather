import json
from fastapi import Depends
import httpx
from redis import Redis

from config import OPENSTREETMAP_API_URL, REDIS_URL
from domain.entities import City
from persistence.repositories.city_repository import CityRepository

class OpenStreetMapService:
    def __init__(
            self, 
            api_url: str=OPENSTREETMAP_API_URL,
            city_repository: CityRepository = Depends()
        ):
        self.api_url = api_url
        self.redis = Redis.from_url(REDIS_URL)
        self.city_repository = city_repository
    
    async def get_city_coordinates_async(
            self, 
            city: str,
            use_cache: bool = True,
            cache_ttl: int = 86400
        ):
        """Получение координат города с кэшированием в Redis"""
        
        cache_key = f"city_coords:{city.lower()}"
        try:
            if use_cache:
                cached_data = self.redis.get(cache_key)
                if cached_data:
                    print('---------------- FROM REDIS ----------------')
                    return json.loads(cached_data)
        except:
            print('---------------- NO CONNECTION REDIS ----------------')
        
        entity = await self.city_repository.get_by_name_async(name=city)
        if entity:
            coordinates = {
                "latitude": entity.latitude,
                "longitude": entity.longitude
            }
            
            try:
                self.redis.set(
                    cache_key,
                    json.dumps(coordinates),
                    ex=cache_ttl
                )
            except:
                print('---------------- NO CONNECTION REDIS ----------------')
            
            print('---------------- FROM POSTGRESQL ----------------')
            return coordinates
        
        params = {
            "q": city,
            "format": "json",
            "limit": 1
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(self.api_url, params=params)
            data = response.json()
            if data:
                coordinates = {
                    "latitude": float(data[0]["lat"]),
                    "longitude": float(data[0]["lon"])
                }
                
                try:
                    self.redis.set(
                        cache_key,
                        json.dumps(coordinates),
                        ex=cache_ttl
                    )
                except:
                    print('---------------- NO CONNECTION REDIS ----------------')
                
                await self.city_repository.unit_of_work.create_async(
                    City(
                        name=city,
                        latitude=coordinates['latitude'],
                        longitude=coordinates['longitude'],
                        count=1
                    )
                )
                
                print('---------------- FROM OPENSTREETMAP ----------------')
                return coordinates
            return None
        
    def clear_cache(self, city: str = None):
        """Очистка кэша (для конкретного города или всего)"""
        
        if city:
            self.redis.delete(f"city_coords:{city.lower()}")
        else:
            for key in self.redis.scan_iter("city_coords:*"):
                self.redis.delete(key)