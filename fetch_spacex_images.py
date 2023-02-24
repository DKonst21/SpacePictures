import requests
import os
import argparse

from download_images import download_images, create_directory


def fetch_spacex_last_launch(launch_id, catalog):

    for picture_number, picture in enumerate(get_links_of_pictures(launch_id)):
        name_picture_template = "spaceX{number}.jpg".format(number=picture_number)
        picture_for_telegram = os.path.join(catalog, name_picture_template)
        download_images(picture, picture_for_telegram, launch_id)


def get_links_of_pictures(launch_id):

    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def get_default_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id', default='5eb87d47ffd86e000604b38a')
    parser.add_argument('--catalog', default='images')
    return parser.parse_args()


def main():
    args = get_default_arguments()
    create_directory(args.catalog)
    fetch_spacex_last_launch(args.launch_id, args.catalog)


if __name__ == '__main__':
    main()
