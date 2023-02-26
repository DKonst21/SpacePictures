import requests
import os
import datetime
import argparse

from datetime import datetime
from download_images import download_images, create_directory
from dotenv import load_dotenv


def fetch_epic_pictures_of_the_day(api_key_parameter):

    epic_pictures = get_list_pictures_params(api_key_parameter)

    for index_number, picture_info in enumerate(epic_pictures):
        image_name = picture_info['image']
        image_publication_date = datetime.fromisoformat(picture_info['date'])
        year = image_publication_date.strftime("%Y")
        month = image_publication_date.strftime("%m")
        day = image_publication_date.strftime("%d")
        actual_foto_url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image_name}.png"
        name_picture_template = os.path.join(get_default_catalog(), "{name}.png".format(name=image_name))
        download_images(actual_foto_url, name_picture_template, api_key_parameter)


def get_list_pictures_params(api_key_parameter):

    nasa_url = "https://api.nasa.gov/EPIC/api/natural/images"
    response = requests.get(nasa_url, params=api_key_parameter)
    response.raise_for_status()
    return response.json()


def get_default_catalog():

    parser = argparse.ArgumentParser()
    parser.add_argument('--catalog', default='epic')
    args = parser.parse_args()
    return args.catalog


def main():
    load_dotenv()
    create_directory(get_default_catalog())
    api_key_parameter = {'api_key': os.environ['NASA_API_KEY']}
    fetch_epic_pictures_of_the_day(api_key_parameter)


if __name__ == '__main__':
    main()
