import requests
import json
import random
from datetime import datetime
import util.api_keys as api_keys
import pyowm

class DeviceLocation:
    @staticmethod
    def get_city():
        ip_request = requests.get('https://get.geojs.io/v1/ip/geo.json')
        return ip_request.json()['country']

class OpenWeatherApi:
    def __init__(self):
        self.api_key = api_keys.OPEN_WEATHER_API_KEY
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

class UnsplashImageApi:
    def __init__(self):
        self.api_key = api_keys.UNSPLASH_API_KEY

    def fetch_data(self, query='night clear sky'):
        url = f'https://api.unsplash.com/search/photos?per_page=30&order_by=popular&query={query}&client_id={self.api_key}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_image_urls(self, data):
        return [
            img_data['urls']['regular']
            for img_data in data['results']
            if img_data['height'] < img_data['width']
        ]

    def get_most_liked_photo_url(self, data):
        most_liked_photo = max(
            data['results'], key=lambda img_data: img_data['likes']
        )
        return most_liked_photo['urls']['full']

    def get_random_photo_url(self, data):
        photo = random.choice(data['results'])
        return photo['urls']['full']

if __name__ == '__main__':
    weather_api = OpenWeatherApi()
    unsplash_api = UnsplashImageApi()

    weather_status = weather_api.get_weather_status()
    day_part = weather_api.get_day_part()
    print(f"Weather: {weather_status}, Day Part: {day_part}")

    data = unsplash_api.fetch_data()
    image_urls = unsplash_api.get_image_urls(data)
    most_liked_photo_url = unsplash_api.get_most_liked_photo_url(data)
    random_photo_url = unsplash_api.get_random_photo_url(data)

    print(f"Most Liked Photo URL: {most_liked_photo_url}")
    print(f"Random Photo URL: {random_photo_url}")
    print(f"Image URLs: {image_urls[:5]}")  # Print first 5 image URLs for brevity
