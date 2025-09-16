import streamlit as st
import pandas as pd

# Load the CSV
df = pd.read_csv('data/movies.csv')

st.title("🎬 Movie Explorer")

# Loop through each row and display movie details
for _, row in df.iterrows():
    st.subheader(row['title'])              # Movie Title
    st.write(f"**Genres:** {row['genres']}") # Genres
    st.write(row['overview'])               # Overview

    # Display poster from URL if available
    if 'poster_url' in row and pd.notnull(row['poster_url']):
        st.image(row['poster_url'], width=200)
    
    st.markdown("---")  # Add a line separator between movies
