import pandas as pd
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect("dbname=movies_db user=myuser password=mypassword host=localhost")
cur = conn.cursor()

# Load Movies
movies = pd.read_csv("ml-latest-small/movies.csv")
for _, row in movies.iterrows():
    cur.execute("INSERT INTO movies (movieId, title, genres) VALUES (%s, %s, %s)", 
                (row.movieId, row.title, row.genres))

# Load Ratings
ratings = pd.read_csv("ml-latest-small/ratings.csv")
ratings["rating"] = ratings["rating"].astype(float)  # Convert rating to float
for _, row in ratings.iterrows():
    cur.execute("INSERT INTO ratings (user_id, movieId, rating) VALUES (%s, %s, %s)", 
                (int(row.userId), int(row.movieId), float(row.rating)))

# Commit changes and close connection
conn.commit()
conn.close()
