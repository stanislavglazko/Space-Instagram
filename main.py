import os
import argparse
from dotenv import load_dotenv
from PIL import Image
from instabot import Bot
from fetch_spacex import fetch_spacex_launch
from fetch_hubble import fetch_hubble_collection


def make_folder(folder):
    os.makedirs(folder, exist_ok=True)


def change_img(file):
    path_to_file = os.path.join('images', file)
    image = Image.open(path_to_file)
    for size in image.size:
        print(size)
        if size > 1080:
            image.thumbnail((1080, 1080))
    image.save(path_to_file, format="JPEG")
    image.close()


def post_to_instargam(file):
    path_to_file = os.path.join('images', file)
    load_dotenv()
    login = os.getenv("INSTAGRAM_LOGIN")
    password = os.getenv("INSTAGRAM_PASSWORD")
    change_img(file)
    bot = Bot()
    bot.login(username=login, password=password)
    bot.upload_photo(path_to_file)


def post_all_images_to_instagram(folder):
    for file in os.listdir(folder):
        print(file)
        post_to_instargam(file)


def get_parser():
    parser = argparse.ArgumentParser(description='Post photos of space to Instagram')
    parser.add_argument('-fn', '--flight_number', type=int, default=64)
    parser.add_argument('-cn', '--collection_name', type=str, default='spacecraft')
    return parser


def main():
    args = get_parser().parse_args()
    folder = 'images'
    make_folder(folder)
    fetch_spacex_launch(args.flight_number)
    fetch_hubble_collection(args.collection_name)
    post_all_images_to_instagram(folder)


if __name__ == '__main__':
    main()
