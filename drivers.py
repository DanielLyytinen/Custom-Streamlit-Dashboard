import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pydeck as pdk

st.text("Formula 1 World Championship (1950 - 2024)")

drivers = pd.read_csv('drivers.csv')
circuits = pd.read_csv('circuits.csv')

st.header('Kuljettajien määrä per maa')

driver_counts = drivers['nationality'].value_counts().reset_index()
driver_counts.columns = ['Nationality', 'Number of Drivers']

st.dataframe(driver_counts)

st.bar_chart(driver_counts.set_index('Nationality'))

st.header('Ratojen sijainnit kartalla')

circuit_locations = circuits[['name', 'location', 'country', 'lat', 'lng']].dropna()

st.map(circuit_locations.rename(columns={'lat': 'latitude', 'lng': 'longitude'}))

