import os
import requests
from load_image import load_img


def fetch_spacex_launch(flight_number=64, folder='images'):
    url = 'https://api.spacexdata.com/v3/launches'
    payload = {'flight_number': flight_number}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    links = response.json()[0]['links']['flickr_images']
    for img_number, img in enumerate(links, 1):
        load_img(f'spacex{str(img_number)}.jpg', img, folder)
