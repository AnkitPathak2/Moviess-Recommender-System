import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Please enter your favorite movie ',
    movies['title'].values)

# def homepage(movie_id):
#      response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=e4e6eee4e1624ced6028203dd107cd35&language=en-US')
#      url = response.json()
#      if url['homepage']=="":
#          return "#"
#      return url['homepage']

# def get_movie_id(title, movies):
#     movie_title_lower = title.lower()
#     match = movies[movies['title'].str.lower() == movie_title_lower]
#     if not match.empty:
#         return match.iloc[0]['movie_id']
#     else:
#         return None

# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=e4e6eee4e1624ced6028203dd107cd35&language=en-US'.format(movie_id))
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# def fetch_poster_url(movie):
    
#     url = "https://movies-api14.p.rapidapi.com/search"

#     querystring = {"query":movie}

#     headers = {
#         "X-RapidAPI-Key": "7a8e4c3a2emshb99de85af7ee894p1a1a46jsn462b95886bae",
#         "X-RapidAPI-Host": "movies-api14.p.rapidapi.com"
#     }

#     response = requests.get(url, headers=headers, params=querystring)

#     print(response.json())

#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def fetch_api(movie):
    
    url = "https://movies-api14.p.rapidapi.com/search"

    querystring = {"query":movie}

    headers = {
        "X-RapidAPI-Key": "7a8e4c3a2emshb99de85af7ee894p1a1a46jsn462b95886bae",
        "X-RapidAPI-Host": "movies-api14.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    res=response.json()
    
    posterURL = res["contents"][0]["poster_path"]
    link = res["contents"][0]["youtube_trailer"]
    return posterURL,link


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]

    movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    mdtxt = []
    

    
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        posterLink , link =fetch_api(movies.iloc[i[0]].title)
        #recommended_movies_posters.append(fetch_poster(movie_id))
        mdtxt.append(f'<a href="{link}" class="hover-img"><img src="{posterLink}" style="height:20vw; max-height:200px"></a>')
        
    return recommended_movies,recommended_movies_posters,mdtxt

if st.button('Recommend'):
    names,posters,mdtxt = recommend(selected_movie_name)
    
    #movie_id_header =  get_movie_id(selected_movie_name,movies)  
    
    posterLink , link =fetch_api(selected_movie_name)
    st.markdown(f'<a href="{link}" class="hover-img"><img src="{posterLink}" style="height:30vw; max-height:600px"></a>', unsafe_allow_html=True)
    st.text(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.markdown(mdtxt[0], unsafe_allow_html=True)
    with col2:
        st.text(names[1])
        st.markdown(mdtxt[1], unsafe_allow_html=True)
    with col3:
        st.text(names[2])
        st.markdown(mdtxt[2], unsafe_allow_html=True)
    with col4:
        st.text(names[3])
        st.markdown(mdtxt[3], unsafe_allow_html=True)
    with col5:
        st.text(names[4])
        st.markdown(mdtxt[4], unsafe_allow_html=True)

st.markdown("""
    <style>
        .hover-img {
            position: relative;
            width: 200px;
            height: 200px;
            overflow: hidden;
        }

        .hover-img img {
            transition: transform .3s ease;
        }

        .hover-img:hover img {
            transform: scale(1.1);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("D:\Downloads\ck.jpg") no-repeat center center fixed;
        -webkit-background-size: cover;
        -moz-background-size: cover;
        -o-background-size: cover;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)