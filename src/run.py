import sys

from data.build import *
from data.anilist import *
from data.module import deserialize


def run():
    fetch_data()

    with open('tests/anime_list.json', 'r', encoding='utf-8') as f:
        anime_json_list = json.load(f)

    create_dataframe(deserialize(anime_json_list))
    # extract_features()
    # preprocess_data()

if __name__ == '__main__':
    # set stdout pipe to allow utf-8 characters (required for japanese letters)
    sys.stdout.reconfigure(encoding='utf-8')
    run()