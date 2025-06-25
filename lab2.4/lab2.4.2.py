import requests
import pandas as pd
import matplotlib.pyplot as plt

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = "78PZMFSNEVBBBS9FR6M2C8FP9"

    def get_api(self, location, start_date, end_date, step='daily'):
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start_date}/{end_date}"
        params = {
            'unitGroup': 'metric',
            'key': self.api_key,
            'contentType': 'json',
            'include': step
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_values(self, location, start_date, end_date, step='daily'):
        json_data = self.get_api(location, start_date, end_date, step)
        dates, temperature, humidity, windspeed, cloudcover, dew = [], [], [], [], [], []

        for day in json_data['days']:
            dates.append(day['datetime'])
            temperature.append(day.get('temp', None))
            humidity.append(day.get('humidity', None))
            windspeed.append(day.get('windspeed', None))
            cloudcover.append(day.get('cloudcover', None))
            dew.append(day.get('dew', None))

        return dates, {
            'Temperature °C': temperature,
            'Humidity': humidity,
            'Windspeed': windspeed,
            'Cloudcover': cloudcover,
            'Dew': dew
        }

class WeatherPlotter:
    def __init__(self, dates, data_dict, colors=None):
        self.dates = dates
        self.data_dict = data_dict
        self.colors = colors if colors else ['red', 'blue', 'green', 'orange', 'pink']

    def plot(self):
        plt.figure(figsize=(12, 6))
        for idx, (label, values) in enumerate(self.data_dict.items()):
            plt.plot(self.dates, values, label=label, color=self.colors[idx % len(self.colors)])
        
        plt.xlabel("Time")
        plt.ylabel("Weather values")
        plt.title("Weather Logger Chart")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.xticks(rotation=45)
        plt.show()

weather_api = WeatherAPI("78PZMFSNEVBBBS9FR6M2C8FP9")

location = "Kyiv"
start_date = "2024-06-01"
end_date = "2024-06-07"
dates, data = weather_api.get_values(location, start_date, end_date)

plotter = WeatherPlotter(dates, data)
plotter.plot()  