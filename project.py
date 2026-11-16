import os
import re
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt


def analyze_feedback(file_path="feedback.csv"):
    """Reads the CSV file, validates ratings, and returns a clean DataFrame."""
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found.")
        return None

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

    # Clean column names
    df.columns = [col.strip() for col in df.columns]

    required_cols = {"StudentID", "Rating", "Comment"}
    if not required_cols.issubset(set(df.columns)):
        print(f"Error: CSV must contain columns: {required_cols}")
        return None

    valid_rows = []

    # Validate each row (Row index starts from 1 for data rows)
    for idx, row in df.iterrows():
        row_num = idx + 1
        rating_val = row["Rating"]

        try:
            rating_int = int(rating_val)
            if rating_int < 1 or rating_int > 5:
                raise ValueError
        except (ValueError, TypeError):
            print(
                f"Warning: Row {row_num} skipped - rating must be a whole number from 1 to 5."
            )
            continue

        valid_rows.append({
            "StudentID": row["StudentID"],
            "Rating": rating_int,
            "Comment": str(row["Comment"]),
        })

    return pd.DataFrame(valid_rows)


def show_summary_and_top_words(df):
    """Calculates valid feedback count, average rating, rating counts, and top 3 words."""
    if df is None or df.empty:
        print("No valid feedback data available.")
        return

    valid_count = len(df)
    avg_rating = df["Rating"].mean()

    # Count ratings 1 to 5
    counts = {i: 0 for i in range(1, 6)}
    rating_counts = df["Rating"].value_counts().to_dict()
    for r in counts:
        counts[r] = rating_counts.get(r, 0)

    print(f"Valid feedback: {valid_count}")
    print(f"Average rating: {avg_rating:.2f}")

    # Format ratings from 5 down to 1 as specified in test cases
    ratings_str = ", ".join([f"{i} -> {counts[i]}" for i in range(5, 0, -1)])
    print(f"Ratings: {ratings_str}")

    # Word frequency analysis
    all_words = []
    stop_words = {"and", "but", "the", "is", "a", "of", "too"}

    for comment in df["Comment"]:
        words = re.findall(r"\b[a-zA-Z]+\b", comment.lower())
        for word in words:
            if word not in stop_words:
                all_words.append(word)

    word_counts = Counter(all_words)

    # Sort by frequency descending (-x[1]), then alphabetically ascending for ties (x[0])
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

    top_3 = sorted_words[:3]
    top_3_str = ", ".join([f"{word} ({count})" for word, count in top_3])
    print(f"Top 3 words: {top_3_str}")


def show_sentiment(df):
    """Calculates sentiment percentages and displays a bar chart."""
    if df is None or df.empty:
        print("No valid feedback data available.")
        return

    total = len(df)
    positive = len(df[df["Rating"] >= 4])
    neutral = len(df[df["Rating"] == 3])
    negative = len(df[df["Rating"] <= 2])

    pos_pct = (positive / total) * 100 if total > 0 else 0
    neu_pct = (neutral / total) * 100 if total > 0 else 0
    neg_pct = (negative / total) * 100 if total > 0 else 0

    print(f"Positive: {positive} ({pos_pct:.2f}%)")
    print(f"Neutral: {neutral} ({neu_pct:.2f}%)")
    print(f"Negative: {negative} ({neg_pct:.2f}%)")
    print("(bar chart is displayed)")

    # Bar chart visualization
    sentiments = ["Positive", "Neutral", "Negative"]
    counts = [positive, neutral, negative]

    plt.figure(figsize=(6, 4))
    plt.bar(sentiments, counts, color=["#2ecc71", "#f1c40f", "#e74c3c"])
    plt.title("Student Feedback Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.ylim(0, max(counts) + 2 if counts else 5)
    plt.tight_layout()
    plt.show()


def main():
    file_path = "feedback.csv"

    print("--- Student Feedback Analyzer Menu ---")
    print("1. Summary and top 3 words")
    print("2. Sentiment")

    choice = input(
        "Enter menu choice (e.g., 'Summary and top 3 words' or 'Sentiment'): "
    ).strip()

    print("\n--- Output ---")
    
    # Process the CSV file here so warnings appear underneath --- Output ---
    df = analyze_feedback(file_path)
    if df is None:
        return

    if "summary" in choice.lower() or choice == "1":
        show_summary_and_top_words(df)
    elif "sentiment" in choice.lower() or choice == "2":
        show_sentiment(df)
    else:
        show_summary_and_top_words(df)


if __name__ == "__main__":
    main()