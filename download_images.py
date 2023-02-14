import requests
import os


def create_directory(directory):
    if not os.path.isdir(directory):
        os.makedirs(directory, exist_ok=False)


def download_images(url, file_path):

    response = requests.get(url)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        return file.write(response.content)
