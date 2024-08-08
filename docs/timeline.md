# Timeline

My personal log entries and general timeline of project.

## DAY 6 - 08/07/2024
- Got the `anime_list.json` completed.
- Starting the preprocessing steps.
  - Need to tokenize anime show descriptions if i'm using it for content-based filtering.
    - Will use natural language toolkit (nltk)

## DAY 5 - 08/06/2024
- Back from vacation lol
- Rejogging memory:
  - Goal: Create an "anime list" json file that is created from my own classes in `module.py`
  - Problem: Rate Limited to 90 requests per minute.
    - Solution: Wait 1 minute before calling recursive function again.
  - While iterating through the responses from graphql query,
    - Create class objects
    - Append class objects to a list data structure
  - Through another function, turn the resulting list to json
  
  - For the rate limiting problem:
    - The current solution is to go for a sleep time of 90 seconds every 25 requests, then continue the recursion.
    - The API says 50 requests every 60 seconds, but doing so resulted in a rate limiting response code anyways.
    - Because of this implementation, we will only call this recursive function when there needs to be a massive update to the existing database.

  - For fetch_data implementation, I made a recursive solution that hit max recrusive depth LMFAO???
    - Changed to iterative implementation using while loop.

## DAY 4 - 06/29/2024
- Need to create an **Anime Feature Matrix**.
  - Columns are features of the anime (genre, characters, etc).
  - Rows are based off the anime ID.
  - Step 1: Extract relevant features (i think I do this manually?).
  - Step 2: Preprocess the data so that it can be used for the Neural Network model.
  - Step 3: Create neural network.

|  | description | characters | genre | tags |
| --- | --- | --- | --- | --- |
| 0 | ... | ... | ... | ... |
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |

- Need a solution for the 90 requests per minute.
  - I only need to do these requests to make the dataset, once I have all the data I don't need to request again.
- Okay so for the dataset, I think I use the ID for each row label.
  - My thinking is that I don't wanna use the title because there's 3 versions (romaji, english, and native) and will be more difficult to work with later on.
  - Instead use ID and then just map it to my objects later to get other necessary info for the anime.
- For the **Anime Feature Matrix**:
  - I will first create a base Pandas dataframe.
    - This df differs from the final df in that it's not processed yet for input into model.
  - Then I will process columns like genre and tags into a one-hot-encoder.

## DAY 3 - 06/28/2024
- Found a good source for structuring my project: https://docs.python-guide.org/writing/structure/

## DAY 2 - 06/25/2024
- Again to reiterate that **content-based filtering** is probably better:
  - I have no users and so collaborative filtering (which gives recommendations based on similar users) is impossible.
- Got extremely tired so I took a nap

## DAY 1 - 06/24/2024

- Anime recommendation website
  - AniList integration later?
- Probably use a **Content-based Filtering** algorithm
  - Content-based Filtering: Recommend similar items using the features of an item based on the user’s preferences.
    - Recommend similar anime based of its similarity with other anime
      - Compare synopsis, genre, etc
    - It’s more personalized to the specific user (doesn’t use the input from other users)
    - Scale of project not expecting a lot of users to use so collaborative filtering would be a bit difficult since the data is sparse.
  - Collaborative Filtering: Recommend items based on their similarity with other similar users’ preferences.
  - **Possible solution to “Cold Start” Problem**
    - Have a page recommending trending and popular current titles.
    - Good place for new user to start off
    - Most Popular Titles
    - Most Watched Titles
    - Trending Titles (based on current season or current year)
  - Anime Release Logistics
    - Usually anime releases are split into seasons
    - Fall, Spring, Summer, Winter
    - Year
  - Neural Network
    - Ensemble Method (Netflix Contest 2009)
    - Increasing the diversity of the models was better than improving the models
    - Build model with PyTorch API
  - Data
    - AniList DB
    - Uses GraphQL to query API
    - MyAnimeList DB
  - Sources:
    - https://www.nvidia.com/en-us/glossary/recommendation-system/
      - Has good pictures to visualize filtering algorithms
  - Struggled with learning everything and started looking into my past course notes

## INTRO

Record after finishing project

## TOOLS

- AniList API
  - https://anilist.gitbook.io/anilist-apiv2-docs