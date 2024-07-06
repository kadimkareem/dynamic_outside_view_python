import datetime
import json
import pyowm

from util.api_keys import OPEN_WEATHER_API_KEY
from util.device_location import DeviceLocation
class OpenWeatherApi:
    def __init__(self):
        self.api_key = OPEN_WEATHER_API_KEY
        self.location = DeviceLocation.get_city()
        self.owm = pyowm.OWM(self.api_key)
        self.weather = self.owm.weather_at_place(self.location).get_weather()
        self.sunrise_time = self.weather.get_sunrise_time()

    def get_weather_status(self):
        return self.weather.get_detailed_status()

    def get_day_part(self):
        current_hour = datetime.now().hour
        return (
            'sunrise' if self.sunrise_time == 0
            else 'morning' if self.sunrise_time <= current_hour <= self.sunrise_time + 6
            else 'afternoon' if 12 <= current_hour <= 17
            else 'evening' if 19 <= current_hour <= 22
            else 'sunset' if 18 <= current_hour <= 19
            else 'night'
        )

    @staticmethod
    def get_cities_list():
        with open("files/world-cities_json.json", "r") as jsonfile:
            return [f"{i['country']} {i['name']} {i['subcountry']}" for i in json.load(jsonfile)]
