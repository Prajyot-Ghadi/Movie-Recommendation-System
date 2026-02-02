import pickle
import streamlit as st
import pandas as pd


# ------------------ RECOMMEND FUNCTION ------------------
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]

    distances = list(enumerate(similarity[movie_index]))
    distances = sorted(distances, reverse=True, key=lambda x: x[1])

    recommended_movie_names = []

    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names


# ------------------ STREAMLIT UI ------------------
st.title("Movie Recommender System")

# load data
movies = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies)

similarity = pickle.load(open("similarity.pkl", "rb"))

# dropdown
movie_list = movies["title"].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

# button
if st.button("Show Recommendation"):
    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.write("👉", movie)
