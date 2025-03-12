import pandas as pd
from surprise import Dataset, Reader, SVD
import pickle

# Load data
reader = Reader(rating_scale=(0, 5))
ratings = pd.read_csv("ml-latest-small/ratings.csv")
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

# Train the model
trainset = data.build_full_trainset()
model = SVD()
model.fit(trainset)

# Save the model
with open("recommendation_model.pkl", "wb") as f:
    pickle.dump(model, f)