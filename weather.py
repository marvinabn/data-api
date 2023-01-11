# pylint: disable=missing-module-docstring

import sys
#import urllib.parse
import requests

BASE_URI = "https://weather.lewagon.com"
KEY= 'f5191f73c320e67df9461049016befe3'

def search_city(query):
    '''Look for a given city. If multiple options are returned, have the user choose between them.
       Return one city (or None)
    '''
    url = f"{BASE_URI}/geo/1.0/direct?q={query}&limit=100"

    response = requests.get(url).json()
    if len(response) > 1:
        print("Multiple matches found, which city did you mean?")
        for i, e in enumerate(response):
            print(f"{i+1} {e['name']} {e['country']}")
        option = int(input("Option?\n> ")) -1
        city = response[option]
        city_info = {"name": city["name"], "lat": city['lat'], "lon": city['lon']}
        print(f"Here is the weather in {city_info['name']}:")
        return city_info

    if len(response) == 1:
        city = response[0]
        city_info = {"name": city["name"], "lat": city['lat'], "lon": city['lon']}
        print(f"Here is the weather in {city_info['name']}:")
        return city_info

    return None




def weather_forecast(lat, lon):
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={KEY}"

    response = requests.get(url).json()


    for index in range(0, 40, 8):
        temp = response['list'][index]['main']['temp']
        temp = float(temp) - 273.15
        temp = round(temp, 1)
        weather = response['list'][index]['weather'][0]['main']
        date = response['list'][index]['dt_txt']
        date = date [0:10]
        var = []
        var.append([f"{date}: {weather} {temp}°C"])
        print(f"{date}: {weather} {temp}°C")
    return response['list']


def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    search_city(query)

if __name__ == '__main__':
    try:
        while True:
            main()

    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
