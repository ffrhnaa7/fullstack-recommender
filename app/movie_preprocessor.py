import pandas as pd
import requests
import sys
from tqdm import tqdm
import time

def add_url(row):
   return f"http://www.imdb.com/ttitle/tt{row}/"

def add_ratings(df):
    ratings_df = pd.read_csv('data/ratings.csv')
    ratings_df['movieId'] = ratings_df['movieId'].astype(str)
    agg_df = ratings_df.groupby('movieId').agg(rating_count=('rating','count'), rating_avg=('rating','mean')).reset_index()

    rating_added_df = df.merge(agg_df,on='movieId')
    return rating_added_df

def add_poster(df):
   for i, row in tqdm(df.iterrows(), total=df.shape[0]):
      tmdb_id = row["tmdbId"]
      tmdb_url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key=47e154f7898f30aa991e76b5eb992ba7&language=en-US"
      result = requests.get(tmdb_url)

      try:
         df.at[i, "poster_path"] ="https://image.tmdb.org/t/p/original" + result.json()["poster_path"]
         time.sleep(0.1)

      except (TypeError,KeyError) as e:
         df.at[i, "poster_path"] = "http://image.tmdb.org/t/p/original/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg"
   return df                  

if __name__ == "__main__":
   movies_df = pd.read_csv('data/movies.csv')
   #to ensure ID can be detected as text, we will change the type of ID to string
   movies_df['movieId'] = movies_df['movieId'].astype(str)
   links_df = pd.read_csv('data/links.csv', dtype=str )
   merged_df = movies_df.merge(links_df, on='movieId', how='left')
   merged_df['url']=merged_df['imdbId'].apply(lambda x: add_url(x))
   result_df = add_ratings(merged_df)
   result_df['poster_path'] = None
   result_df = add_poster(result_df)
   result_df.to_csv('data/movies_final.csv', index=None)