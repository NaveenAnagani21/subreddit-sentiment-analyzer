from analyze import df
import streamlit as st

center_css = """
<style>
    .centered-container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .centered-dataframe {
        width: 100%;
        max-width: 800px;
    }
</style>
"""

st.markdown(center_css, unsafe_allow_html=True)
st.title('reddit+mood :rainbow:')
st.dataframe(df)
st.markdown('</div>', unsafe_allow_html=True)



