import sys

import torch
from torch.utils.data import DataLoader

from setup import setup
from model.classes import AniListDataset
from anilist.login import login_anilist
from anilist.queries import get_viewer

access_token = None


def main():
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == '-setup':
        setup()
    if len(args) == 2 and args[0] == '-dataset':
        dataset = AniListDataset(
            json_path='tests/anime_list.json',
            st_model_name='all-MiniLM-L6-v2'
        )

        sample_data = dataset[0]

        # print(sample_data['genres'])
        # print(sample_data['genre_vector'])

        # print(sorted(sample_data['tags']))
        # print(sample_data['tag_vector'])
        # active_indices = torch.where(sample_data['tag_vector'] == 1.0)[0].tolist()
        # print([dataset.unique_tags[i] for i in active_indices])

        # print(sample_data['description_embedding'])
        # print(sample_data['description_embedding'].shape)

        train_dataloader = DataLoader(dataset, batch_size=4, shuffle=True)

        for batch in train_dataloader:
            # print(batch)
            print(f"Type of batch object: {type(batch)}")
            print(f"Keys in the batch dictionary: {batch.keys()}")
            print(f"Genre vector batch shape: {batch['genre_vector'].shape}")
            print(f"Tag vector batch shape: {batch['tag_vector'].shape}")
            print(f"Description embedding batch shape: {batch['description_embedding'].shape}")

            # print(f"IDs in batch (example): {batch['id'][0]}") # Print first ID
            # print(f"Type of 'id' batch: {type(batch['id'])}") # Likely tuple
            # print(f"Length of 'id' batch: {len(batch['id'])}") # Should match batch size

        return 0

    global access_token
    
    while True:
        print('\nAniMatch')
        print('-----------------------')
        print('1 - Start now')
        if not access_token:
            print('2 - Login with AniList')
            print('3 - Login with MAL')
        else:
            print('4 - Recommend based off Favourites')
            print('5 - Recommend based off Trending')
            print('6 - Recommend based off Genre')
        print('q - Quit Application')
        print('-----------------------\n')
        
        x = input("Input: ")
        
        match x:
            case '1':
                continue
            case '2':
                access_token = login_anilist()
                if access_token:
                    get_viewer(access_token)
            case '3':
                # MAL discontinuing?
                continue
            case '4':
                continue
            case '5':
                continue
            case '6':
                continue
            case 'q':
                return 0
            case _:
                print("Invalid input")


if __name__ == "__main__":
    # set stdout pipe to allow utf-8 characters (required for japanese letters)
    sys.stdout.reconfigure(encoding='utf-8')
    main()
    
    