# PokéLens 🔴⚡

A content-based Pokemon recommendation system built with Python and Streamlit. Enter any Pokemon and instantly discover the 5 most similar ones based on their stats, types, and attributes — powered by cosine similarity and machine learning.

---

## 🚀 Live Demo
> Coming soon via Streamlit Community Cloud

---

## 🧠 How It Works

1. **Data Loading** — Loads the Pokemon dataset with stats like HP, Attack, Defense, Speed, Type1, Type2, and Legendary status
2. **Preprocessing** — Cleans missing values, encodes types using One-Hot Encoding, normalizes features with StandardScaler
3. **Similarity Matrix** — Computes cosine similarity across all Pokemon feature vectors
4. **Recommendation** — Returns the top 5 most similar Pokemon for any selected Pokemon
5. **Streamlit UI** — Displays results interactively with images, match scores, and animated cards

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas & NumPy | Data processing |
| Scikit-learn | StandardScaler + Cosine Similarity |
| Streamlit | Web app UI |
| Pickle | Model serialization |
| Pillow | Image rendering |

---

## 📁 Project Structure

```
PokéLens/
├── app.py               # Streamlit web app
├── pokemon_df.pkl       # Preprocessed Pokemon dataframe
├── similarity.pkl       # Precomputed cosine similarity matrix
├── PokemonData.csv      # Raw dataset
├── images-2/            # Pokemon images (.png)
└── requirements.txt     # Project dependencies
```

---

## ⚙️ Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/khushboo095/Pokemon-Recommendation-app.git
cd Pokemon-Recommendation-app
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

---

## 📊 Dataset

- **Source**: [Kaggle — Pokemon Dataset by Vishal Subbiah](https://www.kaggle.com/datasets/vishalsubbiah/pokemon-images-and-types)
- **Size**: 800 Pokemon with stats, types, and images
- **Features used**: HP, Attack, Defense, Sp. Atk, Sp. Def, Speed, Type1, Type2, Legendary

---

## ✨ Features

- 🔍 Search any Pokemon from a dropdown of 800+
- ⚡ Instant top 5 similar Pokemon recommendations
- 📊 Animated match score progress bar
- 🖼️ Pokemon images displayed alongside results
- 🏅 Medal ranking for each recommendation
- 🎨 Custom dark-themed Pokémon-style UI

---

## 🔮 Future Improvements

- [ ] Deploy on Streamlit Community Cloud
- [ ] Add Pokemon type filter
- [ ] Show stat comparison chart between selected and recommended Pokemon
- [ ] Add generation filter

---

## 👩‍💻 Author

**Khushboo Pandit**
Data Science Student | Brainware University
[LinkedIn](https://www.linkedin.com/in/khushboo095) • [GitHub](https://github.com/khushboo095)

---

## 📄 License

This project is open source and available
