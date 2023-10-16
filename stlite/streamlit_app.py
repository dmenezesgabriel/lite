import sys

import streamlit as st
from streamlit import runtime
from streamlit_ace import st_ace
from utils.code_runner import execute
from utils.shorten_urls import get_code_params, set_code_params

streamlit_version = st.__version__
python_version = sys.version

st.set_page_config(page_title="Stlite - Playground")
st.title("Playground")

if "python" not in st.session_state:
    get_code_params()

with st.expander("Code", expanded=True):
    content = st_ace(
        value=st.session_state["python"],
        key="python",
        language="python",
        min_lines=20,
    )

execute(st.session_state["python"])
set_code_params()
