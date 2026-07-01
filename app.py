# import streamlit as st
# import pandas as pd
# from sklearn.metrics.pairwise import cosine_similarity
# import os
# import pickle

# df=pickle.load(open('pokemon_df.pkl','rb'))
# similar = pickle.load(open('similarity.pkl', 'rb'))

# image_folder = "images-2"  
# # df = pd.read_csv("PokemonData.csv")
# # similar = cosine_similarity(scaled_features)






# pokemon_list = sorted(df['Name'].unique())

# st.title('Pokemon Recommendation System')
# selected = st.selectbox("Choose a Pokémon",pokemon_list)





# if st.button('Recommend'):
   

#         idx = df[df['Name'] == selected].index[0]

#         rc = sorted(
#         list(enumerate(similar[idx])),
#         key=lambda x: x[1],
#         reverse=True
#         )[1:6]

#         for i in rc:

#             pokemon_name = df.iloc[i[0]]['Name']
#             score = i[1]
#             st.write(f"{pokemon_name} — similarity: {score:.3f}")

#             image_name = pokemon_name.lower()
#         if "mega" in image_name:
#             image_name = image_name.split("mega")[0].strip()
#         image_path = os.path.join(image_folder, f"{image_name}.png")
 
#         col1, col2 = st.columns([1, 3])
 
#         with col1:
#             if os.path.exists(image_path):
#                 st.image(image_path, width=120)
#             else:
#                 st.write("(no image)")
 
#         with col2:
#             st.write(f"**{pokemon_name.title()}**")
#             st.write(f"Similarity score: {score:.3f}")
 

#             # st.write(f"{pokemon_name} ({i[1]:.3f})")
import os
import pickle
import streamlit as st

st.set_page_config(page_title="Pokemon Recommender", page_icon="🔴")
st.title("Pokemon Recommender ")

df = pickle.load(open('pokemon_df.pkl', 'rb'))
similar = pickle.load(open('similarity.pkl', 'rb'))

image_folder = "images-2"

pokemon_list = sorted(df['Name'].unique())
selected = st.selectbox("Choose a Pokemon", pokemon_list)

if st.button("Recommend"):
    idx = df[df['Name'] == selected].index[0]

    rc = sorted(
        list(enumerate(similar[idx])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    st.subheader(f"Pokemon similar to {selected.title()}:")

    for i in rc:
        pokemon_name = df.iloc[i[0]]['Name']
        score = i[1]

        # clean name to match image filename
        image_name = pokemon_name.lower()
        if "mega" in image_name:
            image_name = image_name.split("mega")[0].strip()
        image_name = image_name.replace(" ", "-")
        image_name = image_name.replace(".", "")
        image_name = image_name.replace("'", "")

        image_path = os.path.join(image_folder, f"{image_name}.png")

        col1, col2 = st.columns([1, 3])

        with col1:
            if os.path.exists(image_path):
                st.image(image_path, width=120)
            else:
                st.write("(no image)")

        with col2:
            st.write(f"**{pokemon_name.title()}**")
            st.write(f"Similarity: {score:.3f}")