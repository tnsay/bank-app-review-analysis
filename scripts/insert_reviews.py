import pandas as pd
import psycopg2
from psycopg2.extras import execute_values, Json
import os


# Load data
csv_path = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'sentiment_output.csv')
df = pd.read_csv(os.path.abspath(csv_path))

#df = pd.read_csv('../outputs/sentiment_output.csv')

# Clean list strings for 'themes'
df['themes'] = df['themes'].apply(eval)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="bank_reviews",
    user="postgres",            
    password="admina",   
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Step 1: Insert unique banks
banks = df['bank'].unique()
bank_id_map = {}

for bank in banks:
    cursor.execute("INSERT INTO banks (bank_name) VALUES (%s) ON CONFLICT (bank_name) DO NOTHING RETURNING bank_id;", (bank,))
    result = cursor.fetchone()
    if result:
        bank_id_map[bank] = result[0]
    else:
        cursor.execute("SELECT bank_id FROM banks WHERE bank_name = %s;", (bank,))
        bank_id_map[bank] = cursor.fetchone()[0]

# Step 2: Prepare review data
review_data = [
    (
        bank_id_map[row['bank']],
        row['review'],
        row['sentiment'],
        row['sentiment_score'] if pd.notnull(row['sentiment_score']) else None,
        row['bert_sentiment'],
        row['bert_score'],
        row['rating'],
        row['themes']
    )
    for _, row in df.iterrows()
]

# Step 3: Insert reviews using execute_values (bulk insert)
insert_query = """
    INSERT INTO reviews (
        bank_id, review, sentiment, sentiment_score,
        bert_sentiment, bert_score, rating, themes
    )
    VALUES %s;
"""
execute_values(cursor, insert_query, review_data)

# Commit and close
conn.commit()
cursor.close()
conn.close()

print(f"✅ Successfully inserted {len(review_data)} reviews.")
