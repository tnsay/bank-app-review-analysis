from google_play_scraper import reviews
import pandas as pd

def scrape_reviews(app_id, bank_name, max_reviews=450):
    all_reviews = []
    count = 0
    while len(all_reviews) < max_reviews:
        rvs, _ = reviews(app_id, count=count, lang='en', country='us')
        if not rvs:
            break
        for r in rvs:
            all_reviews.append({
                "review": r['content'],
                "rating": r['score'],
                "date": r['at'].strftime('%Y-%m-%d'),
                "bank": bank_name,
                "source": "Google Play"
            })
        count += len(rvs)
    return pd.DataFrame(all_reviews[:max_reviews])

if __name__ == "__main__":
    banks = {
        "Commercial Bank of Ethiopia Mobile": "com.combanketh.mobilebanking",
        "Bank of Abyssinia Mobile": "com.boa.boaMobileBanking",
        "Dashen Bank Mobile": "com.dashen.dashensuperapp"
    }

    df_list = []
    for bank_name, app_id in banks.items():
        df = scrape_reviews(app_id, bank_name)
        df_list.append(df)

    full_df = pd.concat(df_list)
    full_df.to_csv("raw_reviews.csv", index=False)
