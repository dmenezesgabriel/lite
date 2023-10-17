import pandas as pd
import streamlit as st
from pyodide.http import open_url

st.set_page_config(page_title="Page1")
st.title("Fetch Data")

code = """
import pandas as pd
from pyodide.http import open_url

df = pd.read_csv(
  open_url(
  "https://raw.githubusercontent.com/vega/vega-datasets/main/data/airports.csv"
  )
)

st.dataframe(df)
"""

st.code(code, language="python")

with st.expander("Show output"):
    df = pd.read_csv(
        open_url(
            "https://raw.githubusercontent.com/vega/vega-datasets/main/data/airports.csv"
        )
    )

    st.dataframe(df)
