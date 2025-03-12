import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load dataset
ratings = pd.read_csv("ml-latest-small/ratings.csv")
movies = pd.read_csv("ml-latest-small/movies.csv")

# Merge datasets to get movie names
ratings = ratings.merge(movies, on="movieId")

# Function to get top recommended movies for a user
def get_top_movies(user_id, num_recommendations=5):
    user_ratings = ratings[ratings["userId"] == int(user_id)]
    top_movies = user_ratings.sort_values(by="rating", ascending=False).head(num_recommendations)
    return top_movies["title"].tolist()

@app.route("/")
def home():
    return "Welcome to the Movie Recommendation System!"

@app.route("/recommend/<user_id>", methods=["GET"])
def recommend(user_id):
    recommended_movies = get_top_movies(user_id)
    return jsonify({"movies": recommended_movies})

if __name__ == "__main__":
    app.run(debug=True)
