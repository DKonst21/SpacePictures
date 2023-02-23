import requests
import os
import datetime
import argparse

from datetime import datetime
from download_images import download_images, create_directory
from dotenv import load_dotenv


def fetch_epic_pictures_of_the_day(api_key_foto):
    epic_pictures = get_response_with_api_key(api_key_foto).json()

    for index_number, dict_info_epic_pictures in enumerate(epic_pictures):
        massiv_image = dict_info_epic_pictures['image']
        massiv_date = datetime.fromisoformat(dict_info_epic_pictures['date'])
        year = massiv_date.strftime("%Y")
        month = massiv_date.strftime("%m")
        day = massiv_date.strftime("%d")
        url_actual_foto = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{massiv_image}.png"
        name_epic_picture_template = os.path.join(get_default_settings(), "{name}.png".format(name=massiv_image))
        download_images(url_actual_foto, name_epic_picture_template, api_key_foto)


def get_response_with_api_key(api_key_foto):
    nasa_url = "https://api.nasa.gov/EPIC/api/natural/images"
    response = requests.get(nasa_url, params=api_key_foto)
    response.raise_for_status()
    return response


def get_default_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument('--catalog', default='epic')
    args = parser.parse_args()
    return args.catalog


def main():
    load_dotenv()
    create_directory(get_default_settings())
    api_key_foto = {'api_key': os.environ['NASA_API_KEY']}
    fetch_epic_pictures_of_the_day(api_key_foto)


if __name__ == '__main__':
    main()
