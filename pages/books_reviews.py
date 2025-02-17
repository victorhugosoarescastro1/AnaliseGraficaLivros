import streamlit as st
import pandas as pd

df_reviews = pd.read_csv ('dados/customer reviews.csv')
df_top100_livros  = pd.read_csv ("dados/Top-100 Trending Books.csv")

livros = df_top100_livros["book title"].unique()
livro = st.sidebar.selectbox ("Books", livros)

