import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# Load the data
fn1 = 'top_picks_film.csv'
df1 = pd.read_csv(fn1, encoding='latin1')

# Title
st.title("Scraping Film IMDB")

# Sidebar for selecting aspect
st.sidebar.title("Choose an Aspect")
aspect = st.sidebar.selectbox("Select the aspect to visualize", 
                              ("Comparison", "Relationship", "Composition", "Distribution"))

# Main content
st.dataframe(df1)

if aspect == "Comparison":
    # Comparison - Bar Chart
    st.header("Comparison of Movie Ratings")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x='Rating', y='Title', data=df1.sort_values(by='Rating', ascending=False), ax=ax)
    ax.set_title('Comparison of Movie Ratings')
    ax.set_xlabel('Rating')
    ax.set_ylabel('Movie Title')
    st.pyplot(fig)
    st.write("This bar chart compares the ratings of different movies. It helps identify which movies have higher ratings and are potentially more popular or well-received.")

elif aspect == "Relationship":
    # Relationship - Scatter Plot
    st.header("Relationship of Movie Ratings")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.scatterplot(x='Rating', y='Title', data=df1, ax=ax)
    ax.set_title('Relationship of Movie Ratings')
    ax.set_xlabel('Rating')
    ax.set_ylabel('Movie Title')
    st.pyplot(fig)
    st.write("This scatter plot shows the relationship of movie ratings. Each point represents a movie, helping us see any patterns or clusters in the ratings.")

elif aspect == "Composition":
    # Composition - Donut Chart
    st.header("Composition of Movie Ratings")
    rating_counts = df1['Rating'].value_counts()
    fig = go.Figure(data=[go.Pie(labels=rating_counts.index, values=rating_counts.values, hole=.3)])
    fig.update_layout(title_text='Composition of Movie Ratings')
    st.plotly_chart(fig)
    st.write("This donut chart illustrates the composition of movie ratings. It shows the proportion of movies that fall within different rating categories.")

elif aspect == "Distribution":
    # Distribution - Line Chart
    st.header("Distribution of Movie Ratings")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.lineplot(x='Title', y='Rating', data=df1, ax=ax)
    ax.set_title('Distribution of Movie Ratings')
    ax.set_xlabel('Movie Title')
    ax.set_ylabel('Rating')
    ax.tick_params(axis='x', rotation=90)
    st.pyplot(fig)
    st.write("This line chart displays the distribution of movie ratings. It helps us understand how ratings vary across different movies, showing trends and fluctuations.")

# Run the Streamlit app with: streamlit run script_name.py
