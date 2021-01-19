import os
import requests
from load_image import load_img


def get_image_extension(link):
    _, image_extension = os.path.splitext(link)
    return image_extension


def fetch_hubble_image(image_id, folder='images'):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(url, verify=False)
    response.raise_for_status()
    link_from_response = response.json()['image_files'][-1]['file_url']
    link = f'http:{link_from_response}'
    extension = get_image_extension(link)
    filename = f'{image_id}.{extension}'
    load_img(filename, link, folder=folder)


def fetch_hubble_collection(collection_name='spacecraft', folder='images'):
    url = 'http://hubblesite.org/api/v3/images'
    payload = {
        'page': 'all',
        'collection_name': collection_name
    }
    response = requests.get(url, verify=False, params=payload)
    response.raise_for_status()
    for image in response.json():
        fetch_hubble_image(image_id=image['id'], folder=folder)
