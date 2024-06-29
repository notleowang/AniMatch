'''
Handles all incoming API requests and sends response data in json format
'''

import requests
import json


# =============================
# REQUEST HANDLING
# =============================

def handle_request(pageNum):
    print("Handling request")

    # API url
    url = 'https://graphql.anilist.co'

    # read query from GraphQL file
    with open('src/api/query.graphql', 'r') as file:
        query = file.read()

    # values for GraphQL variables
    variables = {
        'pageNum': pageNum,
        'mediaSort': 'ID',
        'perPage': 50, # max
        'statusVersion': 2,
        'asHtml': False,
        'sourceVersion': 3,
        'characterSort': 'ID',
        'staffSort': 'ID',
        'studioSort': 'ID',
    }

    response = requests.post(url, json={'query': query, 'variables': variables})
    return response


# =============================
# RESPONSE HANDLING
# =============================

def handle_response(response):
    print("Handling response")
    if response.status_code == requests.codes.ok:
        json_data = json.loads(response.text)
        return json_data
    else:
        handle_error(json.loads(response.text))


# =============================
# ERROR HANDLING
# =============================

def handle_error(response):
    if response['errors']:
        for error in response['errors']:
            status = error.get('status')
            message = error.get('message')
        print("Status: " + str(status) + " - " + message)
    else:
        print("Error object missing")
    