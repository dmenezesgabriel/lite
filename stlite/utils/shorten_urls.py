import urllib.parse

import streamlit as st


def get_code_params():
    if st.experimental_get_query_params().get("q"):
        st.session_state["python"] = urllib.parse.unquote(
            st.experimental_get_query_params().get("q")[0]
        )
    else:
        st.session_state["python"] = ""


def set_code_params():
    if st.session_state["python"] == "":
        return
    st.experimental_set_query_params(
        q=urllib.parse.quote(st.session_state["python"])
    )
