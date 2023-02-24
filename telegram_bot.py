import telegram
import os
import random
import argparse

from dotenv import load_dotenv
from time import sleep
from telegram.error import NetworkError


def take_files(namespace):
    catalog = namespace.catalog
    picture_title = namespace.image

    if picture_title:
        filepath = os.path.join(catalog, picture_title)
    else:
        filepath = os.path.join(catalog, random.choice(os.listdir(catalog)))
    return filepath


def send_files(bot, telegram_chat_id, namespace):
    while True:
        sleep(1)
        try:
            with open(take_files(namespace), 'rb') as filepath:
                bot.send_photo(chat_id=telegram_chat_id, photo=filepath)
                sending_delay = namespace.delay
                sleep(sending_delay)
        except NetworkError:
            sleep(15)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('image', nargs='?')
    parser.add_argument('--catalog', default='images')
    parser.add_argument('--delay', type=int, default=4*60*60)
    return parser


def main():
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
    namespace = create_parser().parse_args()
    take_files(namespace)
    send_files(bot, telegram_chat_id, namespace)


if __name__ == '__main__':
    main()
