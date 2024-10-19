import requests
from dotenv import load_dotenv
import os

load_dotenv()
GEOCODE_KEY = os.getenv('GEOCODE_KEY')


def geocoding(cord, request):
    geocode_api_server = 'https://geocode-maps.yandex.ru/1.x/'
    geocode_params = {
        'apikey': GEOCODE_KEY,
        'geocode': request,
        'lang': 'ru_RU',
        'll': cord,
        'format': 'json'
    }

    response = requests.get(geocode_api_server, params=geocode_params)
    if not response:
        return {'error': 'Not Found'}
    json_response = response.json()
    try:
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
    except IndexError:
        return {'error': 'Not Found'}
    toponym_cord = list(map(float, toponym["Point"]["pos"].split()))
    address = toponym['metaDataProperty']['GeocoderMetaData']['AddressDetails']['Country']['AddressLine']
    result = {'coordinates': toponym_cord, 'address': address}
    return result
