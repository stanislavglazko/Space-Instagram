import os
import requests


def load_img(filename, url, folder='images'):
    response = requests.get(url)
    response.raise_for_status()
    filepath = os.path.join(folder, filename)
    with open(filepath, 'wb') as file:
        file.write(response.content)
