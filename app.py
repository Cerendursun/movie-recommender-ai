import streamlit as st
import pandas as pd
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# -----------------------
# CONFIG
# -----------------------
st.set_page_config(page_title="AI Movie Recommender", layout="wide")

OMDB_API_KEY = "30abedce"

# -----------------------
# DATA
# -----------------------
df = pd.read_csv("tmdb_5000_movies.csv")
df["overview"] = df["overview"].fillna("")

# -----------------------
# MODEL (RAM SAFE)
# -----------------------
tfidf = TfidfVectorizer(stop_words="english", max_features=5000)
matrix = tfidf.fit_transform(df["overview"])

# RAM patlamaz
cosine_sim = linear_kernel(matrix, matrix)

# -----------------------
# POSTER (OMDb)
# -----------------------
def get_poster(title):
    try:
        url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
        res = requests.get(url).json()

        if res.get("Response") == "True":
            poster = res.get("Poster")
            if poster and poster != "N/A":
                return poster
    except:
        return None

# -----------------------
# UI STYLE (RESPONSIVE FIX)
# -----------------------
st.markdown("""
<style>

/* SAYFA GENİŞLİĞİ */
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

/* BAŞLIK */
.title {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: #00d4ff;
}

/* KART */
.movie-card {
    background-color: #1c1f26;
    padding: 8px;
    border-radius: 10px;
    text-align: center;
    transition: 0.3s;
}

/* POSTER */
.movie-card img {
    width: 100%;
    height: 220px;
    object-fit: cover;
    border-radius: 8px;
}

/* HOVER */
.movie-card:hover {
    transform: scale(1.05);
    background-color: #2a2f3a;
}

/* MOBİL */
@media (max-width: 768px) {
    .title {
        font-size: 26px;
    }
}

</style>
""", unsafe_allow_html=True)

# -----------------------
# HEADER
# -----------------------
st.markdown('<div class="title">🎬 AI Movie Recommender</div>', unsafe_allow_html=True)
st.write("Film seç → sana benzerlerini bulayım")

# -----------------------
# SEARCH
# -----------------------
movie_list = sorted(df["title"].dropna().unique())
selected_movie = st.selectbox("🔍 Film seç", movie_list)

# -----------------------
# RECOMMENDATION
# -----------------------
if st.button("🚀 Önerileri Göster"):

    idx = df[df["title"] == selected_movie].index[0]

    scores = list(enumerate(cosine_sim[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:11]

    st.subheader("🎯 Önerilen Filmler")

    # 🔥 5 kolon (küçük kart fix)
    cols = st.columns(5)

    for index, i in enumerate(scores):
        col = cols[index % 5]

        movie_title = df.iloc[i[0]]["title"]
        percent = round(cosine_sim[idx][i[0]] * 100, 2)
        poster = get_poster(movie_title)

        with col:
            st.markdown(f"""
            <div class="movie-card">
                <img src="{poster}">
                <p><b>{movie_title}</b></p>
                <p>🎯 %{percent}</p>
            </div>
            """, unsafe_allow_html=True)