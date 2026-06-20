# 📊 Task 6: Sentiment Analysis (AI + Data Science)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python Version"/>
  <img src="https://img.shields.io/badge/NLTK-NLP-green.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="NLTK NLP"/>
  <img src="https://img.shields.io/badge/Data_Science-Pandas-orange.svg?style=for-the-badge" alt="Data Science"/>
  <img src="https://img.shields.io/badge/Status-Completed-success.svg?style=for-the-badge" alt="Project Status"/>
</p>

An end-to-end Python-based Natural Language Processing (NLP) application designed to extract textual context, categorize consumer emotions, and compile interactive statistical dashboards. This project fulfills the requirements for **Task 6** of the **Horizon TechX Internship Portfolio**.

---

## 🎯 Project Deliverables Tracker

- [x] **Data Processing:** Structuring social streams, user reviews, and news wire metrics.
- [x] **Sentiment Classification:** Mapping compound metric coefficients via VADER lexicon.
- [x] **Trend Interpretation:** Exporting macro public opinion insights over custom dimensions.
- [x] **Automated Reporting:** Creating stand-alone `.png` analytical visualization matrices.

---

## 🛠️ Tech Stack & Architecture

<details>
<summary><b>📐 Click to Expand Technical Stack Architecture</b></summary>
<br>

* **Core Engine:** Python 3.8+
* **Data Wrangling:** `pandas` (Matrix operations & tabular cleaning)
* **Natural Language Processing:** `nltk.sentiment.vader` (Valence-aware rule engines)
* **Visualization Matrix:** `matplotlib` & `seaborn` (Statistical visualization)

</details>

---

## 💻 Implementation & Setup

### 1️⃣ Installation
Ensure you have the core scientific dependencies installed in your active environment:

```bash
pip install pandas nltk matplotlib seaborn
2️⃣ Execution
Trigger the analytics pipeline from your project directory root:

Bash
python sentiment_analysis.py
🔬 Core Metric ClassificationsThe application processes natural language expressions down to a localized compound range, applying standard mathematical logic layers:$$\text{Compound Score Thresholds} = 
\begin{cases} 
\mathbf{Positive} & \text{Score} \ge 0.05 \\ 
\mathbf{Neutral} & -0.05 < \text{Score} < 0.05 \\ 
\mathbf{Negative} & \text{Score} \le -0.05 
\end{cases}$$
📈 Sample Dashboard Log Output
--- Starting Sentiment Analysis Task ---

[1/4] Loaded dataset containing 8 samples.
[2/4] Processing NLP analysis via VADER Sentiment Analyzer...

[3/4] Analysis complete! Detailed Preview of Results:
------------------------------------------------------------------------------------------
          Source                                              Text  Compound_Score Sentiment
0   Social Media  I absolutely love this new update! The UI is ...          0.8016  Positive
1 Product Review  The product quality is decent, but delivery to...          0.2107  Positive
2           News  Stock prices plummet amid market uncertainty a...         -0.4404  Negative
3 Product Review  Horrible experience. The app keeps crashing ev...         -0.5411  Negative
...
------------------------------------------------------------------------------------------

Public Opinion Summary:
 - Positive: 3 items (37.5%)
 - Negative: 3 items (37.5%)
 - Neutral: 2 items (25.0%)

[4/4] Rendering visualization dashboards...
[INFO] Analytical charts successfully saved to 'sentiment_analysis_report.png'