import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Nama file CSV
fn1 = 'top_picks_film.csv'

# Menampilkan judul di halaman web
st.title("Scraping Film IMDB")

# Membaca file CSV ke dalam DataFrame dengan encoding 'latin1'
df1 = pd.read_csv(fn1, encoding='latin1')

# Menampilkan DataFrame sebagai tabel
st.dataframe(df1)

# Membuat dropdown untuk memilih aspek visualisasi
aspects = ["Comparison", "Relationship", "Composition", "Distribution"]
selected_aspect = st.sidebar.selectbox("Pilih Aspek Visualisasi", aspects)

# Menampilkan visualisasi berdasarkan aspek yang dipilih
if selected_aspect == "Comparison":
    st.subheader("Comparison Chart - Bar Chart")
    # Contoh Bar Chart: Membandingkan rating film
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Title', y='Rating', data=df1)
    plt.xticks(rotation=90)
    plt.title("Comparison of Movie Ratings")
    st.pyplot(plt)

elif selected_aspect == "Relationship":
    st.subheader("Relationship Chart - Scatter Plot")
    # Contoh Scatter Plot: Hubungan antara budget dan gross
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Budget', y='Gross_us', data=df1)
    plt.title("Relationship between Budget and Gross Revenue")
    st.pyplot(plt)

elif selected_aspect == "Composition":
    st.subheader("Composition Chart - Donut Chart")
    # Contoh Donut Chart: Komposisi genre film
    genre_counts = df1['Genre'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.3))
    plt.title("Composition of Movie Genres")
    st.pyplot(plt)

elif selected_aspect == "Distribution":
    st.subheader("Distribution Chart - Line Chart")
    # Contoh Line Chart: Distribusi rating film
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df1['Rating'])
    plt.title("Distribution of Movie Ratings")
    st.pyplot(plt)

# Menambahkan dekorasi untuk mempercantik tampilan
st.sidebar.markdown("### Filter Options")
st.sidebar.markdown("You can choose different aspects of visualization using the dropdown above.")
st.sidebar.markdown("Enjoy exploring the movie data!")

st.markdown("""
<style>
.sidebar .sidebar-content {
    background-color: #f0f2f6;
}
</style>
""", unsafe_allow_html=True)
