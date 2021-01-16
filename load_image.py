import os
import requests


def load_img(filename, url):
    response = requests.get(url)
    response.raise_for_status()
    path_to_file = os.path.join('images', filename)
    print(path_to_file)
    with open(path_to_file, 'wb') as file:
        file.write(response.content)
