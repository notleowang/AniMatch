from Media import Media

class User:
    def __init__(self):
        self.id: int
        self.name: str = None
        self.favourite_anime: list[Media] = None