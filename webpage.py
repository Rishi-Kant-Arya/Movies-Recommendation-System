import pickle
import pandas as pd
import streamlit as st

st.title('Movies Recommendation System')

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]

    recommended_movies=[]

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

similarity = pickle.load(open('similarity.pkl','rb'))
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Search for a movie",
    movie_list
)



if st.button('Show Recommendations'):
    recommended_movie_names = recommend(selected_movie)
    for i in recommended_movie_names:
        st.write(i)
