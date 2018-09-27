from flask import Flask, request

import requests
import json
import os

app = Flask(__name__)


@app.route("/v1/current/")
def current_weather():
    city = request.args.get('city')
    temp_info = get_temp_city(city)
    return json.dumps(temp_info)


@app.route("/v1/forecast/")
def forecast_weather():
    city = request.args.get('city')
    dt = request.args.get('dt')
    temp_info = get_temp_city(city, dt)
    return json.dumps(temp_info)


def get_temp_city(city: str, dt=None):

    result = {
        'city': '',
        'unit': 'celsius',
        'temperature': None
    }

    url = 'https://api.weather.yandex.ru/v1/forecast'

    lat, lon = get_geocode(city)

    raw_response = requests.get(url, headers={'X-Yandex-API-Key': '7f8c2899-ae3c-4f61-96eb-cf86f12ee051'}, params={
        'lang': 'ru_Ru', 'lat': lat, 'lon': lon})

    respons = json.loads(raw_response.text)

    result['city'] = city
    result['temperature'] = respons['fact']['temp']

    if dt:
        for item in respons['forecasts']:
            if dt == item['date']:
                result['temperature'] = item['parts']['day']['temp_avg']

    return result


def get_geocode(city):
    url = 'https://api.opencagedata.com/geocode/v1/json'

    raw_response = requests.get(url, params={'q': city, 'key': 'f93a94f9ac54424a8445d9e6612410de'})
    response = json.loads(raw_response.text)

    lat = response['results'][0]['bounds']['northeast']['lat']
    lng = response['results'][0]['bounds']['northeast']['lng']

    return lat, lng


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv('LISTEN_PORT', 5000)))
