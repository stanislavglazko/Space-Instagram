import os
import argparse
from dotenv import load_dotenv
from PIL import Image
from instabot import Bot
from fetch_spacex import fetch_spacex_launch
from fetch_hubble import fetch_hubble_collection


def make_folder(folder):
    os.makedirs(folder, exist_ok=True)


def change_img(file, folder='images'):
    path_to_file = os.path.join(folder, file)
    image = Image.open(path_to_file)
    critical_size = 1080
    for size in image.size:
        if size > critical_size:
            image.thumbnail((1080, 1080))
            break
    image.save(path_to_file, format="JPEG")
    image.close()


def post_to_instargam(login, password, file, folder='images'):
    path_to_file = os.path.join(folder, file)
    change_img(file, folder=folder)
    bot = Bot()
    bot.login(username=login, password=password)
    bot.upload_photo(path_to_file)


def post_all_images_to_instagram(login, password, folder='images'):
    for file in os.listdir(folder):
        post_to_instargam(login, password, file, folder=folder)


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
