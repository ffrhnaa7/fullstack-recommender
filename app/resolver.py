#코드의 가독성 높이기 위한 resolver.py 파일 생성

import pandas as pd

# Define the path to the CSV file
item_fname = 'data/movies_final.csv'

# Function to get random items from the dataset
def random_items():
    # Read the CSV file and fill missing values
    movies_df = pd.read_csv(item_fname)
    movies_df = movies_df.fillna('')  # Fill empty cells with empty string
    # Get a random sample of 20 items from the dataframe and convert to a list of dictionaries
    result_items = movies_df.sample(n=10).to_dict("records")
    return result_items

def random_genres_items(genre):
    movies_df = pd.read_csv(item_fname)
    genre_df = movies_df[movies_df['genres'].apply(lambda x:genre in x.lower())]
    genre_df = genre_df.fillna('')
     
    # Get a random sample of 20 items from the filtered genre dataframe and convert to a list of dictionaries
    result_items = genre_df.sample(n=20).to_dict("records")
    return result_items