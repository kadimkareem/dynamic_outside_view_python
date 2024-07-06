class DayTime:
    def __init__(self, city_hour):
        self.city_hour = city_hour

    def get_day_part(self):
        if 0 <= self.city_hour <= 5:
            return 'night'
        elif 6 <= self.city_hour <= 11:
            return 'morning'
        elif 12 <= self.city_hour <= 17:
            return 'afternoon'
        elif 18 <= self.city_hour <= 19:
            return 'sunset'
        elif 20 <= self.city_hour <= 23:
            return 'evening'

