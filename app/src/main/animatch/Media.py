class Media:
    def __init__(self, api_media):
        self.id: int

        '''
        If we ever need to store specific information from these classes in the future
        - i.e: For Anime: episodes, duration
        -      For Manga: volumes, chapters
        '''
        # self.anime: Anime = None
        # self.manga: Manga = None

        self.title_english: str = None
        self.title_romaji: str = None
        self.genres: list[str] = None
        self.tags: list[str] = None
        self.description: str = None

        self.is_adult: bool = False # api_media is HENTAI-SAFE for now...

        # ======= CONSTRUCT FIELDS =======
        self.id = api_media.get('id') # Should be non-null based off GraphQL Schema
        if api_media.get('title', None):
            self.title_english = api_media.get('title').get('english', "")
            self.title_romaji = api_media.get('title').get('romaji', "")
        self.genres = api_media.get('genres', [])
        self.tags = self._construct_tags(api_media.get('tags'))
        self.description = api_media.get('description', "")

    def _construct_tags(api_media_tags):
        if not api_media_tags:
            return []

        result = []
        for tag_name in api_media_tags:
            result.append(tag_name)

        return result