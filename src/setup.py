"""
This file is for preparing the data for AniList
"""

import requests
import json

def setup():
    url = 'https://graphql.anilist.co'

    query = '''
        query($sort: [MediaSort], $perPage: Int) {
            Page(perPage: $perPage) {
                media(sort: $sort) {
                    id
                    title {
                        english
                    }
                },
                pageInfo {
                    hasNextPage
                }
            }
        }
    '''
    variables = {
        'sort': 'ID',
        'perPage': 50 # max amount
    }

    response = requests.post(url, json={'query': query, 'variables': variables})
    json_data = json.loads(response.text)

    # print(json_data)

    print(json_data["data"]["Page"]["media"])