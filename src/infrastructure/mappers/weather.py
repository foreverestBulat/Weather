from application.dto.weather import WeatherForecastDTO
from infrastructure.models.openmeteo_response import OpenMeteoResponse


class WeatherMapper:
    @staticmethod
    def map_openmeteo_to_dto(
        city: str,
        api_data: OpenMeteoResponse
    ) -> WeatherForecastDTO:
        return WeatherForecastDTO(
            city=city,
            latitude=api_data.latitude,
            longitude=api_data.longitude,
            time=api_data.hourly['time'],
            temperature=api_data.hourly['temperature_2m'],
            weather_str=WeatherMapper.convert_weather_code_list_to_str_list(
                weather_codes=api_data.hourly['weathercode']
            ),
            count=len(api_data.hourly['time'])
        )
    
    @staticmethod
    def convert_weather_code_list_to_str_list(weather_codes: list[int]):
        result = []
        for code in weather_codes:
            result.append(WeatherMapper.get_weather_description(code))
        return result
    
    @staticmethod
    def get_weather_description(weather_code: int) -> str:
        """Преобразует WMO код погоды в текстовое описание"""
        descriptions = {
            0: "Чистое небо",
            1: "В основном ясно",
            2: "Переменная облачность",
            3: "Пасмурно",
            45: "Туман",
            48: "Осаждающийся инейный туман",
            51: "Слабый мелкий дождь",
            53: "Умеренный мелкий дождь",
            55: "Сильный мелкий дождь",
            56: "Лёгкий замораживающий дождь",
            57: "Плотный замораживающий дождь",
            61: "Слабый дождь",
            63: "Умеренный дождь",
            65: "Сильный дождь",
            66: "Лёгкий ледяной дождь",
            67: "Сильный ледяной дождь",
            71: "Слабый снегопад",
            73: "Умеренный снегопад",
            75: "Сильный снегопад",
            77: "Снежные зерна",
            80: "Слабый ливень",
            81: "Умеренный ливень",
            82: "Сильный ливень",
            85: "Небольшой снегопад",
            86: "Сильный снегопад",
            95: "Гроза (слабая или умеренная)",
            96: "Гроза с небольшим градом",
            99: "Гроза с сильным градом"
        }
        return descriptions.get(weather_code, "Неизвестная погода")
            