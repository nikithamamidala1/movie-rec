import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data(path='data/movies.csv'):
    return pd.read_csv(path)

def create_similarity_matrix(df):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['overview'].fillna(''))
    similarity = cosine_similarity(tfidf_matrix)
    return similarity

def recommend_movies(title, df, similarity_matrix, n=5):
    if title not in df['title'].values:
        return []

    idx = df[df['title'] == title].index[0]
    scores = list(enumerate(similarity_matrix[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:n+1]
    movie_indices = [i[0] for i in scores]
    return df.iloc[movie_indices]
