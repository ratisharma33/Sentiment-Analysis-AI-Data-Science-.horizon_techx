
# Task 6: Sentiment Analysis (AI + Data Science)

An end-to-end Python-based Natural Language Processing (NLP) application designed to analyze text datasets (social media posts, product reviews, and news headlines), classify overall public sentiment, and visualize prevailing opinion trends using statistical data dashboards.

This project fulfills the requirements for **Task 6** of the **Horizon TechX Internship Portfolio**.

---

## 🚀 Key Features

* **Multi-Domain Analysis:** Capable of processing varying text structures including informal social media streams (with emoji support), structured customer reviews, and formal news headlines.
* **VADER Sentiment Integration:** Utilizes the NLTK `vader_lexicon` analyzer, optimized specifically for handling valences, nuances, and context-dependent slang in short text datasets.
* **Automated Classification:** Computes mathematical polarity metrics (Compound Scores between -1.0 and +1.0) to explicitly classify data into **Positive**, **Neutral**, or **Negative** labels.
* **Visual Data Dashboard:** Automatically generates and exports a high-resolution, side-by-side analytical chart (`sentiment_analysis_report.png`) mapping overall distribution and platform-specific trends.

---

## 🛠️ Project Structure

```text
├── sentiment_analysis.py       # Main Python source code file
├── sentiment_analysis_report.png # Saved high-resolution data visualization output
└── README.md                   # Project documentation