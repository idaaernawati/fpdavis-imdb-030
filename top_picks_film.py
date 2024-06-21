import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Nama file CSV
fn1 = 'top_picks_film.csv'

# Menampilkan judul di halaman web
st.title("Visualization Scraping Film IMDB")

# Membaca file CSV ke dalam DataFrame dengan encoding 'latin1'
df1 = pd.read_csv(fn1, encoding='latin1')

# Menampilkan DataFrame sebagai tabel
st.dataframe(df1)

# Sidebar for navigation
st.sidebar.title("Navigation")
selected_aspect = st.sidebar.selectbox(
    'Select Analysis Aspect',
    ('Comparison', 'Relationship', 'Composition', 'Distribution')
)

# Menampilkan visualisasi berdasarkan aspek yang dipilih
if selected_aspect == "Comparison":
    st.subheader("Comparison - Bar Chart")
    # Contoh Bar Chart: Membandingkan rating film
    plt.figure(figsize=(11, 7))
    sns.barplot(x='Title', y='Rating', data=df1)
    plt.xticks(rotation=90)
    plt.title("Comparison of Movie Ratings")
    st.pyplot(plt)
    st.markdown("""
        **Narasi Grafik**: Grafik batang di atas menampilkan perbandingan rating beberapa film populer. Judul film tercantum pada sumbu X, sedangkan rating film tercantum pada sumbu Y. Semakin tinggi batang, semakin tinggi rating film tersebut. Dari grafik tersebut, dapat dilihat bahwa film dengan rating tertinggi adalah Spider-Man: No Way Home, dengan rating 4.5. Disusul dengan Mad Max: Fury Road dengan rating 4.3 dan King Kong dengan rating 4.2. Film dengan rating terendah adalah Oppenheimer, Pacific Rim, dan Bullet Train, dengan rating sama yaitu 3.0. Secara umum, film-film yang ditampilkan dalam grafik ini memiliki rating yang cukup tinggi, dengan rata-rata rating 3.8. Hal ini menunjukkan bahwa film-film tersebut umumnya disukai oleh para penonton.
        """)

elif selected_aspect == "Relationship":
    st.subheader("Relationship - Scatter Plot")
    # Contoh Scatter Plot: Hubungan antara budget dan gross
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x='Budget', y='Gross_us', data=df1)
    plt.title("Relationship between Budget and Gross Revenue")
    st.pyplot(plt)
    st.markdown("""
        **Narasi Grafik**: Grafik scatter plot di atas menampilkan hubungan antara anggaran (budget) dan pendapatan kotor (gross revenue) dari berbagai film. Hal ini dapat diartikan bahwa semakin besar anggaran film, semakin besar pula potensi pendapatan kotornya. Film dengan anggaran di atas 100 juta cenderung memiliki pendapatan kotor yang lebih tinggi dibandingkan film dengan anggaran dibawah 100 juta. Beberapa film dengan anggaran besar, seperti "Avatar" dan "Titanic", berhasil mencapai pendapatan kotor yang sangat tinggi. Ada beberapa film dengan anggaran kecil yang meraih kesuksesan besar, seperti "The Blair Witch Project" dan "Paranormal Activity". Secara keseluruhan, grafik ini menunjukkan bahwa anggaran film merupakan salah satu faktor yang dapat memengaruhi pendapatan kotornya.
        """)

elif selected_aspect == "Composition":
    st.subheader("Composition - Donut Chart")
    # Contoh Donut Chart: Komposisi genre film
    genre_counts = df1['Genre'].value_counts()
    plt.figure(figsize=(17, 19))
    plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.3))
    plt.title("Composition of Movie Genres")
    st.pyplot(plt)
    st.markdown("""
        **Narasi Grafik**: Grafik donat di atas menampilkan komposisi genre film berdasarkan data dari IMDb. Grafik ini dibagi menjadi beberapa segmen yang mewakili genre film yang berbeda, dengan persentase masing-masing genre tertera di samping segmennya. Grafik ini menunjukkan bahwa genre action, action, adventure, sci-fi, dan drama adalah genre film yang paling populer. Genre-genre ini banyak diminati oleh para penonton karena menawarkan berbagai macam hiburan, seperti aksi, petualangan, fiksi ilmiah, dan drama. Genre horror dan animation masih memiliki peminat, meskipun persentasenya tidak sebesar genre-genre lainnya.
        """)

elif selected_aspect == "Distribution":
    st.subheader("Distribution - Line Chart")
    # Contoh Line Chart: Distribusi rating film
    plt.figure(figsize=(13, 9))
    sns.lineplot(data=df1['Rating'])
    plt.title("Distribution of Movie Ratings")
    st.pyplot(plt)
    st.markdown("""
        **Narasi Grafik**: Grafik garis distribusi rating film di atas, dapat diamati bahwa rating film terbanyak berkisar antara 7.0 hingga 7.5. Hal ini menunjukkan bahwa sebagian besar film yang ditampilkan pada platform tersebut memiliki kualitas yang cukup baik dan diterima oleh para penonton. Meskipun rating film terbanyak berkisar antara 7.0 hingga 7.5, terdapat beberapa film dengan rating yang lebih tinggi dan lebih rendah. Hal ini menunjukkan bahwa platform tersebut tidak hanya menampilkan film-film mainstream yang populer di kalangan masyarakat luas, tetapi juga film-film indie atau film-film klasik yang mungkin disukai oleh sekelompok kecil pengguna. Secara keseluruhan, grafik distribusi rating film di atas menunjukkan bahwa platform tersebut menyediakan berbagai jenis film dengan kualitas yang beragam, sehingga dapat memenuhi kebutuhan dan selera para penggunanya.
        """)

st.markdown("""
<style>
.sidebar .sidebar-content {
    background-color: #f0f2f6;
}
</style>
""", unsafe_allow_html=True)
