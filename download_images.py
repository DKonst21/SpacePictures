import requests
import os


def create_directory(directory):
    os.makedirs(directory, exist_ok=True)


def download_images(url, file_path, payload=''):

    response = requests.get(url, params=payload)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        return file.write(response.content)
