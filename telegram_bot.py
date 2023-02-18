import telegram
import os
import random
import time
import argparse

from dotenv import load_dotenv

time_delay = 4 * 60 * 60


def take_files():
    catalog = "images"
    picture_title = create_parser()

    if picture_title:
        filepath = os.path.join(catalog, picture_title)
    else:
        filepath = os.path.join(catalog, random.choice(os.listdir(catalog)))
    return filepath


def send_files(bot, telegram_chat_id):
    while True:
        with open(take_files(), 'rb') as filepath:
            print(take_files())
            bot.send_photo(chat_id=telegram_chat_id, photo=filepath)
            time.sleep(time_delay)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('image', nargs='?')
    namespace = parser.parse_args()
    return namespace.image


def main():
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
    take_files()
    send_files(bot, telegram_chat_id)


if __name__ == '__main__':
    main()
