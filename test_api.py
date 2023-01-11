# pylint: disable=missing-docstring,invalid-name
import requests

url = 'http://api.openweathermap.org/data/2.5/forecast?'
response = requests.get(
    url,
    params = {
        'lat': '44.34',
        'lon': '10.99',
        'appid': 'f5191f73c320e67df9461049016befe3'
    }).json()

temp = response['list'][0]['main']['temp']
date = response['list'][0]['dt_txt']
weather = response['list'][0]['weather'][0]['main']


print(weather)

print(temp)

print(date)
