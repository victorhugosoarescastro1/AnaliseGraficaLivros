import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv ('dados/customer reviews.csv')
df_top100_livros  = pd.read_csv ("dados/Top-100 Trending Books.csv")

price_max = df_top100_livros["book price"].max()
price_min = df_top100_livros["book price"].min()

max_price = st.sidebar.slider ("Price range", price_min, price_max, price_min)
df_books = df_top100_livros[df_top100_livros["book price"] <= max_price]

df_books

grafico_barras = px.bar (df_books["year of publication"].value_counts())
grafico_histograma = px.histogram(df_books["book price"])

col1, col2 = st.columns(2)

col1.plotly_chart (grafico_barras)
col2.plotly_chart (grafico_histograma)

