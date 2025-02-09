#코드의 가독성 높이기 위한 resolver.py 파일 생성

import pandas as pd

item_fname = 'data/movies_final.csv'

def random_items():
    movies_df = pd.read_csv(item_fname)
    movies_df = movies_df.fillna('') #fill up the empty cells with empty string
    result_items = movies_df.sample(n=20).to_dict("records")
    return result_items