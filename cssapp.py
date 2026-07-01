import os
import pickle
import streamlit as st

st.set_page_config(page_title="Pokemon Recommender", page_icon="⚡", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Nunito:wght@400;700;900&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"], .stApp {
    background-color: #0d0d1a !important;
    color: #f0f0f0;
    font-family: 'Nunito', sans-serif;
}

.hero {
    text-align: center;
    padding: 40px 20px 20px;
    background: radial-gradient(ellipse at top, #1a1a3e 0%, #0d0d1a 70%);
    border-bottom: 1px solid #2a2a4a;
    margin-bottom: 30px;
}

.hero-title {
    font-family: 'Press Start 2P', cursive;
    font-size: 28px;
    color: #f5c518;
    text-shadow: 0 0 30px rgba(245,197,24,0.4);
    letter-spacing: 3px;
    margin-bottom: 10px;
    animation: flicker 3s infinite;
}

.hero-sub {
    font-size: 14px;
    color: #8888aa;
    letter-spacing: 1px;
}

@keyframes flicker {
    0%, 95%, 100% { opacity: 1; }
    96% { opacity: 0.8; }
    97% { opacity: 1; }
    98% { opacity: 0.85; }
}

.pokeball-loader {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: linear-gradient(180deg, #e63946 50%, #f0f0f0 50%);
    border: 4px solid #222;
    position: relative;
    margin: 0 auto 20px;
    animation: spin 2s linear infinite;
}

.pokeball-loader::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 16px;
    height: 16px;
    background: white;
    border-radius: 50%;
    border: 4px solid #222;
}

@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

div[data-baseweb="select"] > div {
    background-color: #1a1a3a !important;
    border: 2px solid #3a3a6a !important;
    border-radius: 12px !important;
    color: #f0f0f0 !important;
    transition: border-color 0.3s;
}

div[data-baseweb="select"] > div:hover {
    border-color: #f5c518 !important;
}

div[data-baseweb="select"] * {
    color: #f0f0f0 !important;
    background-color: #1a1a3a !important;
}

.stSelectbox label {
    font-family: 'Press Start 2P', cursive !important;
    font-size: 9px !important;
    color: #8888aa !important;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #e63946 0%, #c1121f 50%, #f5c518 100%);
    background-size: 200% 200%;
    color: white;
    font-family: 'Press Start 2P', cursive;
    font-size: 10px;
    border: none;
    border-radius: 50px;
    padding: 16px 32px;
    cursor: pointer;
    letter-spacing: 2px;
    transition: all 0.3s ease;
    animation: gradientShift 3s ease infinite;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 30px rgba(245,197,24,0.5), 0 0 60px rgba(230,57,70,0.3);
}

.stButton > button:active {
    transform: scale(0.98);
}

.result-title {
    font-family: 'Press Start 2P', cursive;
    font-size: 11px;
    color: #8888aa;
    text-align: center;
    letter-spacing: 2px;
    margin: 30px 0 20px;
    padding: 10px;
    border-top: 1px solid #2a2a4a;
    border-bottom: 1px solid #2a2a4a;
}

.pokemon-card {
    background: linear-gradient(145deg, #1a1a3a, #12122a);
    border: 1px solid #2a2a5a;
    border-radius: 20px;
    padding: 20px;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 20px;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.pokemon-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #e63946, #f5c518, #4cc9f0);
    opacity: 0;
    transition: opacity 0.3s;
}

.pokemon-card:hover::before {
    opacity: 1;
}

.pokemon-card:hover {
    transform: translateX(8px);
    border-color: #f5c518;
    box-shadow: 0 8px 32px rgba(245,197,24,0.15), -4px 0 0 #f5c518;
}

.rank-badge {
    font-family: 'Press Start 2P', cursive;
    font-size: 18px;
    color: #2a2a5a;
    min-width: 40px;
    text-align: center;
}

.pokemon-info {
    flex: 1;
}

.pokemon-name {
    font-family: 'Press Start 2P', cursive;
    font-size: 11px;
    color: #f5c518;
    margin-bottom: 10px;
    letter-spacing: 1px;
}

.score-bar-bg {
    background: #0d0d1a;
    border-radius: 50px;
    height: 8px;
    width: 100%;
    overflow: hidden;
    margin-bottom: 6px;
}

.score-bar-fill {
    height: 100%;
    border-radius: 50px;
    background: linear-gradient(90deg, #e63946, #f5c518);
    transition: width 1s ease;
}

.score-text {
    font-size: 12px;
    color: #8888aa;
    font-weight: 700;
}

.no-image-box {
    width: 90px;
    height: 90px;
    background: #0d0d1a;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    border: 1px dashed #2a2a5a;
}

footer {visibility: hidden;}
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

df = pickle.load(open('pokemon_df.pkl', 'rb'))
similar = pickle.load(open('similarity.pkl', 'rb'))

image_folder = "images-2"

st.markdown("""
<div class="hero">
    <div class="pokeball-loader"></div>
    <div class="hero-title">⚡ POKEMON FINDER</div>
    <p class="hero-sub">Discover Pokemon similar to your favourite</p>
</div>
""", unsafe_allow_html=True)

col_l, col_m, col_r = st.columns([1, 2, 1])
with col_m:
    pokemon_list = sorted(df['Name'].unique())
    selected = st.selectbox("Choose your Pokemon", pokemon_list)
    btn = st.button("Find Similar Pokemon ⚡")

if btn:
    idx = df[df['Name'] == selected].index[0]
    rc = sorted(
        list(enumerate(similar[idx])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    st.markdown(f'<div class="result-title">— similar to {selected.upper()} —</div>', unsafe_allow_html=True)

    for rank, i in enumerate(rc, 1):
        pokemon_name = df.iloc[i[0]]['Name']
        score = i[1]
        score_pct = int(score * 100)

        image_name = pokemon_name.lower()
        if "mega" in image_name:
            image_name = image_name.split("mega")[0].strip()
        image_name = image_name.replace(" ", "-").replace(".", "").replace("'", "")
        image_path = os.path.join(image_folder, f"{image_name}.png")

        col1, col2 = st.columns([1, 4])
        with col1:
            if os.path.exists(image_path):
                st.image(image_path, width=100)
            else:
                st.markdown('<div class="no-image-box">?</div>', unsafe_allow_html=True)

        with col2:
            rank_symbols = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]
            st.markdown(f"""
                <div class="pokemon-card">
                    <div class="rank-badge">{rank_symbols[rank-1]}</div>
                    <div class="pokemon-info">
                        <div class="pokemon-name">{pokemon_name.upper()}</div>
                        <div class="score-bar-bg">
                            <div class="score-bar-fill" style="width:{score_pct}%"></div>
                        </div>
                        <div class="score-text">Match score: {score_pct}%</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            