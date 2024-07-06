from util.api_keys import UNSPLASH_API_KEY
class ImageProvider:
    def __init__(self, day_time_part, weather_status,url):
        self.day_time_part = day_time_part
        self.weather_status = weather_status
        self.unsplash_api = UNSPLASH_API_KEY

    def get_image_urls(self):
        return self.unsplash_api.get_images_urls()

    def download_image(self, image_url):
        file_name = f"{image_url}.jpg"
        return self.url.urlretrieve(image_url, file_name)

    def get_appropriate_image(self):
        image_urls = self.get_image_urls()
        most_liked_photo_url = self.unsplash_api.get_random()
        image_file = self.download_image(most_liked_photo_url)
        return image_file[0]  # Return file path
