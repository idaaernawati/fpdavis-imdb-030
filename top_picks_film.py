import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Koneksi ke database
def create_connection():
    try:
        conn = mysql.connector.connect(
            host="kubela.id",
            user="davis2024irwan",
            password="wh451n9m@ch1n3", 
            port="3306",
            database="aw"
        )
        return conn
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return None

# Fungsi untuk menjalankan query dan mendapatkan hasil sebagai DataFrame
def execute_query(query):
    conn = create_connection()
    if conn is None:
        return pd.DataFrame()  # Return an empty DataFrame if connection fails
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return pd.DataFrame(data, columns=columns)
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return pd.DataFrame()

# Sidebar for navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    'Select Analysis Aspect',
    ('Comparison', 'Relationship', 'Composition', 'Distribution')
)

st.title("Visualization Dump Data Warehouse Adventure Works")

# Display selected aspect
if option == 'Comparison':
    st.header("Comparison - Bar Chart")
    query_comparison = """
    SELECT
        p.EnglishProductName AS ProductName,
        SUM(s.SalesAmount) AS TotalSales
    FROM
        factinternetsales s
    INNER JOIN
        dimproduct p ON s.ProductKey = p.ProductKey
    GROUP BY
        p.EnglishProductName;
    """
    comparison_data = execute_query(query_comparison)

    if not comparison_data.empty:
        fig1, ax1 = plt.subplots(figsize=(23, 10))
        ax1.bar(comparison_data['ProductName'], comparison_data['TotalSales'], color='skyblue')
        ax1.set_xlabel('Product Name')
        ax1.set_ylabel('Total Sales')
        ax1.set_title('Comparison of Total Sales by Product')
        ax1.set_xticks(range(len(comparison_data['ProductName'])))
        ax1.set_xticklabels(comparison_data['ProductName'], rotation=90)
        ax1.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(fig1)
        st.markdown("""
        **Narasi Grafik**: Grafik batang di atas menampilkan perbandingan total penjualan untuk setiap produk berdasarkan data dari database Adventure Works. Berdasarkan grafik, produk dengan total penjualan tertinggi adalah Produk 1 dengan total penjualan 12. Produk dengan total penjualan terendah adalah Produk 3 dengan total penjualan 0. Produk 2 memiliki total penjualan 3. Dengan kata lain, Produk 1 adalah produk yang paling laris, diikuti oleh Produk 2 dan Produk 3. Setiap batang mewakili sebuah produk, dengan tinggi batang menunjukkan jumlah total penjualan yang dihasilkan produk tersebut. Judul grafik serta label sumbu x dan y memberikan konteks yang jelas tentang informasi yang ditampilkan, dan garis-garis kisi horizontal membantu dalam memperkirakan nilai penjualan setiap produk dengan lebih mudah.
        """)
    else:
        st.warning("No data to display")

elif option == 'Relationship':
    st.header("Relationship - Scatter Plot")
    query_relationship = """
    SELECT fs.CustomerKey, fs.ProductKey,
           dc.FirstName, dc.LastName,
           dp.EnglishProductName
    FROM factinternetsales fs
    JOIN dimcustomer dc ON fs.CustomerKey = dc.CustomerKey
    JOIN dimproduct dp ON fs.ProductKey = dp.ProductKey
    """
    relationship_data = execute_query(query_relationship)

    if not relationship_data.empty:
        fig2, ax2 = plt.subplots(figsize=(17, 12))
        sns.scatterplot(data=relationship_data, x='CustomerKey', y='ProductKey', hue='EnglishProductName', ax=ax2)
        ax2.set_title('Relationship between Customers and Products')
        ax2.set_xlabel('Customer Key')
        ax2.set_ylabel('Product Key')
        ax2.legend(title='Product', loc='upper right', bbox_to_anchor=(1.25, 1))
        ax2.grid(True)
        st.pyplot(fig2)
        st.markdown("""
        **Narasi Grafik**: Grafik scatter plot di atas menampilkan hubungan antara pelanggan dan produk yang mereka beli berdasarkan data dari database Adventure Works. Setiap titik pada grafik mewakili satu transaksi, dengan sumbu x menunjukkan CustomerKey dan sumbu y menunjukkan ProductKey. Produk Finger Gloves adalah produk yang paling banyak dibeli oleh pelanggan. Hal ini dapat dilihat dari garis Finger Gloves yang berada di atas garis produk lainnya. Produk Purpose Gian Sta adalah produk yang paling sedikit dibeli oleh pelanggan. Hal ini dapat dilihat dari garis Purpose Gian Sta yang berada di bawah garis produk lainnya. 
        """)
    else:
        st.warning("No data to display")

elif option == 'Composition':
    st.header("Composition - Donut Chart")
    query_composition = """
    SELECT
        pc.EnglishProductCategoryName AS CategoryName,
        SUM(s.SalesAmount) AS TotalSales
    FROM
        factinternetsales s
    INNER JOIN
        dimproduct p ON s.ProductKey = p.ProductKey
    INNER JOIN
        dimproductsubcategory ps ON p.ProductSubcategoryKey = ps.ProductSubcategoryKey
    INNER JOIN
        dimproductcategory pc ON ps.ProductCategoryKey = pc.ProductCategoryKey
    GROUP BY
        pc.EnglishProductCategoryName;
    """
    composition_data = execute_query(query_composition)

    if not composition_data.empty:
        fig3, ax3 = plt.subplots(figsize=(8, 7))
        outer_colors = ['blue', 'red', 'green']
        ax3.pie(composition_data['TotalSales'], labels=composition_data['CategoryName'], autopct='%1.1f%%', startangle=140, colors=outer_colors, wedgeprops=dict(width=0.3, edgecolor='w'))
        inner_circle = plt.Circle((0, 0), 0.7, color='white')
        ax3.add_artist(inner_circle)
        ax3.set_title('Composition of Total Sales by Product Category')
        ax3.axis('equal')
        st.pyplot(fig3)
        st.markdown("""
        **Narasi Grafik**: Grafik donat di atas menampilkan komposisi total penjualan berdasarkan kategori produk dari data di database Adventure Works. Kategori produk yang paling banyak terjual dalam penjualan adalah kategori "Bikes". Kategori ini menyumbang 96,5% dari total penjualan. Kategori "Accessories" menempati urutan kedua dengan persentase penjualan sebesar 2,4%. Kategori "Clothing" menempati urutan terakhir dengan persentase penjualan sebesar 1,2%. Hal ini menunjukkan bahwa produk-produk dalam kategori "Bikes" lebih diminati oleh pembeli dibandingkan dengan produk-produk dalam kategori "Accessories" dan "Clothing". Setiap segmen pada grafik mewakili satu kategori produk, dengan ukuran segmen menunjukkan proporsi total penjualan yang dihasilkan oleh kategori tersebut.
        """)
    else:
        st.warning("No data to display")

elif option == 'Distribution':
    st.header("Distribution - Line Chart")
    query_distribution = """
    SELECT
        t.FullDateAlternateKey AS SalesDate,
        SUM(s.SalesAmount) AS TotalSales
    FROM
        factinternetsales s
    INNER JOIN
        dimtime t ON s.OrderDateKey = t.TimeKey
    GROUP BY
        t.FullDateAlternateKey;
    """
    distribution_data = execute_query(query_distribution)

    if not distribution_data.empty:
        distribution_data['SalesDate'] = pd.to_datetime(distribution_data['SalesDate'])
        fig4, ax4 = plt.subplots(figsize=(17, 13))
        ax4.plot(distribution_data['SalesDate'], distribution_data['TotalSales'], marker='o', color='green', linestyle='-')
        ax4.set_xlabel('Sales Date')
        ax4.set_ylabel('Total Sales')
        ax4.set_title('Distribution of Sales over Time')
        ax4.grid(True, linestyle='--', alpha=0.7)
        st.pyplot(fig4)
        st.markdown("""
        **Narasi Grafik**: Grafik garis di atas menampilkan distribusi total penjualan sepanjang waktu berdasarkan data dari database Adventure Works. Secara keseluruhan, penjualan produk mengalami peningkatan dari tahun 2002 hingga tahun 2004. Grafik ini tidak menunjukkan pola musiman yang jelas dalam penjualan produk. Selain itu penjualan produk juga menunjukkan tren peningkatan yang konsisten dari tahun 2002 hingga tahun 2004.
        """)
    else:
        st.warning("No data to display")
