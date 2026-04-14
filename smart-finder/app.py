import streamlit as st
from database import EndeeManager

db = EndeeManager()

st.title("🛍️ Smart AI Product Finder")
st.write("Using Endee Vector DB for Semantic Search")

query = st.text_input("What are you looking for today?", "Something for a rainy day")

if st.button("Search"):
    results = db.search(query)
    
    st.subheader("Top Matches:")
    for res in results.get('matches', []):
        with st.container():
            st.write(f"**Product ID:** {res['id']}")
            st.write(f"**Relevance Score:** {res['score']}")
            st.write(f"**Category:** {res['metadata']['category']}")
            st.write("---")
