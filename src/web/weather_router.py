from datetime import datetime
import json
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse

from application.services.weather_service import WeatherService
from config import templates


weather_router = APIRouter(tags=['weather'], prefix='/weather')


@weather_router.get('/main', response_class=HTMLResponse)
async def main_page(
        request: Request,
        city: str=None,
        weather_service: WeatherService = Depends()
    ):
    history = []
    cookie_history = request.cookies.get("weather_history")
    if cookie_history:
        history = json.loads(cookie_history)
    
    is_non_existent_city = False
    if city:
        # Получаем прогноз
        forecast = await weather_service.get_forecast_async(city=city)
        
        if forecast:
            # Добавляем новый запрос в историю            
            new_entry = {
                "city": city,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "temp": forecast.temperature if forecast else None
            }

            # Обновляем историю (максимум 5 последних запросов)
            history = [new_entry] + [h for h in history if h["city"] != city][:4]
        else:
            is_non_existent_city = True
    
    
    print(is_non_existent_city, 'is_non_existent_city')
    response = templates.TemplateResponse(
        'weather.html',
        {
            'request': request,
            'city': city,
            'forecast': forecast,
            'is_non_existent_city': is_non_existent_city,
            'history': history
        }
    )
    
    if history:
        response.set_cookie(
            key="weather_history",
            value=json.dumps(history),
            max_age=30*24*60*60,
            httponly=True,
            secure=True,
            samesite="lax"
        )

    return response