import streamlit as st
import pickle
import pandas as pd
import requests
st. set_page_config(layout="wide")

st.title("Movie Recommender System")


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=38cd4035dde2b5c6fcb6f0b793b1b48b&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    L = []
    posters = []
    index = movies[movies['title'] == movie].index[0]
    movie_distance = similarity[movies[movies['title'] == movie].index[0]]
    movie_list = sorted(list(enumerate(movie_distance)), reverse=True, key=lambda x: x[1])[1:6]
    list_overview = original_movies_dataset[original_movies_dataset['title'] == movie]['overview'][index]
    overview = " ".join(list_overview)
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        posters.append(fetch_poster(movie_id))
        L.append(movies.iloc[i[0]].title)
    return L, overview, posters


movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
original_movies_dict = pickle.load(open('original_movies_dict.pkl', 'rb'))
original_movies_dataset = pd.DataFrame(original_movies_dict)

selection = st.selectbox('Select movie for recommendation', movies['title'].values)

if st.button('Recommend'):
    movies_name, overview, posters = recommend(selection)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.subheader(movies_name[0])
        st.image(posters[0])

    with col2:
        st.subheader(movies_name[1])
        st.image(posters[1])

    with col3:
        st.subheader(movies_name[2])
        st.image(posters[2])

    with col4:
        st.subheader(movies_name[3])
        st.image(posters[3])

    with col5:
        st.subheader(movies_name[4])
        st.image(posters[4])
