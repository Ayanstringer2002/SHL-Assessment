import streamlit as st
from app.recommender import recommend_assessments

st.title("SHL Assessment Recommender")

query = st.text_area("Paste JD or Query here")
max_time = st.slider("Max Duration (mins)", 10, 90, 60)

if st.button("Recommend"):
    results = recommend_assessments(query, max_duration=max_time)
    if results:
        st.write("### Recommendations")
        for r in results:
            st.markdown(f"**[{r['name']}]({r['url']})**")
            st.write(f"Type: {r['type']} | Duration: {r['duration']} mins | Remote: {r['remote']} | Adaptive: {r['adaptive']}")
            st.markdown("---")
    else:
        st.warning("No matching assessments found.")
