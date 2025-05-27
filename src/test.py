from infrastructure.openmeteo import OpenMeteoService
import asyncio


service = OpenMeteoService('https://api.open-meteo.com/v1/forecast', None)

print(asyncio.run(service.get_weather_forecast_by_coordinates_async(
    latitude=52.510885,
    longitude=13.3989367
)))