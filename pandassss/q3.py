import pandas as pd

data = {
    "Movie Name": ["A","B","C","D","E","F","G","H","I","J"],
    "Language": ["Hindi","English","Hindi","Tamil","Hindi","English","Hindi","Telugu","Hindi","English"],
    "Genre": ["Action","Drama","Comedy","Action","Romance","Drama","Thriller","Action","Comedy","Romance"],
    "Rating": [7.5,8.2,6.9,7.8,8.5,7.1,8.0,6.5,9.0,7.3],
    "Review": ["Good","Good","Good","Good","Good","Good","Good","Good","Good","Good"]
}

df = pd.DataFrame(data)

df.to_csv("Movies.csv", index=False)

movies = pd.read_csv("Movies.csv")

highest_movie = movies.loc[movies["Rating"].idxmax()]
print(highest_movie)

hindi_movies = movies[movies["Language"] == "Hindi"]
hindi_movies.to_csv("HindiMovies.csv", index=False)
