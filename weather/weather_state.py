import pyowm
from main import API

class WeatherState:
    def __init__(self, city):
        self.city = city
        owm = pyowm.OWM(API.OPEN_WEATHER_API_KEY)
        self.obs = owm.weather_at_place(city)

    def get_weather_state(self):
        weather = self.obs.get_weather()
        return weather.get_detailed_status()

