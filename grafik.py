import pandas as pd
import streamlit as st

# Nama file CSV
fn1 = 'top_picks_film.csv'

# Menampilkan judul di halaman web
st.title("Scraping Film IMDB")

# Membaca file CSV ke dalam DataFrame dengan encoding 'latin1'
df1 = pd.read_csv(fn1, encoding='latin1')

# Menampilkan DataFrame sebagai tabel
st.dataframe(df1)