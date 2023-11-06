import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from streamlit_lottie import st_lottie
import requests
import re 
import plotly.graph_objects as go
import plotly.figure_factory as ff
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import folium
import streamlit.components.v1 as components
import webbrowser
from urllib.request import urlopen
import json


import plotly.express as px


image1 = Image.open('ucr.png')
image2 = Image.open('images (1).jpeg')
image3 = Image.open('Logo-Ulacit.jpg')
url1 = "https://github.com/barquerosanchezdiegoarmando" 
url2 = "https://www.linkedin.com/in/diego-armando-barquero-s%C3%A1nchez-/"
url3 = "https://twitter.com/absanchez"

def load_lottierurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


gdf = gpd.read_file('Distritos_de_Costa_Rica.geojson')
heredia_gdf = gdf[gdf["NOM_PROV"] == "HEREDIA"]
Bandera = load_lottierurl("https://lottie.host/0461a0c2-7332-4807-b7d9-bde8403a3721/p9IajdxLwr.json")
Uruguay = load_lottierurl("https://lottie.host/caaf5e8f-0c37-40fb-91b5-b961e235e5db/owo1MCXMY1.json")
df = pd.DataFrame(
    {"lat": [9.9502, 
            9.9413,
            9.9988,
            -34.9055],
     "lon": [-84.0407,
             -84.0778,
             -84.1115,
             -56.1851],
     "text": ["UCR", "ULACIT", "UNA", "Sede Uruguay"],
     "Provincia": ["aliceblue", "antiquewhite", "aqua", "aquamarine"]}
    )

import plotly.graph_objects as go

heredia_center = [heredia_gdf.geometry.centroid.y.mean(), heredia_gdf.geometry.centroid.x.mean()]


m = folium.Map(location=[9.63, -84.25], zoom_start=8)
# Add the GeoDataFrame to the map
folium.GeoJson(gdf).add_to(m)
points = [
    {"location": [9.9040, -83.9850], "name": "La unión"},
    {"location": [9.9281, -84.0907], "name": "San José"},
    {"location": [10.5252, -85.2541], "name": "Bagaces"},
    {"location": [10.4274, -85.0935], "name": "Cañas"},
    {"location": [9.95582, -84.0854], "name": "Tibás"},
    {"location": [10.0145, -84.0986], "name": "San Rafael"},
    {"location": [9.9146, -84.0387], "name": "Curridabat"},
    {"location": [9.8392, -83.8664], "name": "Paraíso"},
    {"location": [9.8642, -84.0934], "name": "Aserrí"},
    {"location": [9.3660, -83.6961], "name": "San Isidro"},
    {"location": [9.7055, -84.0696], "name": "León Córtes"},
    {"location": [9.9408, -84.0247], "name": "Montes de Oca"},
    {"location": [11.0337, -84.7133], "name": "Los chiles"},
    {"location": [10.0481, -83.9533], "name": "Vásquez de Coronado"},
    {"location": [9.9981, -84.1198], "name": "Heredia"}
]

for point in points:
    folium.Marker(
        location=point["location"],
        popup=point["name"]
    ).add_to(m)
    

m1 = folium.Map(location=[9.63, -84.25], zoom_start=8)
# Add the GeoDataFrame to the map
folium.GeoJson(gdf).add_to(m1)
points1 = [
    {"location": [9.9040, -83.9850], "name": "La unión"},
    {"location": [9.9281, -84.0907], "name": "San José"},
    {"location": [10.5252, -85.2541], "name": "Bagaces"},
    {"location": [10.4274, -85.0935], "name": "Cañas"},
    {"location": [9.95582, -84.0854], "name": "Tibás"}
]

for point in points1:
    folium.Marker(
        location=point["location"],
        popup=point["name"]
    ).add_to(m1)

st.set_page_config(page_title='Datathon Uruguay - Data Solution Aproach',
                    page_icon="chart_with_upwards_trend",
                    layout = "wide")

class SessionState:
    def __init__(self):
        self.page = "Home"  # Default page

# Create an instance of the session state
state = SessionState()

# Define the functions for each page
def home_page():
    with st.container():
        izquierda1,centro1, derecha1 = st.columns((2,1,1))
        with izquierda1:
            st.title("UN- Datathon Montevideo Uruguay")
            st.subheader("DATA-DRIVEN SOLUTIONS FOR SUSTAINABLE HOUSING IN COSTA RICA")
            st.write("Structured data analysis")
            st.write("Deep learning models for image transformation")
            st.write("Unsupervised analysis to understand geospacial images")
        with derecha1: 
            centro3, derecha3 = st.columns((1,1))
            with centro3:
                st_lottie(Bandera, height = 150, key = "CR")
            with derecha3:
                st_lottie(Uruguay, height = 150, key = "UR")
        with centro1:
            st.subheader("Members")
            st.markdown("""
                     - [Alexander Valverde-ULACIT-](https://www.linkedin.com/in/alexandervalverdeguillen/)
                     - [Diego Barquero-UNA-](https://www.linkedin.com/in/diego-armando-barquero-s%C3%A1nchez-/)
                     - [Luis Solano-UCR-](https://www.linkedin.com/in/luis-fernando-solano-80746a272/)
                     
            """
            )
    st.write("___")
    st.header("PROBLEM STATEMENT")
    st.write("""Costa Rica faces pressing housing issues marked by rapid urbanization, affordability concerns, and environmental considerations. This presentation seeks to leverage data-driven insights to propose sustainable housing solutions.
""")
    st.header("DATA SOURCE")
    st.write("""Our analysis is grounded in a comprehensive dataset covering the Costa Rican housing market over the past decade. This dataset was obtained from INEC ( costarican institute of statistics and census) and encompasses critical housing market attributes.
""")
    st.write("___")
    st.map(df)
    st.write("___")

def page1():
    st.title("Exploratory Data Analysis")
    st.write("___")
    st.title("Time Series")
    with st.container():
        izquierda1,centro1, derecha1 = st.columns((1,1,1))
        with izquierda1:
            st.subheader("Total number of constructions")
            st.image("serie_tiempo_numero_obras_en_construccion_total.png", caption="Library: Seaborn", use_column_width=True)
        with derecha1: 
            st.subheader("Total area")
            st.image("serie_tiempo_area_total.png", caption="Library: Seaborn", use_column_width=True)
        with centro1:
            st.subheader("Total value")
            st.image("serie_tiempo_valor_total.png", caption="Library: Seaborn", use_column_width=True)
    with st.container():
        izquierda1,centro1, derecha1 = st.columns((1,1,1))
        with izquierda1:
            st.subheader("Total n. of residencials constructions")
            st.image("serie_tiempo_numero_obras_en_construccion_residenciales.png", caption="Library: Seaborn", use_column_width=True)
        with derecha1: 
            st.subheader("Total residencial area")
            st.image("serie_tiempo_area_residenciales.png", caption="Library: Seaborn", use_column_width=True)
        with centro1:
            st.subheader("Total residencial value")
            st.image("serie_tiempo_valor_residenciales.png", caption="Library: Seaborn", use_column_width=True)
    with st.container():
        izquierda1,centro1, derecha1 = st.columns((1,1,1))
        with izquierda1:
            st.subheader("Total n. of nonresidencials constructions")
            st.image("serie_tiempo_numero_obras_en_construccion_noresidenciales.png", caption="Library: Seaborn", use_column_width=True)
        with derecha1: 
            st.subheader("Total residencial area")
            st.image("serie_tiempoo_area_no_residenciales.png", caption="Library: Seaborn", use_column_width=True)
        with centro1:
            st.subheader("Total nonresidencial value")
            st.image("serie_tiempo_valor_noresidenciales.png", caption="Library: Seaborn", use_column_width=True)  
    st.title("Correlation Matrix")
    st.image("correlation.png", caption="Library: Seaborn", use_column_width=True)
    st.title("Pairplot per Cantons")
    st.image("pairplotpercanton.png", caption="Library: Seaborn", use_column_width=True)
    st.title("Standardized Growth of All Cantons of Costa Rica in 10 Years")
    st.image("tasa_crecimiento_estandarizado.png", caption="Library: Seaborn", use_column_width=True)
    st.title("Top Cantons with Maximum Growth in Costa Rica Over 10 Years")
    st.image("top15_cantones.png", caption="Library: Seaborn", use_column_width=True)
    st.header("Interactive map with the Top Cantons with Maximum Growth in Costa Rica Over 10 Years")
    st.components.v1.html(m._repr_html_(), height=500)
    with st.container():
        izquierda1, derecha1 = st.columns((1,1))
        with izquierda1:
            st.subheader("Cantons with Cost per Square Meter Above and Below the General Average in Costa Rica in 10 Years")
            st.image("cantones_costo_metro_cuadrado.png", caption="Library: Seaborn", use_column_width=True)
        with derecha1: 
            st.subheader("Cantons in Quintiles of Cost per Square Meter in Costa Rica in 10 Years")
            st.image("cantones_costo_quintiles_costo_metro_cuadrado.png", caption="Library: Seaborn", use_column_width=True)
    
    st.write("___") 
            
def page2():
    st.title("Image Embedding and Clustering")
    st.write("Converted the satellite images into numerical vectors using a pre-trained deep learning model. Each image is resized, normalized, and embedded into a feature vector. Subsequently applied the K-Means clustering algorithm to group these vectors, resulting in clusters of similar images.")
    st.title("Visualization and Similarity Analysis")
    st.write("Employed visualization techniques such as PCA (Principal Component Analysis) and t-SNE (t-distributed Stochastic Neighbor Embedding) to visualize the clustered data. These visualizations provide insights into the relationships between the clusters. Additionally calculated Euclidean distances and cosine similarities between images to identify the degree of similarity to the cantons of maximum growth found on the EDA, which aids in determining potential growth areas based on the characteristics of the satellite images.")
    st.title("PCA Clustering")
    st.image("PCA_clustering.png", caption="", use_column_width=True)
    st.write("___")
    st.title("TSNE Clustering")
    st.image("TSNE_clustering.png", caption="", use_column_width=True)
    st.write("___")
    st.title("The 5 cantons with the greatest growing are")
    st.header("La Unión, San José, Bagaces, Cañas, Tibás.")
    st.components.v1.html(m1._repr_html_(), height=500)
    st.header("Using cosine similarity, the cantons that have similar features to the top 5 were.")
    st.markdown("""
    ### - Similar to La Unión: 
    Turrialba,
    Paraíso,
    Tilarán,
    Cañas,
    Flores
    ### - Similar to the San José:
    Montes_de_Oca,
    Goicoechea,
    Tibás ,
    Oreamuno,
    Alajuelita
    ### - Similar to the Bagaces:   
    Cañas,
    Liberia,
    Turrialba,
    Orotina,
    Tilarán
    ### - Similar to the Cañas
    Turrialba,
    Bagaces ,
    Santa_Bárbara,
    Tilarán,
    Nicoya
    ### - Similar to the Tibás
    Moravia,
    Heredia,
    Alajuelita,
    Oreamuno,
    Desamparados
    """
    )
    st.header("In summary, our analysis of cantons using cosine similarity revealed a strong presence of green hues in their RGB composition, indicating ample undeveloped land. This suggests future potential for increased construction activity in these areas")
    

# Create the multipage app
def main():
    st.sidebar.title("Navigation")
    pages = ["Home", "Exploratory Data Analysis", "Solution"]
    state.page = st.sidebar.radio("Go to", pages)

    if state.page == "Home":
        home_page()
    elif state.page == "Exploratory Data Analysis":
        page1()
    elif state.page == "Solution":
        page2()

if __name__ == "__main__":
    main()
    
    