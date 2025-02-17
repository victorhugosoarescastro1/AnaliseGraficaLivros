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
valor_livro = df_book ["price"].iloc[0]
avaliacao_livro = df_book ["rating"].iloc[0]
ano_livro = df_book ["year of publication"].iloc[0]
