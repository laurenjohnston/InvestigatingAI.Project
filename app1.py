import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Media Sentiment & the 2016 Election")

st.title("How the 2016 Election Changed Media Tone")
st.write("Analyzing HuffPost & Wall Street Journal headlines using AI-powered sentiment analysis.")

# Load data
data = pd.read_csv("data/sentiment_scores.csv")  # Make sure this matches your file name!

# Line Chart
st.subheader("Sentiment Over Time by Outlet")
fig, ax = plt.subplots()
for outlet in data['outlet'].unique():
    subset = data[data['outlet'] == outlet]
    ax.plot(subset['month'], subset['compound_score'], label=outlet)
plt.xticks(rotation=45)
plt.legend()
st.pyplot(fig)

st.subheader("Key Takeaways")
st.markdown("""
- Sentiment shifted significantly post-election
- Tone varied by outlet (left vs. right)
- Political events influenced media framing
""")

