'''
File responsible for building the dataframe from the JSON file containing all the anime shows
'''

import pandas as pd
import numpy as np

from api.controller import *
import data.module as module


RELEVANT_FEATURES = [
    'description',
    'season',
    'genres'
]

def create_dataframe(anime_list):
    # create dataframe columns (column labels)
    column_labels = RELEVANT_FEATURES