# openweathermap.org 접속
# openweathermap API(Application Programming Interface)
# openweather API key (키값이 있어야 데이터를 가져올 수 있다)
# requests 모듈 : 데이터 로드(data load)
# json 모듈 : 데이터 분석


import requests
import json


aipkey = 'aef453ab974739e7472d19f638f594d9'
cityList = ['Seoul', 'Tokyo', 'New York', 'Harbin']
# http:// 프로토콜 추가
api = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=kr'

for name in cityList:
    url = api.format(city=name, key=aipkey)
    res = requests.get(url)
    data = json.loads(res.text)
    print(data)

    print('='*50)
    print(f'base: {data["base"]}')
    print(f'visibility: {data["visibility"]}')
    print(f'dt: {data["dt"]}')
    print(f'timezone: {data["timezone"]}')
    print(f'id: {data["id"]}')
    print(f'name: {data["name"]}')
    print(f'cod: {data["cod"]}')
    print(f'coord lon: {data["coord"]["lon"]}')
    print(f'coord lat: {data["coord"]["lat"]}')
    print(f'weather id: {data["weather"][0]["id"]}')
    print(f'weather main: {data["weather"][0]["main"]}')
    print(f'weather description: {data["weather"][0]["description"]}')
    print(f'weather icon: {data["weather"][0]["icon"]}')
    print(f'main temp: {data["main"]["temp"]}')
    print(f'main feels_like: {data["main"]["feels_like"]}')
    print(f'main temp_min: {data["main"]["temp_min"]}')
    print(f'main temp_max: {data["main"]["temp_max"]}')
    print(f'main pressure: {data["main"]["pressure"]}')
    print(f'main humidity: {data["main"]["humidity"]}')
    print(f'wind speed: {data["wind"]["speed"]}')
    print(f'wind deg: {data["wind"]["deg"]}')
    # print(f'wind gust: {data["wind"]["gust"]}')
    print(f'clouds all: {data["clouds"]["all"]}')
    print(f'sys type: {data["sys"]["type"]}')
    print(f'sys id: {data["sys"]["id"]}')
    print(f'sys country: {data["sys"]["country"]}')
    print(f'sys sunrise: {data["sys"]["sunrise"]}')
    print(f'sys sunset: {data["sys"]["sunset"]}')

