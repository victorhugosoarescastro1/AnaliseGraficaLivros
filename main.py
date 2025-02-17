import streamlit as st
import pandas as pd
import plotly as pt

st.set_page_config(layout="wide")

df_reviews = pd.read_csv ('dados/customer reviews.csv')
df_top100_livros  = pd.read_csv ("dados/Top-100 Trending Books.csv")

price_max = df_top100_livros ["Book Price"].max()
price_min = df_top100_livros ["Book Price"].min()

max_price = st.sidebar.slider ("Price range", price_min, price_max, price_min)
df_books = df_top100_livros[df_top100_livros["Book Price"] <= max_price]

df_books