import streamlit as st
import pickle
import pandas as pd
import requests

def homepage(SeriesTitle):
    response = requests.get(f'https://api.tvmaze.com/search/shows?q={SeriesTitle}')
    data = response.json()
    if data and data[0].get('show', {}).get('officialSite'):
        return data[0]['show']['officialSite']
    else:
        return "#"

def fetch_poster_url(SeriesTitle):
    response = requests.get(f'https://api.tvmaze.com/search/shows?q={SeriesTitle}')
    data = response.json()
    if data is not None and isinstance(data, list) and len(data) > 0:
        if 'show' in data[0] and isinstance(data[0]['show'], dict) and 'image' in data[0]['show'] and data[0]['show']['image'] is not None and 'medium' in data[0]['show']['image']:
            return data[0]['show']['image']['original']
        else:
            return "https://static.tvmaze.com/uploads/images/medium_portrait/45/112879.jpg"
    else:
        return "https://static.tvmaze.com/uploads/images/medium_portrait/45/112879.jpg"

def recommend(web):
    series_index = webseries[webseries['SeriesTitle'] == web].index[0]
    distance = similarity[series_index]
    series_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_webseries = []
    recommended_webseries_poster = []
    mdtxt = []
    for i in series_list:
        SeriesTitle = webseries.iloc[i[0]].SeriesTitle
        recommended_webseries.append(webseries.iloc[i[0]].SeriesTitle)
        recommended_webseries_poster.append(fetch_poster_url(SeriesTitle))
        mdtxt.append(f'<a href="{homepage(SeriesTitle)}" class="hover-img"><img src="{fetch_poster_url(SeriesTitle)}" style="height:20vw; max-height:200px"></a>')
    return recommended_webseries,recommended_webseries_poster,mdtxt

webs_dict = pickle.load(open('web_dict.pkl','rb'))
webseries = pd.DataFrame(webs_dict)
similarity = pickle.load(open('similaritys.pkl','rb'))

st.title('Web Series Recommender System')

selected_webseries_name = st.selectbox(
    'Please enter your favorite Web Series',
    webseries['SeriesTitle'].values)

if st.button('Recommend'):
    names,poster,mdtxt = recommend(selected_webseries_name)
    
    st.markdown(f'<a href="{homepage(selected_webseries_name)}" class="hover-img"><img src="{fetch_poster_url(selected_webseries_name)}" style="height:30vw; max-height:600px"></a>', unsafe_allow_html=True)
    st.text(selected_webseries_name)
    
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
