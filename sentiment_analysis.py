import os
import matplotlib.pyplot as plt
import nltk
import pandas as pd
import seaborn as sns
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon package (only needed once)
nltk.download("vader_lexicon", quiet=True)


def load_dataset():
    """Simulates loading text data (reviews, social media, news).

    Replace this with pd.read_csv('your_file.csv') in production.
    """
    data = {
        "Review_ID": [1, 2, 3, 4, 5, 6, 7, 8],
        "Source": [
            "Social Media",
            "Product Review",
            "News",
            "Product Review",
            "Social Media",
            "News",
            "Product Review",
            "Social Media",
        ],
        "Text": [
            "I absolutely love this new update! The UI is incredibly smooth and fast. 🔥",
            "The product quality is decent, but delivery took way too long. Average experience.",
            "Stock prices plumet amid market uncertainty and regulatory pressure.",
            "Horrible experience. The app keeps crashing every time I try to log in. Fix it!",
            "Just okay. Nothing spectacular, but gets the job done.",
            "Tech breakthrough: Scientists develop highly efficient quantum chip.",
            "Best purchase I have made this year! Highly recommend it to everyone.",
            "Why is the service so slow today? Pretty frustrating to wait in line for an hour.",
        ],
    }
    return pd.DataFrame(data)


def analyze_sentiment(df):
    """Analyzes text data and classifies it as Positive, Negative, or Neutral."""
    # Initialize the VADER sentiment analyzer
    sia = SentimentIntensityAnalyzer()

    # Calculate compound sentiment scores
    df["Compound_Score"] = df["Text"].apply(
        lambda x: sia.polarity_scores(str(x))["compound"]
    )

    # Classify sentiment based on standard VADER thresholds
    # Positive: compound >= 0.05 | Negative: compound <= -0.05 | Neutral: in between
    def get_sentiment_label(score):
        if score >= 0.05:
            return "Positive"
        elif score <= -0.05:
            return "Negative"
        else:
            return "Neutral"

    df["Sentiment"] = df["Compound_Score"].apply(get_sentiment_label)
    return df


def generate_visualizations(df):
    """Generates charts to visualize sentiment trends and distribution."""
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(12, 5))

    # Chart 1: Sentiment Distribution (Count Plot)
    plt.subplot(1, 2, 1)
    # Using specific colors for clarity: Green for positive, Red for negative, Grey for neutral
    palette = {
        "Positive": "#2ecc71",
        "Neutral": "#95a5a6",
        "Negative": "#e74c3c",
    }
    sns.countplot(
        data=df,
        x="Sentiment",
        hue="Sentiment",
        palette=palette,
        order=["Positive", "Neutral", "Negative"],
        legend=False,
    )
    plt.title("Overall Sentiment Distribution")
    plt.xlabel("Sentiment Class")
    plt.ylabel("Number of Items")

    # Chart 2: Sentiment Breakdowns by Source Platform
    plt.subplot(1, 2, 2)
    sns.countplot(
        data=df,
        x="Source",
        hue="Sentiment",
        palette=palette,
        hue_order=["Positive", "Neutral", "Negative"],
    )
    plt.title("Sentiment Trends Across Platforms")
    plt.xlabel("Data Source")
    plt.ylabel("Count")
    plt.xticks(rotation=15)

    plt.tight_layout()

    # Save the plot for the project submission documentation
    output_image = "sentiment_analysis_report.png"
    plt.savefig(output_image, dpi=300)
    print(f"\n[INFO] Analytical charts successfully saved to '{output_image}'")
    plt.show()


def main():
    print("--- Starting Sentiment Analysis Task ---")

    # 1. Clean and preprocess datasets (Simulated/Loaded)
    df = load_dataset()
    print(f"\n[1/4] Loaded dataset containing {len(df)} samples.")

    # 2. Analyze text data & Classify sentiments
    print("[2/4] Processing NLP analysis via VADER Sentiment Analyzer...")
    processed_df = analyze_sentiment(df)

    # 3. Interpret public opinion and trends
    print("\n[3/4] Analysis complete! Detailed Preview of Results:")
    print("-" * 90)
    print(processed_df[["Source", "Text", "Compound_Score", "Sentiment"]])
    print("-" * 90)

    # Summary metrics calculation
    counts = processed_df["Sentiment"].value_counts()
    print("\nPublic Opinion Summary:")
    for label, count in counts.items():
        percentage = (count / len(processed_df)) * 100
        print(f" - {label}: {count} items ({percentage:.1f}%)")

    # 4. Generate analytical charts
    print("\n[4/4] Rendering visualization dashboards...")
    generate_visualizations(processed_df)


if __name__ == "__main__":
    main()