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
    st.subheader("Comparison Chart - Bar Chart")
    # Contoh Bar Chart: Membandingkan rating film
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Title', y='Rating', data=df1)
    plt.xticks(rotation=90)
    plt.title("Comparison of Movie Ratings")
    st.pyplot(plt)
    st.markdown("""
        **Narasi Grafik**: Grafik batang di atas menampilkan perbandingan rating berbagai film. Pada sumbu horizontal, terdapat judul-judul film yang disusun secara vertikal agar lebih mudah dibaca. Sementara itu, sumbu vertikal menunjukkan nilai rating dari setiap film. Tinggi masing-masing batang mewakili rating yang diperoleh film tersebut, memungkinkan kita untuk dengan cepat membandingkan popularitas atau kualitas relatif dari setiap film berdasarkan rating yang diberikan. Judul grafik, "Comparison of Movie Ratings," memberikan konteks yang jelas bahwa fokus utama adalah pada perbandingan rating film. Melalui visualisasi ini, kita bisa mengidentifikasi film mana yang mendapatkan rating tertinggi dan terendah, serta melihat distribusi rating secara keseluruhan.
        """)

elif selected_aspect == "Relationship":
    st.subheader("Relationship Chart - Scatter Plot")
    # Contoh Scatter Plot: Hubungan antara budget dan gross
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Budget', y='Gross_us', data=df1)
    plt.title("Relationship between Budget and Gross Revenue")
    st.pyplot(plt)
    st.markdown("""
        **Narasi Grafik**: Grafik scatter plot di atas menampilkan hubungan antara anggaran (budget) dan pendapatan kotor (gross revenue) dari berbagai film. Pada sumbu horizontal, ditampilkan nilai anggaran yang dialokasikan untuk masing-masing film, sedangkan pada sumbu vertikal, tercatat pendapatan kotor yang dihasilkan oleh film tersebut. Setiap titik pada grafik mewakili satu film, sehingga kita dapat melihat pola atau tren tertentu dalam data. Judul grafik, "Relationship between Budget and Gross Revenue," menjelaskan fokus utama dari analisis ini, yaitu untuk menilai bagaimana anggaran film berhubungan dengan pendapatan yang dihasilkan. Melalui visualisasi ini, kita dapat mengamati apakah ada kecenderungan bahwa film dengan anggaran lebih besar cenderung menghasilkan pendapatan kotor yang lebih tinggi, atau jika ada outlier yang menonjol dengan anggaran kecil namun pendapatan besar, atau sebaliknya.
        """)

elif selected_aspect == "Composition":
    st.subheader("Composition Chart - Donut Chart")
    # Contoh Donut Chart: Komposisi genre film
    genre_counts = df1['Genre'].value_counts()
    plt.figure(figsize=(15, 17))
    plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.3))
    plt.title("Composition of Movie Genres")
    st.pyplot(plt)
    st.markdown("""
        **Narasi Grafik**: Grafik donat di atas menampilkan komposisi genre film yang ada dalam dataset. Setiap segmen pada grafik merepresentasikan satu genre film, dengan ukuran segmen yang proporsional terhadap jumlah film dalam genre tersebut. Persentase di dalam setiap segmen menunjukkan proporsi masing-masing genre dalam keseluruhan kumpulan data. Judul grafik, "Composition of Movie Genres," menjelaskan bahwa fokus utama adalah untuk menunjukkan distribusi berbagai genre film. Melalui visualisasi ini, kita dapat dengan mudah melihat genre mana yang paling dominan dan seberapa besar kontribusi masing-masing genre terhadap total keseluruhan. Grafik donat ini memberikan gambaran yang jelas dan intuitif tentang bagaimana berbagai genre film terdistribusi dalam dataset.
        """)

elif selected_aspect == "Distribution":
    st.subheader("Distribution Chart - Line Chart")
    # Contoh Line Chart: Distribusi rating film
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df1['Rating'])
    plt.title("Distribution of Movie Ratings")
    st.pyplot(plt)
    st.markdown("""
        **Narasi Grafik**: Grafik garis di atas menampilkan distribusi rating film dalam dataset. Sumbu horizontal merepresentasikan urutan data rating film, sementara sumbu vertikal menunjukkan nilai rating tersebut. Setiap titik pada grafik dihubungkan dengan garis, memberikan visualisasi yang jelas tentang bagaimana rating film terdistribusi. Judul grafik, "Distribution of Movie Ratings," menekankan bahwa fokus utama adalah pada distribusi nilai rating. Melalui visualisasi ini, kita dapat mengamati pola atau tren tertentu dalam rating film, seperti apakah terdapat banyak film dengan rating tinggi atau rendah, dan bagaimana variasi rating tersebut tersebar. Grafik ini membantu kita memahami bagaimana kualitas film dinilai secara keseluruhan dalam dataset.
        """)

st.markdown("""
<style>
.sidebar .sidebar-content {
    background-color: #f0f2f6;
}
</style>
""", unsafe_allow_html=True)
