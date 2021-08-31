
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
            
            latitude_slider = st.sidebar.number_input("Latitude (entre -23.72412 e -23.46010)",-23.72412, -23.46010,-23.60000, step=0.01, format="%.5f")

            user_data = {'componente': latitude_slider}
                         
            return user_data

#----------MAIN
def main():
    user_input_variables = get_user_date()


    #st.sidebar.write(int(user_input_variables['cep']))

    st.sidebar.write('#manda nuggets')


#----------FUNCAO DE ESTIMATIVA DE DENSIDADE DE CRIMES
    


main()

