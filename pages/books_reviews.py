import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df_reviews = pd.read_csv ('dados/customer reviews.csv')
df_top100_livros  = pd.read_csv ("dados/Top-100 Trending Books.csv")

livros = df_top100_livros["book title"].unique()
livro = st.sidebar.selectbox ("Books", livros)

df_book = df_top100_livros[df_top100_livros["book title"] == livro]
df_reviews_filtro = df_reviews[df_reviews["book name"] == livro]

titulo_livro = df_book ["book title"].iloc[0]
genero_livro = df_book ["genre"].iloc[0]
valor_livro = f"${df_book ['price'].iloc[0]}"
avaliacao_livro = df_book ["rating"].iloc[0]
ano_livro = df_book ["year of publication"].iloc[0]

st.title(titulo_livro)
st.subheader(genero_livro)

col1, col2, col3 = st.columns(3)

col1.metric ("Preço", valor_livro)
col2.metric ("Avaliação", avaliacao_livro)
col3.metric |("Ano Publicado", ano_livro)

st.divider()

for row in df_reviews_filtro.values:
    message = st.chat_message(f"{row[4]}")
    st.write(f"**{row[2]}**")
    st.write(row[5])