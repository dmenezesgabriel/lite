import sys

import micropip
import streamlit as st

st.set_page_config(page_title="Stlite- Installed Packages")
st.title("Installed Packages")

streamlit_version = st.__version__
python_version = sys.version
python_executable = sys.executable

st.write(f"Streamlit version: {streamlit_version}")
st.write(f"Python version: {python_version}")
st.write(f"Python executable: {python_executable}")

st.divider()

st.write(micropip.list())
