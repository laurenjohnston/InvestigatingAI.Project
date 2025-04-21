import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Trump’s 2016 Win: Media Impact", layout="wide")

# Title
st.title("Trump’s 2016 Win: Impact on Media")
st.caption("By Lauren, Marius, Gensei, Bernice")

# Section: Introduction
st.header("Introduction")
st.write("""
The 2016 U.S. presidential election marked a turning point in American media and politics. 
This project investigates how the tone of media headlines shifted before and after Trump’s election,
with a focus on sentiment and thematic trends in left- and right-leaning outlets.
""")

# Section: Research Question & Hypotheses
st.header("Research Question & Hypotheses")
st.markdown("""
**Research Question:**  
Did the election of Donald Trump in 2016 significantly impact the editorial tone of U.S. media headlines?

**Hypothesis 1:** The average tone of news headlines becomes more negative post-election.  
**Hypothesis 2:** Political editorial categories show more pronounced tonal shifts than cultural or entertainment content.
""")

# Section: Methodology
st.header("Methodology")
st.markdown("""
- **Data Collection:** Headlines from HuffPost (left) & WSJ (right)
- **Processing:** Cleaning, date formatting, filtering to 2015–2017
- **Sentiment Analysis:** VADER model (scores -1 to +1)
- **Aggregation:** Monthly tone by outlet and category
- **Visualization:** Time series & topic breakdowns
""")

# Section: Sentiment Line Chart
st.subheader("Sentiment Over Time")
data = pd.read_csv("data/sentiment_scores.csv")
fig, ax = plt.subplots()
for outlet in data['outlet'].unique():
    subset = data[data['outlet'] == outlet]
    ax.plot(subset['month'], subset['compound_score'], label=outlet)
plt.xticks(rotation=45)
plt.legend()
st.pyplot(fig)

# Section: Findings
st.header("Findings")
st.image("images/huffpost.png", caption="HuffPost Headlines")
st.image("images/wsj.png", caption="Wall Street Journal Headlines")
st.image("images/multiple_outlets.png", caption="Combined Media Tone Trends")

# Section: Conclusion
st.header("Conclusion & Limitations")
st.markdown("""
- **Tone shifted negatively post-election**, especially in political news
- **Limitations:**  
  - Source bias (HuffPost ≠ all left-leaning media)  
  - VADER lacks nuance (e.g., sarcasm)  
  - Correlation ≠ causation  
  - Simplified sentiment scores may overlook linguistic depth
""")

# End
st.markdown("---")
st.caption("Streamlit site created as part of an AI & Society class project.")