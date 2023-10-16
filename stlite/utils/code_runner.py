import streamlit as st
from pyodide.code import CodeRunner


def execute(code: str):
    try:
        code_runner = CodeRunner(code)
        code_runner.compile()
        code_runner.run(globals=globals(), locals=globals())
    except Exception as e:
        st.exception(e)
