
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
            
            grupo = st.sidebar.number_input("SeleGrupo",1, 9,1, step=1)
            with st.form(key='my_form'):
                text_input = st.text_input(label='Enter your name')
                submit_button = st.form_submit_button(label='Submit')

            user_data = {'grupo': grupo,
                        'form': text_input}

            return user_data

#----------MAIN
def main():
    user_input_variables = get_user_date()
    grupo = user_input_variables['grupo']
    if grupo==1:
        st.write('Queridas Lin e Lana, /n não tenho como agradecer pelo todo carinho e dedicaçõ que tiveram em preparar as aulas e por separar esse conteúdo maravilhoso. É sério, não tem como. A crise ta braba. Manda nuggets pls')
    if grupo==2:
        st.write('texto grupo 2')
    else: 
        st.write('galeris, vcs entenderam a lógica')
    st.write('Att., Grupo {}'.format(grupo))
    st.write('#manda nuggets')
    st.write(user_input_variables['form'])
    st.image('nuggets.jpg')
    st.image('love.gif')


#----------FUNCAO DE ESTIMATIVA DE DENSIDADE DE CRIMES
    


main()

