"""
Text preprocessing pipeline.
"""

import re
import string
from typing import List


class TextPreprocessor:
    """Handles text cleaning and tokenization."""

    STOP_WORDS = {{
        "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "do", "does", "did", "will", "would", "shall",
        "should", "may", "might", "can", "could", "must", "and", "but", "or",
        "nor", "not", "so", "yet", "both", "either", "neither", "each",
        "every", "all", "any", "few", "more", "most", "other", "some",
        "such", "no", "only", "own", "same", "than", "too", "very",
        "of", "in", "to", "for", "with", "on", "at", "from", "by",
        "about", "as", "into", "through", "during", "before", "after",
        "above", "below", "between", "this", "that", "these", "those",
        "it", "its", "i", "me", "my", "we", "our", "you", "your",
        "he", "him", "his", "she", "her", "they", "them", "their",
    }}

    def clean(self, text: str) -> str:
        """Clean text by removing special characters and normalizing whitespace."""
        text = text.lower()
        text = re.sub(r"http\S+|www\S+", "", text)
        text = re.sub(r"<[^>]+>", "", text)
        text = re.sub(r"[^a-zA-Z0-9\s.,!?;:-]", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text

    def tokenize(self, text: str) -> List[str]:
        """Tokenize text into words."""
        cleaned = self.clean(text)
        tokens = cleaned.split()
        return [t.strip(string.punctuation) for t in tokens if t.strip(string.punctuation)]

    def remove_stopwords(self, tokens: List[str]) -> List[str]:
        """Remove stop words from token list."""
        return [t for t in tokens if t.lower() not in self.STOP_WORDS]

    def get_ngrams(self, tokens: List[str], n: int = 2) -> List[str]:
        """Generate n-grams from token list."""
        return [" ".join(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]
