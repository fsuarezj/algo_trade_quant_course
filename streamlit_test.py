import streamlit as st
import pandas as pd

st.write("""
         # My first app
         Hellow *world!*
         """)

x = st.slider("Select a number")
st.write("You selected", x)
