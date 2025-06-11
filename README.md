# bank-app-review-analysis
#  Bank App Review Analysis – Omega Consultancy Project

This project simulates a Data Analyst role at **Omega Consultancy**, tasked with providing actionable insights to Ethiopian banks based on Google Play Store reviews. It involves **data scraping**, **sentiment and thematic NLP analysis**, **database management**, and **visual analytics** for three banks: **Commercial Bank of Ethiopia (CBE)**, **Bank of Abyssinia (BOA)**, and **Dashen Bank**.

---

## 🧩 Project Overview

| Task | Description |
|------|-------------|
| **Task 1** | Web scraping of user reviews from Google Play Store |
| **Task 2** | Sentiment analysis and thematic classification (Amharic + English) |
| **Task 3** | Structured storage of processed data into a PostgreSQL database |
| **Task 4** | Deriving insights, visualizing patterns, and generating a report |

---

## 📁 Directory Structure

bank-app-review-analysis/
├── data/
├── outputs/
│ ├── plots/
│ └── sentiment_output.csv
├── scripts/
│ ├── scrape_reviews.py
│ ├── sentiment_thematic_analysis.py
│ ├── database_insert.py
│ └── analyze_insights.py
├── notebooks/
├── README.md
└── requirements.txt


## 🛠️ Technologies Used

- **Python (Pandas, Seaborn, Matplotlib, TextBlob, langdetect, WordCloud)**
- **BeautifulSoup + Requests** (for scraping)
- **Transformers (DistilBERT)** for robust sentiment analysis
- **PostgreSQL + psycopg2** for data storage
- **Jupyter Notebooks** for prototyping
- **Git/GitHub** for version control

---

## ✅ Task Details

### 📌 Task 1: Scraping Google Play Reviews

- Scraped reviews for CBE, BOA, and Dashen Bank apps using `requests` and `BeautifulSoup`.
- Collected:
  - Review text
  - Star rating
  - Timestamp
  - App name

---

### 📌 Task 2: Sentiment & Thematic Analysis

- **Sentiment classification** using:
  - `TextBlob` (English)
  - `DistilBERT` for better accuracy across both languages
- **Hybrid language handling**:
  - Detected Amharic reviews using `langdetect`
  - Ensured support for bilingual sentiment processing
- **Thematic classification** via keyword mapping and TF-IDF:
  - Themes include: *Login Issues*, *Customer Service*, *Network Problems*, *App Performance*, etc.
- Output saved to `outputs/sentiment_output.csv`

---

### 📌 Task 3: PostgreSQL Database Storage

- Created a PostgreSQL DB named `bank_reviews`
- Tables:
  - `Banks`: bank metadata
  - `Reviews`: processed review data + sentiment + themes
- Inserted over 1,000 cleaned and enriched records using `psycopg2`

---

### 📌 Task 4: Insight Extraction & Reporting

- Generated visualizations:
  - 📊 Sentiment distribution per bank
  - 📉 Rating boxplots
  - ☁️ Word cloud of English reviews
- Identified:
  - Top **drivers** (positive themes)
  - Top **pain points** (negative themes)
- Final 4-page report summarizes key insights and actionable recommendations

---

## 📷 Sample Visuals

- `outputs/plots/sentiment_distribution.png`
- `outputs/plots/rating_boxplot.png`
- `outputs/plots/wordcloud.png`

---

## 📌 How to Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt


## Run scripts sequentially:
python scripts/scrape_reviews.py
python scripts/sentiment_thematic_analysis.py
python scripts/database_insert.py
python scripts/analyze_insights.py
