import requests
import os
import argparse

from download_images import download_images, create_directory
from dotenv import load_dotenv


def fetch_nasa_pictures_of_the_day(api_key_parameter):

    nasa_pictures_of_the_day = get_list_nasa_pictures_params(api_key_parameter)
    name_picture_template = "nasa_apod{number}.jpg".format(number=nasa_pictures_of_the_day['date'])
    picture_path = os.path.join(get_default_catalog(), name_picture_template)
    download_images(nasa_pictures_of_the_day['url'], picture_path, api_key_parameter)


def get_list_nasa_pictures_params(api_key_parameter):

    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=api_key_parameter)
    response.raise_for_status()
    return response.json()


def get_default_catalog():

    parser = argparse.ArgumentParser()
    parser.add_argument('--catalog', default='APOD')
    args = parser.parse_args()
    return args.catalog


def main():
    load_dotenv()
    create_directory(get_default_catalog())
    api_key_parameter = {'api_key': os.environ['NASA_API_KEY']}
    fetch_nasa_pictures_of_the_day(api_key_parameter)


if __name__ == '__main__':
    main()
