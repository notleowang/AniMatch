import sys

from data.build import *
from data.anilist import *
from data.module import deserialize

def run():
    anime_list_csv_path = 'tests/anime_list.json'

    # 1. get data from Anilist API
    # fetch_data()

    # 2. load data into a json file
    with open(anime_list_csv_path, 'r', encoding='utf-8') as f:
        anime_list = json.load(f)

    # 3. create pandas dataframe from json file and generate a csv
    df = create_dataframe(anime_list)
    # df = df.head(50000)                           # SLICE DATAFRAME FOR TESTING IN JUPYTER
    # generate_csv(df, anime_list_csv_path)

    # 4. begin preprocessing data
    preprocess_data(anime_list_csv_path)

if __name__ == '__main__':
    # set stdout pipe to allow utf-8 characters (required for japanese letters)
    sys.stdout.reconfigure(encoding='utf-8')
    run()