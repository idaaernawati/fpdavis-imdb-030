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

# Sidebar for navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
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
        **Narasi Grafik**: Grafik batang di atas menampilkan perbandingan rating dari berbagai judul film yang ada dalam dataset. Pada sumbu horizontal (X) ditampilkan judul-judul film, sementara sumbu vertikal (Y) menunjukkan nilai rating dari setiap film. Tinggi setiap batang pada grafik menunjukkan besarnya rating yang diterima oleh film tersebut, di mana semakin tinggi batang, semakin tinggi pula rating film tersebut. Dengan visualisasi ini, dapat di gunakan untuk mengidentifikasi film mana yang memiliki rating tertinggi dan terendah, serta melihat distribusi rating di antara berbagai judul film.
        """)

elif selected_aspect == "Relationship":
    st.subheader("Relationship Chart - Scatter Plot")
    # Contoh Scatter Plot: Hubungan antara budget dan gross
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Budget', y='Gross_us', data=df1)
    plt.title("Relationship between Budget and Gross Revenue")
    st.pyplot(plt)
    **Narasi Grafik**: Grafik scatter plot di atas menampilkan hubungan antara anggaran (budget) dan pendapatan kotor (gross revenue) dari berbagai film yang ada dalam dataset. Pada sumbu horizontal (X) ditampilkan anggaran film, sedangkan pada sumbu vertikal (Y) ditampilkan pendapatan kotor yang dihasilkan oleh film tersebut. Setiap titik pada grafik mewakili satu film, dengan posisi titik menunjukkan besarnya anggaran dan pendapatan kotor. Melalui visualisasi ini, pola hubungan antara anggaran dan pendapatan kotor dapat terlihat, seperti apakah film dengan anggaran lebih besar cenderung menghasilkan pendapatan yang lebih tinggi. Grafik ini membantu dalam menganalisis bagaimana investasi dalam anggaran film berkorelasi dengan keberhasilan finansialnya di box office.
        """)

elif selected_aspect == "Composition":
    st.subheader("Composition Chart - Donut Chart")
    # Contoh Donut Chart: Komposisi genre film
    genre_counts = df1['Genre'].value_counts()
    plt.figure(figsize=(10, 10))
    plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.3))
    plt.title("Composition of Movie Genres")
    st.pyplot(plt)
    **Narasi Grafik**: Grafik donat di atas menampilkan komposisi genre film dalam dataset. Setiap sektor pada grafik mewakili satu genre film, dengan ukuran sektor yang proporsional terhadap jumlah film dalam genre tersebut. Persentase di setiap sektor menunjukkan proporsi masing-masing genre terhadap keseluruhan dataset. Dengan visualisasi ini, kita dapat dengan mudah melihat genre film yang paling dominan serta seberapa besar kontribusi setiap genre terhadap keseluruhan komposisi film. 
        """)

elif selected_aspect == "Distribution":
    st.subheader("Distribution Chart - Line Chart")
    # Contoh Line Chart: Distribusi rating film
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df1['Rating'])
    plt.title("Distribution of Movie Ratings")
    st.pyplot(plt)
**Narasi Grafik**: Grafik garis di atas menampilkan distribusi rating film dalam dataset. Sumbu horizontal (X) mewakili indeks atau urutan film dalam dataset, sedangkan sumbu vertikal (Y) menunjukkan nilai rating dari setiap film. Garis pada grafik menggambarkan perubahan rating dari satu film ke film lainnya, memberikan pandangan tentang bagaimana rating bervariasi di seluruh dataset. Dengan visualisasi ini, kita dapat mengidentifikasi pola atau tren dalam rating film, seperti adanya periode dengan rating tinggi atau rendah yang konsisten.
        """)

st.markdown("""
<style>
.sidebar .sidebar-content {
    background-color: #f0f2f6;
}
</style>
""", unsafe_allow_html=True)
