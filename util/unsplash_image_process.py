import random
from api_keys import UNSPLASH_API_KEY
import requests

class UnsplashImageApi:
    def __init__(self):
        self.api_key = UNSPLASH_API_KEY

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
