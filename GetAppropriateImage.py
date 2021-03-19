'''
get the prorteate image based on the weather state and dy time part
get good api website to provide images
send the device status (weather , day time pat)
get the appropreate image
resolution
send the image to the man
check if the photo has the same screen resolution if not choose another one
'''
#TODO improve image selecting by putt image for every state in a database  without need to api
import os
from datetime import datetime
import pyowm
import ctypes
import requests
import urllib.request as url
import api_keys as api_keys
import apiProcess
class api:
    OPEN_WEATHER_API_KEY=api_keys.OPEN_WEATHER_API_KEY
    UNSPLASH_API_KEY=api_keys.UNSPLASH_API_KEY
def getDeviceCity():
    ip_request=requests.get('https://get.geojs.io/v1/ip/geo.json')
    the_city=ip_request.json()['country']
    return  the_city

city=getDeviceCity()
def get_screen_reslution():
    ctypes.windll.user32.SetProcessDPIAware()
    user32 = ctypes.windll.user32
    screen_width=user32.GetSystemMetrics(0)
    screen_high=user32.GetSystemMetrics(1)
    screen_size=screen_width,screen_high
    return screen_size

def get_city():
    return city

def chcek_opw_api():
    pass



class GetDayTime:
    def __init__(self):
        self.get_current_hour=datetime.now().hour #TODO change to get the dateime to the city the got from open weather api

    def get_day_part(self):
        sunrisetime=99
        return (
            'sunrise' if sunrisetime==0
            else

            'morning' if sunrisetime<= self.get_current_hour <= sunrisetime+6
            else
            'afternoon' if 12 <= self.get_current_hour <=17
            else
            'evening' if 19 <= self.get_current_hour <= 22
            else
           'sunset' if 18 <= self.get_current_hour <= 19
            else
            'night'
        )

class GetWeatherState:

    def __init__(self):
        self.city=get_city()
        print('your city is {}'.format(self.city))
        owm = pyowm.OWM(api.OPEN_WEATHER_API_KEY)
        self.obs = owm.weather_at_place(get_city())
        # self.weather=pyowm.timeutils.now(timeformat='iso')
        self.current_city=owm.three_hours_forecast(self.city)
        # self.current_city=owm.weather_at_place(city)
        # self.current_city_check=owm.weather_at_place(city)




    def get_weather_state(self):
        w = self.obs.get_weather()
        return str(w.get_detailed_status())

    # def day_part(self):
    #     return (
    #         'morning' if self.current_city.
    #     )

class GetAppropriateImage:
    day_time_part=None
    weather_status=None
    API_KEY=None
    year_part=None
    unsplsh_image_api=None

    def __init__(self):
        city1=get_city()
        self.unsplsh_image_api=apiProcess.UnsplashImageApiProcess() #initlize the instance so we dont need to call it every time we use its methods
        self.day_time_part=GetDayTime().get_day_part()
        print('your day part is {}'.format(self.day_time_part))
        self.weather_status=GetWeatherState().get_weather_state()
        print('your weather state is  {}'.format(self.weather_status))
        self.API_KEY=api.UNSPLASH_API_KEY
        # self.get_location
        # self.get_device_resolution
        self.year_part='summer' #TODO make it dynamic



    def get_images_data(self):
        imgdat=self.unsplsh_image_api.data()
        return imgdat.data()

    def get_images_urls(self):
        image_urls=self.unsplsh_image_api.get_images_urls()
        return image_urls #TODO or return list of photo urls

    def get_image_files_list(self):
        image_files=[]
        for image_url in self.get_images_urls():
            file_name=str(image_url) + ".jpg"
            image_file=url.urlretrieve(image_url, file_name)
            image_files.append(image_file)
            # save_images_to_database(image_file)

        return image_files


    def get_single_image(self):
        image_urls=self.get_images_urls()
        list_size=len(image_urls)
        #random_number=random.randint(0,list_size) #TODO the problem is randrange(a, b+1).
        #mostlikephoto_url=self.unsplsh_image_api.get_most_liked_photo_url()
        mostlikephoto_url=self.unsplsh_image_api.get_random()
        # random_number=mostlikephoto
        # print('images got {}'.format(list_size))
        # print('image choosed {}'.format(random_number))
        # #single_image_url=image_urls[random_number] #TODO we invok the new deition of function so it does not effected in the top line :the first call brings diffiret size of list of second call for that i will save the image urls in list in this function
        image_file=url.urlretrieve(mostlikephoto_url, str('singleimage') + ".jpg")
        single_image_file=image_file #TODO check if file exicet
        # Database_conf.insert_img(mostlikephoto_url,self.weather_status,self.day_time_part,get_city())
        single_image_file=single_image_file[0] #TODO check if file exicet


        return single_image_file  #becuause it returens a tupel with file name and http reaquest so when set it ot 0 that mean it will return only the first tupel item which itis the file



def change_background_now():
    getApprpreateImageinstantce=GetAppropriateImage()
    appropreate_image=getApprpreateImageinstantce.get_single_image()
    file_path=os.path.abspath(appropreate_image)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, file_path , 0)
    # self.add_to_db()
    print('wait for download and set image ...')
    print('your background have been set')
if __name__ == '__main__':
    change_background_now()
