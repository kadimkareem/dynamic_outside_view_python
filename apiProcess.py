import requests
import json
import random
from datetime import datetime
import api_keys
import pyowm

# import astral lib for getting sunlight position on the earth
weatherstate=None
daypar=None


class GetDeviceLocation:
    def the_city(self):
        ip_request=requests.get('https://get.geojs.io/v1/ip/geo.json')
        the_city=ip_request.json()['country']
        return  the_city



class OperWeatherApiProcess:
    API_KIY=api_keys.OPEN_WEATHER_API_KEY
    # location='istanbul'
    owm=None



    def __init__(self):
        self.location=GetDeviceLocation().the_city()
        owm=self.owm =pyowm.OWM(self.API_KIY)
        obs = owm.weather_at_place(self.location)
        self.w = obs.get_weather()
        self.sunrisetime=self.w.get_sunrise_time()



    def GetWeather(self):
        w=self.w
        return w.get_detailed_status()


    def get_day_part(self):
        get_current_hour=datetime.now().hour
        sunrisetime=self.sunrisetime
        return (
            'sunrise' if sunrisetime==0
            else

            'morning' if sunrisetime<= get_current_hour <= sunrisetime+6
            else
            'afternoon' if 12 <= get_current_hour <=17
            else
            'evening' if 19 <= get_current_hour <= 22
            else
           'sunset' if 18 <= get_current_hour <= 19
            else
            'night'
        )

    def get_cities_list(self):
        with open("files/world-cities_json.json", "r") as jsonfile:
            jsondata=json.load(jsonfile)

        city_list=[]
        for i in jsondata:
            city=str(i['country'])+str(i['name'])+str(i['subcountry'])
            city_list.append(city)

        return city_list


class WeatherState(OperWeatherApiProcess):
    def __init__(self):
        pass

    def weather_state(self):
        owm=self.owm
        obs = owm.weather_at_place(self.location)

class UnsplashImageApiProcess:
    owp=OperWeatherApiProcess()
    def check_unsplashimage_api(url):
        try:
            response=requests.get(url)
            if response.status_code !=200:
                return print('there is problem in api : no data fetched')
            else: print(response.status_code)

        except requests.exceptions.RequestException as error:
            print(error)

    def data(self):
        r = requests.get('https://api.unsplash.com/search/photos?per_page=30&order_by=popular&query=night clear sky&client_id=' + api_keys.UNSPLASH_API_KEY + '') #TODO change the params
        data = r.json()
        return data

    def get_images_urls(self):
        image_urls=[]
        for img_data in self.data()['results']:
            # img_url = img_data['cover_photo']['urls']['raw'] if the link containes 'collection' instaed of 'photo-> the collection is grup of photos for spicify user or specify tag contains many photos'
            if img_data['height']<img_data['width']: #get only the photos that have
                # print(img_data['height'],img_data['width']) //
                img_url = img_data['urls']['regular'] #TODO change it to 'raw'
                image_urls.append(img_url)
            #dermin image resolution
        # print('we got {} urls'.format(len(image_urls)))
        return image_urls #TODO or return list of photo urls

    def get_most_liked_photo_url(self):
        mostlikedphotolist={}
        for results in self.data()['results']:
            likes=int(results['likes'])
            url=results['urls']['full']
            mostlikedphotolist[likes]=url #the perfect method to append to dictionary
            # print(likes) // most liked image
        #     likeed=int(results['likes']),results['urls']
        #     mostlikedphotolist.append(likes)
        # mostlikedphoto=mostlikedphotolist[0]
        maxmostlikedphoto=max(mostlikedphotolist.keys())  #choosing the most liked photo
        #randommostlikedphoto=random.choice([i for i in mostlikedphotolist.keys()]) #chosing random most liked photo
        # print('random most like chosed {}'.format(maxmostlikedphoto))
        mostlikedphoto=mostlikedphotolist[maxmostlikedphoto]
        return mostlikedphoto

    def get_random(self):
        mostlikedphotolist={}
        for results in self.data()['results']:
            likes=int(results['likes'])
            url=results['urls']['full']
            mostlikedphotolist[likes]=url #the perfect method to append to dictionary
            # print(likes)
        #     likeed=int(results['likes']),results['urls']
        #     mostlikedphotolist.append(likes)
        # mostlikedphoto=mostlikedphotolist[0]
        #maxmostlikedphoto=max(mostlikedphotolist.keys())  #choosing the most liked photo
        randommostlikedphoto=random.choice([i for i in mostlikedphotolist.keys()]) #chosing random most liked photo
        print('random most like chosed {}'.format(randommostlikedphoto))
        mostlikedphoto=mostlikedphotolist[randommostlikedphoto]
        return mostlikedphoto







if __name__ == '__main__':

    # ow=OperWeatherApiProcess()
    # usplash=UnsplashImageApiProcess()
    opw=OperWeatherApiProcess()
    # print(usplash.get_most_liked_photo_url())
    # print(usplash.get_images_urls())
    print(opw.sunrisetime)
    print(opw.location)

    # for results in usplash.data()['results']:
    #     if results['height']<results['width'] :
    #         print(results['height'],results['width'],results['tags'],results['color'],results['urls'])
    # print(ow.get_cities_list())



