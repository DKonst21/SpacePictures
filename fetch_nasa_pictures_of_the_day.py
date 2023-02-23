import requests
import os
import argparse

from download_images import download_images, create_directory
from dotenv import load_dotenv


def fetch_nasa_pictures_of_the_day(api_key_foto):

    nasa_pictures_of_the_day = get_response_with_api_key(api_key_foto).json()
    name_picture_template = "nasa_apod{number}.jpg".format(number=nasa_pictures_of_the_day['date'])
    picture_for_telegram = os.path.join(get_default_settings(), name_picture_template)
    download_images(nasa_pictures_of_the_day['url'], picture_for_telegram, api_key_foto)


def get_response_with_api_key(api_key_foto):
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=api_key_foto)
    response.raise_for_status()
    return response


def get_default_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument('--catalog', default='APOD')
    args = parser.parse_args()
    return args.catalog


def main():
    load_dotenv()
    create_directory(get_default_settings())
    api_key_foto = {'api_key': os.environ['NASA_API_KEY']}
    fetch_nasa_pictures_of_the_day(api_key_foto)


if __name__ == '__main__':
    main()
