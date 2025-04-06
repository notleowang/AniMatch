'''
Custom Dataset class
https://pytorch.org/tutorials/beginner/basics/data_tutorial.html#creating-a-custom-dataset-for-your-files
'''

import json

import torch
from torch.utils.data import Dataset
from sentence_transformers import SentenceTransformer

from app.src.main.animatch.anilist.api.queries import *


class AniListDataset(Dataset):
    def __init__(self, json_path, st_model_name):
        super().__init__()
        
        self.json_path = json_path
        self.json_data = []
        
        self.unique_genres = []
        self.num_unique_genres = 0
        self.genre_to_idx = {}
        
        self.unique_tags = []
        self.num_unique_tags = 0
        self.tag_to_idx = {}
        
        self.st_model = None
        self.embeddings_dim = 0
        
        try:
            with open(self.json_path, 'r', encoding='utf-8') as f:
                self.json_data = json.load(f)
            print(f"Successfully loaded {len(self.json_data)} entries from {self.json_path}")
            
            # GENRES
            self.unique_genres = get_genre_collection()
            self.num_unique_genres = len(self.unique_genres)
            self.genre_to_idx = {genre: idx for idx, genre in enumerate(self.unique_genres)}
            print(f"{self.num_unique_genres} unique genres")
            # print(f"Genres: {self.unique_genres}")
            
            # TAGS
            self.unique_tags = get_media_tag_collection()
            self.num_unique_tags = len(self.unique_tags)
            self.tag_to_idx = {tag: idx for idx, tag in enumerate(self.unique_tags)}
            print(f"{self.num_unique_tags} unique tags")
            # print(f"Tags: {self.unique_tags}")
            
            # SENTENCE TRANSFORMER MODEL
            self.st_model = SentenceTransformer(st_model_name)
            self.embeddings_dim = self.st_model.get_sentence_embedding_dimension()
        except Exception as e:
            print("An error occurred during AniListDataset initialization")
            print(e)
    
    def __len__(self):
        return len(self.json_data)
    
    def __getitem__(self, idx):
        anime_entry = self.json_data[idx]
        
        # EXTRACT RAW DATA
        anime_id = anime_entry['id']
        title_english = anime_entry['title']['english']
        title_romaji = anime_entry['title']['romaji']
        genres = anime_entry['genres']
        tags = [tag['name'] for tag in anime_entry['tags']]
        description = anime_entry['description']
        
        # PROCESS GENRES
        # - Use Multi-Hot Encoding since there's multiple genres for an anime show
        # - Multiple categorical features
        genre_vector = torch.zeros(self.num_unique_genres, dtype=torch.float32)
        for g in genres:
            g_idx = self.genre_to_idx[g]
            genre_vector[g_idx] = 1.0
            
        # PROCESS TAGS
        tag_vector = torch.zeros(self.num_unique_tags, dtype=torch.float32)
        for t in tags:
            t_idx = self.tag_to_idx[t]
            tag_vector[t_idx] = 1.0
            
        # PROCESS DESCRIPTION
        embeddings = self.st_model.encode(description, convert_to_tensor=True)
        description_embedding = embeddings.to(dtype=torch.float32)
        
        result = {
            # 'id': anime_id,
            # 'title_english': title_english,
            # 'title_romaji': title_romaji,
            # 'genres': genres,
            # 'tags': tags,
            'genre_vector': genre_vector,                       # tensor
            'tag_vector': tag_vector,                           # tensor
            'description_embedding': description_embedding      # tensor
        }
        
        return result