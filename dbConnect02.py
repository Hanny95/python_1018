import pymysql
import requests
import json

conn = None
cur = None


sql = ""

aipkey = 'aef453ab974739e7472d19f638f594d9'
cityList = ['Seoul', 'Tokyo', 'New York', 'Harbin']

api = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=kr'

conn = pymysql.connect(host='127.0.0.1',
                        user='root',
                        password='1234',
                        db='weatherdb',
                        charset='utf8')
cur = conn.cursor()

try:
   # for i in range(len(names)):
    for name in cityList:
        url = api.format(city=name, key=aipkey)
        res = requests.get(url)
        data = json.loads(res.text)

        weatherInfo = [data["base"], data["visibility"], data["dt"], data["timezone"], data["id"], data["name"], data["cod"], data["coord"]["lon"],
                       data["coord"]["lat"], data["weather"][0]["id"], data["weather"][0]["main"], data["weather"][0]["description"],
                       data["weather"][0]["icon"], data["main"]["temp"], data["main"]["feels_like"], data["main"]["temp_min"],
                       data["main"]["temp_max"], data["main"]["pressure"], data["main"]["humidity"], data["wind"]["speed"], data["wind"]["deg"],
                       data["clouds"]["all"], data["sys"]["type"], data["sys"]["id"], data["sys"]["country"],
                       data["sys"]["sunrise"], data["sys"]["sunset"]]

        sql = "INSERT INTO tbl_weather VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        cur.execute(sql, weatherInfo)

    conn.commit()

    conn.close()

except Exception as e:
    print(e)
    print('fail')

else:
    print('success')


# data["wind"]["gust"],