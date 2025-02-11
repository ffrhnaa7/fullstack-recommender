import pandas as pd
import numpy as np
from scipy.sparse import coo_matrix
from implicit.als import AlternatingLeastSquares
import pickle

saved_model_fname = "model/finalized_model.sav"
data_fname = "data/ratings.csv"
item_fname = "data/movies_final.csv"
weight = 10

def model_train():
    ratings_df = pd.read_csv(data_fname)
    ratings_df["userId"] = ratings_df["userId"].astype("category")
    ratings_df["movieId"] = ratings_df["movieId"].astype("category")  

    # Sparse matrix of all users/movies
    rating_matrix = coo_matrix(
        (
            ratings_df["rating"].astype(np.float32),
            (
                ratings_df["movieId"].cat.codes.copy(),  
                ratings_df["userId"].cat.codes.copy(),
            ),
        )
    )

    # Train ALS model
    als_model = AlternatingLeastSquares(factors=50, regularization=0.01, dtype=np.float64, iterations=50)
    als_model.fit(weight * rating_matrix)

    # Save trained model
    pickle.dump(als_model, open(saved_model_fname, "wb"))
    return als_model

def calculate_item_based(item_id, items):
    #Load the saved model
    loaded_model = pickle.load(open(saved_model_fname, "rb"))
    recs = loaded_model.similar_items(item_id, N=11)
    return [str(items[r]) for r in recs[0]]

def items_based_recommendation(item_id):
    ratings_df = pd.read_csv(data_fname)
    ratings_df["userId"] = ratings_df["userId"].astype("category")
    ratings_df["movieId"] = ratings_df["movieId"].astype("category")
    movies_df = pd.read_csv(item_fname)

    items = dict(enumerate(ratings_df["movieId"].cat.categories))
    try:
        parsed_id = ratings_df["movieId"].cat.categories.get_loc(int(item_id))
        #parsed_id는 기존 item_idㅇ하는 다은 모델에서 사용하는 id이다
        result = calculate_item_based(parsed_id, items)
    except KeyError as e:
        result = []
    
    result = [int(x) for x in result if x != item_id]]
    result_items = movies_df[movies_df["movieId"].isin(result)].to_dict("records")
    return result_items
  

if __name__ == "__main__":
    model = model_train()
