'''
1. Query all the fields we need from AniList DB
    - 30 requests per minute to be safe (warning on API docs https://docs.anilist.co/guide/rate-limiting)
    - Normally 90 requests per minute
2. Write all the json into a file
3. Build training data from json file?
    - Need to generate embeddings
4. Train model
'''

import time
import json

import requests

FILE_PATH = 'tests/anime_list.json'
API_URL = 'https://graphql.anilist.co'
REQUESTS_THRESHOLD_BUFFER = 10 # safety guard
REQUESTS_THRESHOLD = 60 + REQUESTS_THRESHOLD_BUFFER
MAX_ENTRIES_PER_PAGE = 50
SLEEP_BUFFER = 30 # safety guard
SLEEP_DURATION = 60 + SLEEP_BUFFER


def setup():
    print("\n--Running Setup")
    start_time = time.time()
    
    # build data
    anime_list = []
    page_num = 1
    for _ in range(5):
    # while True:
        query = '''
        query Page($page: Int, $perPage: Int) {
            Page(page: $page, perPage: $perPage) {
                media {
                    id
                    title {
                        english
                        romaji
                    }
                    genres
                    tags {
                        name
                    }
                    description
                }
                pageInfo {
                    hasNextPage
                }
            }
        }
        '''
        
        variables = {
            'page': page_num,
            'perPage': MAX_ENTRIES_PER_PAGE
        }
        
        json_body = {
            'query': query,
            'variables': variables,
        }
        
        # TODO: wrap request in try catch
        response = requests.post(API_URL, json=json_body)
        json_data = response.json()
        
        # CHECK FOR ERRORS
        if 'errors' in json_data:
            for error in json_data['errors']:
                message = error['message']
                status = error['status']
                print(f'ERROR DURING SETUP: {status} - {message}')
            break
        
        # CHECK IF WE HAVE MORE PAGES
        has_next_page = json_data['data']['Page']['pageInfo']
        if not has_next_page:
            break
        
        # CHECK RATE LIMITS
        rate_limit_remaining = response.headers['X-RateLimit-Remaining']
        print(f"X-RateLimit-Remaining: {rate_limit_remaining}")
        # chill for one minute if we've hit the rate limit
        if int(rate_limit_remaining) == REQUESTS_THRESHOLD:
            print("Sleeping")
            time.sleep(SLEEP_DURATION)
            
        # APPEND TO VECTOR
        for media in json_data['data']['Page']['media']:
            anime_list.append(media)
            
        page_num += 1
        
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(anime_list, f, ensure_ascii=False, indent=4)
        
    print(f'Added {len(anime_list)} anime in {time.time() - start_time} seconds')
    print("--Finished Setup")