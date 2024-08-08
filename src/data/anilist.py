'''
AniList data handler; Fetches all the data from the API and builds the Anime List JSON file.
'''

import time

from api.controller import *
import data.module as module


REQUESTS_PER_PAGE = 50

# recursively traverse through all the pages and create a list of Anime objects
# TODO: NEED SOLUTION FOR MAX 90 REQUESTS PER MINUTE
#       CURRENT SOLUTION: Sleep for 90 seconds after every 25 requests.
def fetch_data():
    print("Creating Anime Show List")
    anime_list = []

    pageNum = 1

    while True:
        # Temporary force stop to handle rate limiting
        if pageNum % 25 == 0:
            # print("======SLEEPING FOR 90 SECONDS======")
            time.sleep(90)
        
        response = handle_request(pageNum, REQUESTS_PER_PAGE)
        json_data = handle_response(response)
        curr_page = module.Page(json_data['data']['Page'])

        for media in curr_page.media:
            curr_anime = module.Anime(media)
            anime_list.append(curr_anime)

        if not curr_page.hasNextPage:
            break
        
        pageNum += 1

    # Write to 'test/anime_list.json'
    with open('tests/anime_list.json', 'w', encoding='utf-8') as f:
        json.dump(anime_list, f, ensure_ascii=False, indent=4)

    print("Finished Anime Show List")