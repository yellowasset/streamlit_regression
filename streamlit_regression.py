import streamlit as st
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

with open("result.pkl", "rb") as f:
  lr_loaded = pickle.load(f)

x_input = st.sidebar.slider("xの値 ", min_value=0.0, max_value=1.0, value=0.0, step=0.01, format="%.2f")
y_predict = lr_loaded.predict(np.array([[x_input]]))[0,0]

st.write(f"x = {x_input} のとき， yの予測値 = {y_predict:.2f}")