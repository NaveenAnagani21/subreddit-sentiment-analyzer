from analyze import df, df_score
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
st.title("reddit+mood :rainbow:")
st.dataframe(
    df_score,
    column_order=("subreddit", "mood"),
    width=None,
    column_config={
        "subreddit": st.column_config.TextColumn(
            "subreddit",
        ),
        "mood": st.column_config.ProgressColumn(
            "mood",
            format="%.2f",
            min_value=-1,
            max_value=1,
        ),
    },
)
st.markdown("</div>", unsafe_allow_html=True)
