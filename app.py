import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv(r"github_dataset.csv")
    data.columns = data.columns.str.strip()  # Clean column names
    return data

data = load_data()

# Display data overview
st.title('GitHub Repositories Dashboard')
st.write('Data Preview:', data.head())
st.write('Columns in the dataset:', data.columns)

# Repository Stars Distribution visualization
st.subheader('Visualization: Repository Stars Distribution')
if 'stars_count' in data.columns:
    st.bar_chart(data['stars_count'].value_counts())
else:
    st.error("The 'stars_count' column does not exist in the dataset.")

# Repository Forks Distribution visualization
st.subheader('Visualization: Repository Forks Distribution')
if 'forks_count' in data.columns:
    st.bar_chart(data['forks_count'].value_counts())
else:
    st.error("The 'forks_count' column does not exist in the dataset.")

# Issues Count Distribution visualization
st.subheader('Visualization: Issues Count Distribution')
if 'issues_count' in data.columns:
    st.bar_chart(data['issues_count'].value_counts())
else:
    st.error("The 'issues_count' column does not exist in the dataset.")

# Top 10 Repositories by Stars visualization
st.subheader('Top 10 Repositories by Stars')
if 'stars_count' in data.columns:
    top_10_stars = data[['repositories', 'stars_count']].sort_values(by='stars_count', ascending=False).head(10)
    st.bar_chart(top_10_stars.set_index('repositories')['stars_count'])
else:
    st.error("The 'stars_count' column does not exist in the dataset.")

# Language Distribution visualization
st.subheader('Language Distribution')
if 'language' in data.columns:
    st.bar_chart(data['language'].value_counts())
else:
    st.error("The 'language' column does not exist in the dataset.")

# Filter by programming language
st.subheader('Filter Repositories by Programming Language')
if 'language' in data.columns:
    selected_language = st.selectbox('Select a Programming Language', data['language'].unique())
    filtered_data = data[data['language'] == selected_language]
    st.write(f'Repositories using {selected_language}:', filtered_data)
else:
    st.error("The 'language' column does not exist in the dataset.")
