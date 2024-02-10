from datetime import datetime, timedelta
import requests
import json

class WeatherForecast:
    # Parametry wejściowe
    URL = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
    latitude = 53.14694290777315
    longitude = 18.09934250841188

    def __init__(self):
        self.open_file()

    def __repr__(self):
        return f"WeatherForecast Object"

    def __getitem__(self, item):
        return self.json_dict.get(item, [])

    def __setitem__(self, key, value):
        self.add_information(key, value)

    def __iter__(self):
        return iter(self.json_dict.items())

    def items(self):
        while json_dict != None:
            with open("date.json") as file:
                self.json_dict = json.load(file)
            yield print(file.readline())


    def add_information(self, data, rain):
        if data in self.json_dict:
            self.json_dict[data].append(rain)
        else:
            self.json_dict[data] = [rain]

    def _get_url(self, searched_date):
        return self.URL.format(latitude=self.latitude, longitude=self.longitude, searched_date=searched_date)

    def search_date(self, searched_date):
        try:
            datetime.strptime(searched_date, "%Y-%m-%d")
        except ValueError:
            print("Podałeś złą datę - wybieram dzień jutrzejszy")
            searched_date = str(datetime.today().date() + timedelta(days=1))
        print(f"Wykorzystana data: {searched_date}")
        return searched_date

    def get_response(self, searched_date):
        try:
            response = requests.get(self._get_url(searched_date))
            code = response.status_code
            # Weryfikacja czy odpowiedź z serwera ma kod 200
            if code != 200:
                print(f"Bład serwera spróbuj później")
            else:
                rain_sum = response.json()["daily"]["rain_sum"][0]
                self.json_dict[searched_date] = f"{rain_sum}"
                return rain_sum

        except KeyError:
            print(f"W bazie brakuje danych o które pytasz")

    def get_information_about_rain(self, rain_sum):
        if rain_sum > 0.0:
            print("Będzie padać")
        elif rain_sum == 0.0:
            print("Nie będzie padać")
        else:
            print("Nie wiem")

    def verify_information_about_rain(self, value):
        if float(value) > 0:
            print(f"Będzie padać")
        elif float(value) == 0:
            print(f"Nie będzie Padać")
        else:
            print(f"Nie wiem czy będzie padać")


    def verify_date(self, searched_date):
        if searched_date in self.json_dict.keys():
            for key, value in self.json_dict.items():
                keys = key
                if searched_date == keys:
                    print(f"{key}:{value}")
                    self.verify_information_about_rain(value)
                    return 0
                else:
                    continue

    def open_file(self):
        try:
            with open("date.json") as file:
                self.json_dict = json.load(file)
        except FileNotFoundError:
            self.json_dict = {}

    def save_file(self):
        with open('date.json', 'w') as file:
            json.dump(self.json_dict, file)



weather_forecast = WeatherForecast()

# print(weather_forecast)
# # weather_forecast.add_information("2023-05-01", "0.0")
# # weather_forecast.add_information("2023-05-02", "0.2")
# print(weather_forecast.json_dict)
# print(weather_forecast["2023-04-25"])
#
# print(weather_forecast.items())


