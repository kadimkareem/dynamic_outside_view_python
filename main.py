import os
from datetime import datetime
from util.day_time import DayTime
from weather.weather_state import WeatherState
import ctypes
import requests
import urllib.request as url
from util.image_provider import ImageProvider


def get_device_city():
    ip_request = requests.get('https://get.geojs.io/v1/ip/geo.json')
    city = ip_request.json()['country']
    return city

def get_screen_resolution():
    ctypes.windll.user32.SetProcessDPIAware()
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    return screen_width, screen_height


def change_background():
    city = get_device_city()
    city_hour = datetime.now().hour
    day_time = DayTime(city_hour).get_day_part()
    weather_status = WeatherState(city).get_weather_state()

    image_provider = ImageProvider(day_time, weather_status,url=url)
    appropriate_image = image_provider.get_appropriate_image()
    
    file_path = os.path.abspath(appropriate_image)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, file_path, 0)
    print('Background image has been set.')

if __name__ == '__main__':
    change_background()
