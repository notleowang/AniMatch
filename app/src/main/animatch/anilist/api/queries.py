'''
Helper functions to query AniList
TODO: clean up the duplicate code in this file.
- should just make one function called handle_request and handle_response.
    - handle_response should return the json_data itself instead of the actual value.
'''

import requests

API_URL = 'https://graphql.anilist.co'

# Query for Viewer
def get_viewer(access_token):
    query = '''
    query Viewer {
        Viewer {
            id
            name
        }
    }
    '''

    json_body = {
        'query': query,
        # 'variables': variables
    }

    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    response = requests.post(API_URL, headers=headers, json=json_body)

    if response.status_code == 200:
        json_data = response.json()
        viewer = json_data['data']['Viewer']
        print(f"Welcome {viewer['name']} (id: {viewer['id']})")
    else:
        print("ERROR: Failed to fetch viewer info")

# Query for GenreCollection
def get_genre_collection():
    query = '''
    query Query {
        GenreCollection
    }
    '''

    json_body = {
        'query': query,
    }

    response = requests.post(API_URL, json=json_body)

    if response.status_code == 200:
        json_data = response.json()
        genre_collection = json_data['data']['GenreCollection']
        return genre_collection
    else:
        print("ERROR: Failed to fetch Genre Collection")
        return []

# Query for MediaTagCollection
def get_media_tag_collection():
    query = '''
    query Query {
        MediaTagCollection {
            name
        }
    }
    '''

    json_body = {
        'query': query,
    }

    response = requests.post(API_URL, json=json_body)

    if response.status_code == 200:
        json_data = response.json()
        media_tag_collection = json_data['data']['MediaTagCollection']
        return [tag['name'] for tag in media_tag_collection]
    else:
        print("ERROR: Failed to fetch Media Tag Collection")
        return []