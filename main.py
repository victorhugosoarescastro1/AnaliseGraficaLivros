import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df_reviews = pd.read_csv ("Documents\archive\ costumer reviews.csv")
df_top100_livros  = pd.read_csv ("Documents\archive\ Top-100 Trending Books.csv")