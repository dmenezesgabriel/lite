import micropip
import streamlit as st

code = """
import micropip

await micropip.install('snowballstemmer');

import snowballstemmer

stemmer = snowballstemmer.stemmer('english')

st.write(stemmer.stemWords('go goes going gone'.split()))
"""

st.code(code, language="python")

with st.expander("Show output"):
    await micropip.install("snowballstemmer")

    import snowballstemmer

    stemmer = snowballstemmer.stemmer("english")

    st.write(stemmer.stemWords("go goes going gone".split()))
