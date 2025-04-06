import webbrowser

from urllib.parse import urlparse, parse_qs

from animatch.anilist.api.keys import ANILIST_CLIENT_ID

AUTH_URL = 'https://anilist.co/api/v2/oauth/authorize'

def login_anilist():
    auth_link = f'{AUTH_URL}?client_id={ANILIST_CLIENT_ID}&response_type=token'
    webbrowser.open(auth_link)

    redirected_url = input("Enter the redirected url after AniList approval: ")
    parsed_url = urlparse(redirected_url)
    fragment_query_string = parsed_url.fragment
    fragment_dict = parse_qs(fragment_query_string)

    access_token = fragment_dict['access_token'][0]

    if access_token:
        print("\nUser Authenticated!\n")
        return access_token

    return None