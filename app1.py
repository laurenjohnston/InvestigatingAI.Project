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
The average tone of news headlines becomes increasingly negative over the course of the 2016 campaign season, reflecting rising political tension and public polarization.
""")
st.subheader("Hypothesis 2")
st.write("""
Editorial categories related to politics exhibit more dramatic tonal shifts during the campaign period compared to non-political categories like culture or entertainment.
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
st.header("🧠 Key Findings")

st.markdown("""
- **Sentiment became more negative over the campaign season**, particularly in late 2015 and mid-2016, supporting Hypothesis 1.
- **HuffPost consistently expressed more negative sentiment** than The Wall Street Journal throughout the campaign timeline.
- **The most dramatic tone shifts occurred in political categories**, validating Hypothesis 2.
- **Wall Street Journal’s tone remained relatively neutral**, though subtle changes were still observed around major campaign moments.
- **Editorial focus shifted over time**, with HuffPost placing more emphasis on socially and politically charged topics as the campaign intensified.
""")

# ---------------- CONCLUSION ----------------
st.header("⚖️ Research Limitations")

st.write("""
I. **Source bias:** HuffPost is not representative of the entire U.S. media landscape and maintains a distinct editorial stance. This is why we aim to expand our analysis to other outlets in future work.  
II. **Limitations of sentiment analysis tools:** While VADER is effective for short texts, it may lack nuance in detecting sarcasm, irony, or complex rhetorical strategies.  
III. **Causality vs. correlation:** It's difficult to attribute tonal shifts solely to the campaign season, given the influence of concurrent events such as international crises and domestic unrest.  
IV. **Reduction of linguistic complexity:** Turning headlines into a single sentiment score may obscure deeper stylistic and rhetorical patterns.
""")

st.markdown("---")
st.caption("Streamlit site created for AI & Society Research Project — Spring 2025")
# ---------------- END ----------------
st.markdown("---")
st.caption("The End")
