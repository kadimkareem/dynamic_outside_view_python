import requests

class DeviceLocation:
    @staticmethod
    def get_city():
        ip_request = requests.get('https://get.geojs.io/v1/ip/geo.json')
        return ip_request.json()['country']

