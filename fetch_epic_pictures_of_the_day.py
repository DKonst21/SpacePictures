import requests
import os
import datetime

from datetime import datetime
from download_images import download_images, create_directory
from dotenv import load_dotenv


def fetch_epic_pictures_of_the_day(api_key_foto):
    nasa_url = "https://api.nasa.gov/EPIC/api/natural/images"
    epic_pictures = get_url(nasa_url, api_key_foto).json()

    for index_number, index in enumerate(epic_pictures):
        massiv_image = index['image']
        massiv_date = datetime.fromisoformat(index['date'])
        year = massiv_date.strftime("%Y")
        month = massiv_date.strftime("%m")
        day = massiv_date.strftime("%d")
        url_actual_foto = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{massiv_image}.png"
        response_url_actual_foto = requests.get(url_actual_foto, params=api_key_foto)
        response_url_actual_foto.raise_for_status()
        name_epic_picture_template = os.path.join("epic", "{name}.png".format(name=massiv_image))
        download_images(response_url_actual_foto.url, name_epic_picture_template)


def get_url(url, api_key_foto):
    response = requests.get(url, params=api_key_foto)
    response.raise_for_status()
    return response


def main():
    load_dotenv()
    create_directory("epic")
    api_key_foto = {'api_key': os.environ['NASA_API_KEY']}
    fetch_epic_pictures_of_the_day(api_key_foto)


if __name__ == '__main__':
    main()
