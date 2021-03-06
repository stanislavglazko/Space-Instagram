import argparse
import os
from instabot import Bot
from PIL import Image
from dotenv import load_dotenv
from fetch_hubble import fetch_hubble_collection
from fetch_spacex import fetch_spacex_launch


def make_folder(folder):
    os.makedirs(folder, exist_ok=True)


def change_img(filename, folder='images'):
    filepath = os.path.join(folder, filename)
    image = Image.open(filepath)
    critical_size = 1080
    for size in image.size:
        if size > critical_size:
            image.thumbnail((1080, 1080))
            break
    image.save(filepath)
    image.close()


def post_to_instargam(login, password, filename, folder='images'):
    filepath = os.path.join(folder, filename)
    change_img(filename, folder=folder)
    bot = Bot()
    bot.login(username=login, password=password)
    bot.upload_photo(filepath)


def post_all_images_to_instagram(login, password, folder='images'):
    for filename in os.listdir(folder):
        post_to_instargam(login, password, filename, folder=folder)


def get_parser():
    parser = argparse.ArgumentParser(description='Post photos of space to Instagram')
    parser.add_argument('-fn', '--flight_number', type=int, default=64)
    parser.add_argument('-cn', '--collection_name', type=str, default='spacecraft')
    parser.add_argument('-f', '--folder', type=str, default='images')
    return parser


def main():
    load_dotenv()
    login = os.getenv("INSTAGRAM_LOGIN")
    password = os.getenv("INSTAGRAM_PASSWORD")
    args = get_parser().parse_args()
    folder = args.folder
    make_folder(folder)
    fetch_spacex_launch(args.flight_number, folder)
    fetch_hubble_collection(args.collection_name, folder)
    post_all_images_to_instagram(login, password, folder)


if __name__ == '__main__':
    main()
