import streamlit as st
import os


with open(f".{os.sep}streamlit_readme.md" ,'r', encoding='utf-8') as readme:
    txt = readme.read()
st.markdown(txt)

