# app/utils.py

import json
import re

def clean_text(text: str) -> str:
    """
    Basic text preprocessing: lowercasing, removing special characters.
    """
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.strip()

def load_json(path: str):
    """
    Load and return JSON from a file.
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
