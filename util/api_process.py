from weather.weather import OpenWeatherApi
from util.unsplash_image_process import UnsplashImageApi
 


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
