# Timeline

Daily log entries and general timeline of project.

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