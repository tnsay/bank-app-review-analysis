-- Create the database (run outside psql or skip if already created)
-- CREATE DATABASE bank_reviews;

-- Connect to the database
-- \c bank_reviews

-- Banks table
CREATE TABLE banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name TEXT UNIQUE NOT NULL
);

-- Reviews table
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    bank_id INTEGER REFERENCES banks(bank_id),
    review TEXT,
    sentiment TEXT,
    sentiment_score FLOAT,
    bert_sentiment TEXT,
    bert_score FLOAT,
    rating FLOAT,
    themes TEXT[]
);
