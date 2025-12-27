import streamlit as st
import os


with open(f".{os.sep}README.md" ,'r', encoding='utf-8') as readme:
    txt = readme.read()
st.markdown(txt)

