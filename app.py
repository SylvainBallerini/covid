from pandas._config.config import options
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

data = pd.read_csv("owid-covid-data.csv")

options_death = st.multiselect('Quel pays pour une comparaison ?', data['location'].unique(),['France'])

#st.write('Le(s) pays sélectionnées : ', options_death)

df = data[data['location'].isin(options_death)]
fig = px.line(df, x='date', y='total_deaths', title="Nombres de morts par le Covid dans les pays", color='location', 
width=800)

fig.update_layout(xaxis_title = 'Date', yaxis_title = 'Total de morts')

st.plotly_chart(fig)

fig = px.line(df, x='date', y='total_deaths_per_million', title="Nombres de morts par le Covid par millios d'habitants", color='location', 
width=800)

fig.update_layout(xaxis_title = 'Date', yaxis_title = "Total de morts par millions d'habitants")

st.plotly_chart(fig)