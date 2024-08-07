'''
Class objects for the JSON data response from AniList API
'''

class Page:
    def __init__(self, page_json):
        self.media = page_json['media']                             # all the media on this page (in json)
        self.hasNextPage = page_json['pageInfo']['hasNextPage']     # boolean value for if another page exists after

class Anime:
    def __init__(self, media_json):
        self.id = media_json['id']              # AniList ID
        self.idMal = media_json['idMal']        # MyAnimeList ID (might need later)
        self.title = media_json['title']        # Romanji, English, and Native versions of title stored in dict
        self.format = media_json['format']
        self.status = media_json['status']
        self.description = media_json['description']
        self.season = media_json['season']
        self.genres = media_json['genres']

    def to_json(self):
        return {
            'id': self.id,
            'idMal': self.idMal,
            'title': self.title,
            'format': self.format,
            'status': self.status,
            'description': self.description,
            'season': self.season,
            'genres': self.genres
        }


# HELPER FUNCTIONS
def deserialize(json_list):
    anime_list = []
    for json_str in json_list:
        anime_list.append(Anime(json_str))

    return anime_list