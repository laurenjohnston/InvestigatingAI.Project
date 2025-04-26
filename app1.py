import streamlit as st

st.set_page_config(page_title="The 2016 Campaign Season’s Impact on Media", layout="wide")
st.image("images/banner.png", use_container_width=True)




st.title("The 2016 Campaign Season’s Impact on Media")
st.caption("By Marius, Lauren, Gensei, Bernice — April 22, 2025")

# ---------------- INTRODUCTION ----------------
st.header("📌 Introduction")
st.write("""
The 2016 U.S. presidential campaign season marked a turning point in American media and politics. 
It reshaped the media landscape and raised questions about the press’s role in political polarization, the rise of populist discourse, and evolving editorial tone during one of the most contentious election cycles in modern history.
""")

# ---------------- RESEARCH QUESTION ----------------
st.header("❓ Research Question")
st.write("""
How did the tone of U.S. media headlines evolve during the final two years of the Obama administration and throughout the 2016 presidential campaign, culminating in Donald Trump's inauguration?
""")

# ---------------- HYPOTHESES ----------------
st.header("🧠 Hypotheses")
st.subheader("Hypothesis 1")
st.write("""
The average tone of news headlines becomes significantly more negative during the 2016 election, reflecting a more conflictual media climate.
""")
st.subheader("Hypothesis 2")
st.write("""
Editorial categories related to politics show more pronounced tonal shifts compared to categories focused on culture or entertainment.
""")

# ---------------- METHODOLOGY ----------------
st.header("🧪 Methodology")

st.subheader("A. Data Collection")
st.write("""
We collected news headlines from HuffPost and The Wall Street Journal between January 20, 2015 and January 20, 2017 to capture the final phase of the Obama presidency and the entire 2016 campaign cycle.
""")

st.subheader("B. Data Processing")
st.write("""
We standardized column names, handled missing values, and formatted dates to create a clean dataset. Our analysis focuses on the two-year span leading up to Trump’s inauguration.
""")

st.subheader("C. Sentiment Analysis")
st.write("""
We used the VADER SentimentIntensityAnalyzer, a tool designed for short texts like headlines. VADER assigns each headline a score from -1 (very negative) to +1 (very positive).
""")

st.subheader("D. Temporal Aggregation and Analysis")
st.write("""
We aggregated sentiment scores by month to identify evolving trends over time. We also disaggregated data by editorial category — such as politics, business, and society — to observe tone shifts by topic.
""")

st.subheader("E. Visualization")
st.write("""
Time series and stacked area plots were created to visualize sentiment evolution and editorial focus during the campaign season.
""")
st.header("🤖 AI Tools in Our Research")

st.markdown("""
- **VADER**  
  Used for sentiment analysis to assign polarity scores to headlines (–1 to +1) based on emotional tone

- **Google Colab**  
  Enabled scalable implementation of VADER for data processing and analysis in a cloud-based environment

- **Streamlit**  
  Used to build an interactive web app for data visualization and public presentation of findings
""")
# ---------------- RESULTS ----------------
st.header("📊 Results")

st.subheader("HuffPost Findings")
st.image("images/huffpost1.png")
st.image("images/huffpost2.png")

st.subheader("Wall Street Journal Findings")
st.image("images/wsj1.png")
st.image("images/wsj2.png")

st.subheader("Multiple Media Outlets Findings")
st.image("images/outlets.png")

# ---------------- KEY FINDINGS ----------------
# ---------------- KEY FINDINGS ----------------
st.header("📊 Key Findings")

st.subheader("1. Overall Sentiment Is Negative")
st.write("""
Across all sources analyzed, the average sentiment score remained slightly negative throughout the campaign period. 
There was no dramatic swing in tone before or after the 2016 election — the tone stayed consistently below neutral, 
with small fluctuations. This supports the idea of a persistent media negativity bias.
""")

st.subheader("2. No Significant Shift in Tone or Content Volume")
st.write("""
We found no substantial tonal change tied directly to Trump’s election win, nor did we see a spike or drop in 
any specific category of article coverage. The proportion of article topics remained relatively steady, 
challenging our assumption that the media landscape would shift drastically post-election.
""")

# ---------------- LIMITATIONS ----------------
st.header("⚠️ Limitations")

st.markdown("""
**I. Limited Timeline**  
The two-year dataset restricts our ability to observe long-term sentiment trends or post-election evolution.

**II. Limited Sources**  
We analyzed a small number of media outlets, which may introduce bias and does not reflect the full diversity of U.S. media.

**III. Sentiment Tool Constraints**  
VADER captures polarity but misses nuance such as sarcasm, rhetorical framing, or subjectivity in topic selection.
""")

# ---------------- FUTURE WORK ----------------
st.header("🔭 Future Work")

st.markdown("""
**I. Expand Timeline**  
Analyze headlines over a 10-year span to capture broader political trends and tone shifts across administrations.

**II. Diversify Dataset Sources**  
Include additional media outlets across the ideological spectrum for a more balanced and holistic view.

**III. Deepen Analysis**  
Incorporate content-based sentiment analysis to examine **what** topics were covered — not just **how** they were framed.
""")

st.header("🔭 References")

st.markdown("""
**Kaggle. (2023). Wall Street Journal Articles, 2014–2020. Retrieved from https://www.kaggle.com

**Kaggle. (2022). News Category Dataset. Retrieved from https://www.kaggle.com/datasets/rmisra/news-category-dataset

""")

st.markdown("---")
st.caption("Streamlit site created for AI & Society Research Project — Spring 2025")
# ---------------- END ----------------
st.markdown("---")
st.caption("The End.")
