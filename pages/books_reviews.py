import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df_reviews = pd.read_csv ('dados/customer reviews.csv')
df_top100_livros  = pd.read_csv ("dados/Top-100 Trending Books.csv")

livros = df_top100_livros["book title"].unique()
livro = st.sidebar.selectbox ("Books", livros)

df_book = df_top100_livros[df_top100_livros["book title"] == livro]
df_reviews_filtro = df_reviews[df_reviews["book name"] == livro]

df_book
df_reviews_filtro