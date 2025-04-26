import pandas as pd
import re

def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    return text.lower()

def preprocess():
    df = pd.read_csv("data/yelp_small_train.csv")
    df['cleaned_text'] = df['text'].apply(clean_text)
    df.to_csv("data/yelp_small_train_cleaned.csv", index=False)

if __name__ == "__main__":
    preprocess()
