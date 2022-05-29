import streamlit as st
import pickle
import pandas as pd
import requests

# config site
st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    .reportview-container {
        background: black}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("<h1 style='text-align: center; color: white; font-size: 70px'>MovieQuick</h1>", unsafe_allow_html=True)

# required functions
def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(
            movie_id))
    # converted to viewable
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def fetch_link(movie_id):
    return "https://www.themoviedb.org/movie/" + str(movie_id)

def fetch_popular(movies):
    popular_movies_ordered =sorted(list(enumerate(movies['rating'])), reverse=True, key=lambda x: x[1])[1:21]

    popular_movies = []
    popular_movies_poster = []
    popular_movies_page = []
    a=0

    for i in popular_movies_ordered:
        if(a!=8):
            movie_id = movies.iloc[i[0]].id
            a+=1
            popular_movies.append(movies.iloc[i[0]].movie)
            # API poster
            popular_movies_poster.append(fetch_poster(movie_id))
            # link of page
            popular_movies_page.append(fetch_link(movie_id))
            # a+=1

    return popular_movies, popular_movies_poster, popular_movies_page

def recommend(movie):
    movie_index = movies[movies['movie'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity_matrix[movie_index])), reverse=True, key=lambda x: x[1])[1:31]

    recommended_movies = []
    recommended_movies_poster = []
    recommended_movies_page = []
    count = 0
    n=0

    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        if (movies.iloc[i[0]].rating) > 5 and count < 8:
            count += 1
            # print (movies.iloc[i[0]].movie)
            # print (movies.iloc[i[0]].rating)
            recommended_movies.append(movies.iloc[i[0]].movie)
            # API poster
            recommended_movies_poster.append(fetch_poster(movie_id))
            # link of page
            recommended_movies_page.append(fetch_link(movie_id))
            n +=1

        else:
            count+=1

    return recommended_movies, recommended_movies_poster, recommended_movies_page, n


movies_pickle = pickle.load(open('movie.pkl','rb'))
movies = pd.DataFrame(movies_pickle)

similarity_matrix = pickle.load(open('similarity_matrix.pkl','rb'))

selected_movie_name = st.selectbox(
     'Recommended Movies similar to:',
      movies['movie'].values)



if st.button('Go'):
       names,posters,page,num = recommend(selected_movie_name)

       # col1, col2, col3, col4, col5 = st.columns(5)
       col = st.columns(num)
       for x in range(0,num):
           with col[x]:
                st.text(names[x])
                st.image(posters[x])
                link = f'[Click]({page[x]})'
                # print (page[x])
                st.markdown(link,unsafe_allow_html=True)

       st.text('(Clicking on "Click" will direct you to the homepage of the movie)')



st.header('Popular Picks:')

pnames,pposters,ppage = fetch_popular(movies)

col = st.columns(7)
for x in range(0,7):
    with col[x]:
                st.text(pnames[x])
                st.image(pposters[x])
                plink = f'[Click]({ppage[x]})'
                # print (page[x])
                st.markdown(plink,unsafe_allow_html=True)