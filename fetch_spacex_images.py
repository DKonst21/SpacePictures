import requests
import os
import argparse

from download_images import download_images, create_directory


def fetch_spacex_last_launch():

    for picture_number, picture in enumerate(create_response()):
        name_picture_template = "spaceX{number}.jpg".format(number=picture_number)
        picture_for_telegram = os.path.join("images", name_picture_template)
        download_images(picture, picture_for_telegram)


def create_response():
    launch_id = get_launch_id()
    if not launch_id:
        launch_id = "5eb87d47ffd86e000604b38a"
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def get_launch_id():
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id', default='5eb87d47ffd86e000604b38a')
    args = parser.parse_args()
    return args.launch_id


def main():
    create_directory('images')
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
