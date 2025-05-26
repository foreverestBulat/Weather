import json
import httpx
from redis import Redis

from config import OPENSTREETMAP_API_URL, REDIS_URL

class OpenStreetMapService:
    def __init__(self, api_url: str=OPENSTREETMAP_API_URL):
        self.api_url = api_url
        self.redis = Redis.from_url(REDIS_URL)
    
    async def get_city_coordinates_async(
            self, 
            city: str,
            use_cache: bool = True,
            cache_ttl: int = 86400
        ):
        """Получение координат города с кэшированием в Redis"""
        
        if self.redis:
            cache_key = f"city_coords:{city.lower()}"
            
            if use_cache:
                cached_data = self.redis.get(cache_key)
                if cached_data:
                    print('---------------- FROM REDIS ----------------')
                    return json.loads(cached_data)
            
            
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
                
                if self.redis:
                    self.redis.set(
                        cache_key,
                        json.dumps(coordinates),
                        ex=cache_ttl
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