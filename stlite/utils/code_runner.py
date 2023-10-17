import streamlit as st
from pyodide.code import eval_code_async


async def execute(code: str):
    try:
        await eval_code_async(code, globals=globals(), locals=globals())
    except Exception as e:
        st.exception(e)
