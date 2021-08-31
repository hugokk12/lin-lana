
import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium
from folium.plugins import HeatMap
import json
import numpy as np
import matplotlib.pyplot as plt
import random
import pickle
import plotly.express as px
import streamlit.components.v1 as components
import statistics




#----------DEFINIÇÃO DA LAT LON
def get_user_date():
            
            grupo = st.sidebar.number_input("Selecionar Grupo",1, 9,1, step=1)

            user_data = {'grupo': grupo}

            return user_data

#----------MAIN
def main():
    
    col1, col2, col3 = st.columns([1,10,1])
    with col2:
        user_input_variables = get_user_date()
        grupo = user_input_variables['grupo']
        if grupo==1:
            st.write('Queridas Lin e Lana,')
            st.write('não tenho como agradecer pelo todo carinho e dedicaçõ que tiveram em preparar as aulas e por separar esse conteúdo maravilhoso. É sério, não tem como. A crise ta braba. Manda nuggets pls')
        elif grupo==2:
            st.write('texto grupo 2')
        else: 
            st.write('galeris, vcs entenderam a lógica')
        st.write('Att., Grupo {}'.format(grupo))
        
    col1, col2, col3 = st.columns([1,1,1])
    
    with col2:
        st.write('#manda nuggets')
        st.image('nuggets.jpg', width=200)
        st.image('love.gif')

    


main()

