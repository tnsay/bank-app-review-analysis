import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import ast

df = pd.read_csv('outputs/sentiment_output.csv')
df['themes'] = df['themes'].apply(lambda x: ast.literal_eval(x))  # Convert stringified lists


# Explode themes to count per bank
theme_df = df.explode('themes')
theme_counts = theme_df.groupby(['bank', 'themes', 'sentiment']).size().reset_index(name='count')

# Example: Top positive themes per bank (drivers)
drivers = theme_counts[theme_counts['sentiment'] == 'Positive'].groupby(['bank', 'themes'])['count'].sum().reset_index()
drivers = drivers.sort_values(['bank', 'count'], ascending=[True, False]).groupby('bank').head(2)

# Example: Top negative themes per bank (pain points)
pain_points = theme_counts[theme_counts['sentiment'] == 'Negative'].groupby(['bank', 'themes'])['count'].sum().reset_index()
pain_points = pain_points.sort_values(['bank', 'count'], ascending=[True, False]).groupby('bank').head(2)


sns.countplot(data=df, x='bank', hue='sentiment')
plt.title("Sentiment Distribution by Bank")
plt.savefig("outputs/plots/sentiment_distribution.png")
plt.clf()

#rating Distribution
sns.boxplot(data=df, x='bank', y='rating')
plt.title("Rating Distribution by Bank")
plt.savefig("outputs/plots/rating_boxplot.png")
plt.clf()


from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0  # For consistent results

def safe_detect_lang(text):
    try:
        if not isinstance(text, str) or not text.strip():
            return False  # Treat as not Amharic by default
        return detect(text) == 'am'
    except:
        return False

df['is_amharic'] = df['review'].apply(safe_detect_lang)


from textblob import TextBlob
#english_reviews = df[~df['is_amharic']]  --later add lang specific

english_reviews = df[~df['is_amharic']]
english_reviews['review'] = english_reviews['review'].fillna('').astype(str)
text = " ".join(str(r) for r in english_reviews['review'])

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Keyword Cloud of English Reviews")
plt.savefig("outputs/plots/wordcloud.png")
plt.clf()


#WordCloud by Sentiment
# Only for English reviews
from textblob import TextBlob
english_reviews = df[~df['is_amharic']]

# Clean review text to ensure no NaNs or non-string types
english_reviews['review'] = english_reviews['review'].fillna('').astype(str)

text = " ".join(str(r) for r in english_reviews['review'].fillna(''))

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Keyword Cloud of English Reviews")
plt.savefig("outputs/plots/wordcloud.png")
plt.clf()


# Save drivers and pain points to CSV
drivers.to_csv('outputs/summary/drivers.csv', index=False)
pain_points.to_csv('outputs/summary/pain_points.csv', index=False)
print("\nTop Drivers per Bank:")
print(drivers)

print("\nTop Pain Points per Bank:")
print(pain_points)

# Bias risk due to more vocal unhappy users.

# Theme classification may miss nuances in Amharic.