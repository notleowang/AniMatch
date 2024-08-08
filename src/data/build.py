'''
File responsible for building the dataframe from the JSON file containing all the anime shows
'''

import os
import warnings
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning

from api.controller import *
import data.module as module


RELEVANT_FEATURES = [
    'id',
    'romaji',
    'english',
    'native',
    'description',
    'season',
    'genres'
]

def create_dataframe(anime_list):
    # create dataframe columns (column labels)
    column_labels = RELEVANT_FEATURES

    # create dataframe from anime_list
    df = pd.DataFrame(anime_list)

    # split title into three columns (romaji, english, native) respectively
    # - normalize_json() from pandas slower than below solution
    # - Fastest way to split dict into separate columns: https://stackoverflow.com/questions/38231591/split-explode-a-column-of-dictionaries-into-separate-columns-with-pandas/63311361#63311361
    df = df.join(pd.DataFrame(df.pop('title').values.tolist()))

    # reorder columns
    df = df[column_labels]

    # handle null and missing values
    # - replace with empty string for now
    # print(df.isnull().sum())
    df.fillna('', inplace=True)

    return df


def generate_csv(df, filepath):
    # ignoring bs4 warning about descriptions looking like filepaths.
    # - we know 100% that it isn't a filepath.
    warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

    # remove html tags from description
    df['description'] = df['description'].apply(clean_description)

    df.to_csv(filepath, sep='|', index=False)

    print("Generated csv at " + filepath)


def preprocess_data(filepath):

    df = pd.read_csv(filepath)

    # DESCRIPTION
    # download_nltk_packages()                  # uncomment if needed
    df['description'] = df['description'].apply(preprocess_data)

    generate_csv(df, 'tests/test.csv')


######################
# HELPER FUNCTIONS
######################

def clean_description(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text().strip()               # strip removes all the new lines


def preprocess_description(text):
    # Lowercase
    text = text.lower()
    # Tokenize
    words = word_tokenize(text)
    # Remove stopwords
    words = [word for word in words if word not in stopwords.words('english')]
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)


def download_nltk_packages():

    # path stuff
    nltk_data_dir = os.path.abspath('.venv/share/nltk_data')
    os.makedirs(nltk_data_dir, exist_ok=True)
    nltk.data.path.append(nltk_data_dir)

    # download packages
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
