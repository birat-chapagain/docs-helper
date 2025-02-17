import json
import os
import re

RAW_PATH = "../../data/raw/react_docs.json"
PROCESSED_DIR = "../../data/processed/"
os.makedirs(PROCESSED_DIR, exist_ok=True)
PROCESSED_PATH = os.path.join(PROCESSED_DIR, "react_cleaned.json")


def clean_text(text):
    """Removes unwanted characters, extra spaces, and special symbols."""
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^A-Za-z0-9.,!?;:\'\"()\s/-]', '', text)  # Keep only useful characters
    return text.strip()


def process_data():
    """Loads raw JSON, cleans text, and saves processed data."""
    with open(RAW_PATH, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    processed_data = []
    for entry in raw_data:
        cleaned_text = clean_text(entry["text"])
        processed_data.append({"url": entry["url"], "text": cleaned_text})

    with open(PROCESSED_PATH, "w", encoding="utf-8") as f:
        json.dump(processed_data, f, indent=4)

    print(f"✅ Processing complete. Cleaned data saved to {PROCESSED_PATH}")


if __name__ == "__main__":
    process_data()
