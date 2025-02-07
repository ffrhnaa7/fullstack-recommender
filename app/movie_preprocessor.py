import pandas as pd
import requests 

def add_url(row):
   return f"http://www.imdb.com/ttitle/tt{row}/"

if __name__ == "__main__":
   movies_df = pd.read_csv('data/movies.csv')
   print(movies_df)
   #to ensure ID can be detected as text, we will change the type of ID to string
   movies_df['movieId'] = movies_df['movieId'].astype(str)
   links_df = pd.read_csv('data/links.csv', dtype=str )
   merged_df = movies_df.merge(links_df, on='movieId', how='left')
   merged_df['url']=merged_df['imdbId'].apply(lambda x: add_url(x))
   print(merged_df)
   print(merged_df.columns)