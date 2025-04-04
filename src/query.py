import requests

API_URL = 'https://graphql.anilist.co'

def get_viewer(access_token):
    query = '''
    query Viewer {
        Viewer {
            id
            name
        }
    }
    '''
    
    json = {
        'query': query,
        # 'variables': variables
    }
    
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    
    response = requests.post(API_URL, headers=headers, json=json)
    
    if response.status_code == 200:
        json_data = response.json()
        viewer = json_data['data']['Viewer']
        print(f"Welcome {viewer['name']} (id: {viewer['id']})")
    else:
        print("ERROR: Failed to fetch viewer info")