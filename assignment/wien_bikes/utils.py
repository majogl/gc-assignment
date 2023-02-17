import requests
from time import sleep
from wien_bikes.config import ADDRESS_RESOLVE_URL

def get_address_from_coords(lat, lon):
    resp = requests.get(f'{ADDRESS_RESOLVE_URL}?latitude={lat}&longitude={lon}')
    sleep(0.03) # Delay needed due to API limitations. Without it, I kept gettin 429 TOO MANY REQUESTS status code
    return resp.json()['data']['name']
