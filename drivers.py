import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pydeck as pdk

st.text("Formula 1 World Championship (1950 - 2024)")

drivers = pd.read_csv('drivers.csv')
circuits = pd.read_csv('circuits.csv')

# 1. Kuljettajien määrä maittain
st.header('Kuljettajien määrä per maa')

# Oletan että 'nationality' sarake kertoo kuljettajien kansallisuuden
driver_counts = drivers['nationality'].value_counts().reset_index()
driver_counts.columns = ['Nationality', 'Number of Drivers']

st.dataframe(driver_counts)

# Voit myös näyttää pylväsdiagrammina:
st.bar_chart(driver_counts.set_index('Nationality'))

# 2. Ratojen sijainnit kartalla
st.header('Ratojen sijainnit kartalla')

# Oletan että 'lat' ja 'lng' sarakkeet ovat ratojen sijainnit
circuit_locations = circuits[['name', 'location', 'country', 'lat', 'lng']].dropna()

# Näytetään kartalla
st.map(circuit_locations.rename(columns={'lat': 'latitude', 'lng': 'longitude'}))

