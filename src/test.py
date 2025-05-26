from infrastructure.openmeteo import OpenMeteoService
import asyncio

service = OpenMeteoService()

print(asyncio.run(service.get_weather_forecast_by_city_async(city='Moscow')))


# def a():
#     return {
#         'a': 1,
#         'b': 2
#     }
    
# def b(a, b, c=3):
#     print(a, b, c)
    
    
# data = a()
# b(**data, c=123)
# b(**a(), c= 123)


# import httpx
# import asyncio

# async def get_city_coordinates(city: str):
#     url = "https://nominatim.openstreetmap.org/search"
#     params = {
#         "q": city,
#         "format": "json",
#         "limit": 1
#     }
    
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, params=params)
#         data = response.json()
#         if data:
#             return {
#                 "latitude": float(data[0]["lat"]),
#                 "longitude": float(data[0]["lon"])
#             }
#         return None


# print(asyncio.run(get_city_coordinates('Nurlat')))


# from infrastructure.open_meteo import OpenMeteoService

# CITY_COORDINATES = {
#     "Москва": {"latitude": 55.7558, "longitude": 37.6176},
#     "Санкт-Петербург": {"latitude": 59.9343, "longitude": 30.3351}
# }

# # CITY_COORDINATES['Москва']['latitude'], 
# # CITY_COORDINATES['Москва']['longitude']

# import asyncio

# service = OpenMeteoService()
# result = asyncio.run(service.get_weather_forecast_by_coordinates(
#     latitude=55.7558,
#     longitude=37.6176
# ))


# print(result)