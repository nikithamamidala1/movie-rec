# utils/helpers.py

import pandas as pd
import re

def clean_text(text):
    """
    Basic cleaning of overview or any text data:
    - Lowercasing
    - Removing special characters
    """
    if pd.isnull(text):
        return ""
    
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text.strip()

def format_genres(genre_str):
    """
    Replace '|' with commas for better display of genres.
    """
    if pd.isnull(genre_str):
        return ""
    return genre_str.replace('|', ', ')

def get_movie_by_title(df, title):
    """
    Returns movie row if title exists (case-insensitive), else None.
    """
    matches = df[df['title'].str.lower() == title.lower()]
    return matches.iloc[0] if not matches.empty else None
