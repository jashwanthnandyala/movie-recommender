import streamlit as st
import pickle
import numpy as np

movies=pickle.load(open('movies.pkl', 'rb'))
movies_list=movies['title'].values
st.title('Movie Recommender')
selected_movie = st.selectbox(
    'select a movie',
    movies_list,
)

similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
    movie_index=movies[movies['title'] == movie].index[0]
    distances=similarity[movie_index]

    Mlist = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in Mlist:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


if st.button('Recommend'):
    result=recommend(selected_movie)
    for i in result:
        st.write(i)
