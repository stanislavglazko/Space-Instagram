import os
import requests
from load_image import load_img


def get_image_extension(link):
    link = link.rstrip('/').split('.')
    return link[-1]


def get_hubble_image(image_id):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(url, verify=False)
    response.raise_for_status()
    link = 'http:' + response.json()['image_files'][-1]['file_url']
    extension = get_image_extension(link)
    filename = f'{image_id}.{extension}'
    print(link)
    load_img(filename, link)


def get_hubble_collection(collection_name='spacecraft'):
    url = 'http://hubblesite.org/api/v3/images'
    payload = {
        'page': 'all',
        'collection_name': collection_name
    }
    response = requests.get(url, verify=False, params=payload)
    response.raise_for_status()
    for image in response.json():
        print(image['id'])
        get_hubble_image(image_id=image['id'])
