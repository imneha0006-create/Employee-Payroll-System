# Student Feedback Analyzer

A Python console application that processes, validates, analyzes, and visualizes student feedback data from a CSV file using `pandas` and `matplotlib`.

## Features

- **CSV Data Validation:** Reads `feedback.csv`, checks for missing files or required columns (`StudentID`, `Rating`, `Comment`), and validates that ratings are whole numbers between `1` and `5`. Skips invalid entries with descriptive row-level warnings.
- **Summary & Word Frequency Analysis:**
  - Calculates total valid feedback count and average rating.
  - Displays the distribution of ratings from `5` down to `1`.
  - Extracts and ranks the top 3 most frequently used words in comments (filtering out common stop words and breaking ties alphabetically).
- **Sentiment Analysis & Visualization:**
  - Categorizes feedback into **Positive** ($\ge 4$), **Neutral** ($= 3$), and **Negative** ($\le 2$) with percentage breakdowns.
  - Generates a color-coded bar chart displaying the sentiment distribution using `matplotlib`.

## Prerequisites

Ensure you have Python 3 installed along with the required libraries:

```bash
pip install pandas matplotlib
```

## Project Structure

```text
├── project.py       # Main Python script containing the analyzer logic and CLI menu
├── feedback.csv     # Input dataset containing StudentID, Rating, and Comment
└── README.md        # Project documentation
```

## Setup & Usage

1. Ensure `feedback.csv` is located in the same directory as `project.py`. Example format:
   ```csv
   StudentID,Rating,Comment
   S1,5,Great teaching and clear notes
   S2,4,Clear explanations and good examples
   S3,2,Too fast and notes unclear
   S4,5,Great examples
   S5,3,Good but too fast
   S6,4,Great notes
   ```

2. Run the application from your terminal:
   ```bash
   python project.py
   ```

3. Choose an option from the interactive console menu:
   - Enter `1` (or `Summary and top 3 words`) to view rating statistics and top keywords.
   - Enter `2` (or `Sentiment`) to view sentiment percentages and render the bar chart.

## Test Cases Covered

| Test Case | Scenario | Expected Behavior |
| :--- | :--- | :--- |
| **Test Case 1** | Normal Input (6 valid rows) | Outputs valid count (`6`), average (`3.83`), rating breakdown, and top 3 words (`great (3), notes (3), clear (2)`). |
| **Test Case 2** | Boundary / Minimum Input (1 row) | Outputs valid count (`1`), average (`5.00`), rating breakdown, and top word (`great (1)`). |
| **Test Case 3** | Invalid Input (out-of-range or non-numeric ratings) | Logs row-specific warnings (`Row 7 skipped...`, `Row 8 skipped...`) and computes metrics using only valid rows. |
| **Test Case 4** | Sentiment Analysis | Outputs Positive (`66.67%`), Neutral (`16.67%`), Negative (`16.67%`), and displays a bar chart. |