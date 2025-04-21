import streamlit as st

st.set_page_config(page_title="Trump’s 2016 Win: Impact on Media", layout="wide")

st.title("Trump’s 2016 Win: Impact on Media")
st.caption("By Marius, Lauren, Gensei, Bernice — April 22, 2025")

# ---------------- INTRODUCTION ----------------
st.header("Introduction")
st.write("""
The 2016 U.S. presidential election marked a turning point in American media and politics, reshaping the media landscape and raising questions about the press’s role in political polarization, the rise of populist discourse, and shifts in news coverage.
""")

# ---------------- RESEARCH QUESTION ----------------
st.header("Research Question")
st.write("""
Did the election of Donald Trump in 2016 have a significant impact on the editorial tone of news headlines in U.S. media, particularly in terms of emotional polarity and thematic evolution?
""")

# ---------------- HYPOTHESES ----------------
st.header("Hypotheses")
st.subheader("Hypothesis 1")
st.write("""
The average tone of news headlines becomes significantly more negative following the election of Donald Trump, reflecting a more conflictual media climate.
""")
st.subheader("Hypothesis 2")
st.write("""
Editorial categories related to politics show more pronounced tonal shifts compared to categories focused on culture or entertainment.
""")

# ---------------- METHODOLOGY ----------------
st.header("Methodology")

st.subheader("A. Data Collection")
st.write("""
We collected news headlines from HuffPost and The Wall Street Journal to represent left- and right-leaning media perspectives.
""")

st.subheader("B. Data Processing")
st.write("""
Standardization of column names, handling of missing values, and date formatting. Selection of a temporal subset centered around the election (e.g., 2015–2017).
""")

st.subheader("C. Sentiment Analysis")
st.write("""
Application of the VADER SentimentIntensityAnalyzer, a tool designed for sentiment analysis of short texts (e.g., headlines). Each headline is assigned a sentiment score ranging from -1 (very negative) to +1 (very positive).
""")

st.subheader("D. Temporal Aggregation and Analysis")
st.write("""
Monthly aggregation of sentiment scores to track global tone evolution. Disaggregation by editorial category (politics, business, society, etc.). Comparison of sentiment before and after the election (temporal break in Jan 2016).
""")

st.subheader("E. Visualization")
st.write("""
Time series plots (line plots, stacked area plots) to illustrate global and sector-specific dynamics. Tracking the evolution of editorial topic proportions over time.
""")

# ---------------- RESULTS ----------------
st.header("Results")

st.subheader("HuffPost Findings")
st.image("images/huffpost1.png")
st.image("images/huffpost2.png")

st.subheader("Wall Street Journal Findings")
st.image("images/wsj1.png")
st.image("images/wsj2.png")

st.subheader("Multiple Media Outlets Findings")
st.image("images/outlets.png")

# ---------------- CONCLUSION ----------------
st.header("Research Limitations")

st.write("""
I. **Source bias:** HuffPost is not representative of the entire U.S. media landscape and maintains a distinct editorial stance. That is why we want to expand our research to other headline news datasets.  
II. **Limitations of sentiment analysis tools:** While VADER is effective for short texts, it may lack nuance in detecting sarcasm, irony, or complex rhetorical strategies.  
III. **Causality vs. correlation:** It is difficult to attribute tonal shifts solely to the election, given the influence of concurrent events (e.g., social movements, international crises).  
IV. **Reduction of linguistic complexity:** Converting headlines into a single numerical sentiment score may obscure subtler stylistic or lexical variations.
""")

# ---------------- END ----------------
st.markdown("---")
st.caption("The End")
