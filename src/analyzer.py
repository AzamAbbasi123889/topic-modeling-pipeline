"""
Text analysis engine.
"""

import re
from typing import Dict, Any, List
from collections import Counter
from .preprocessor import TextPreprocessor


class TextAnalyzer:
    """Analyzes text and extracts features."""

    def __init__(self):
        self.preprocessor = TextPreprocessor()

    def analyze(self, text: str) -> Dict[str, Any]:
        """Full text analysis returning multiple metrics."""
        tokens = self.preprocessor.tokenize(text)
        content_tokens = self.preprocessor.remove_stopwords(tokens)
        sentences = self._split_sentences(text)

        return {{
            "char_count": len(text),
            "word_count": len(tokens),
            "sentence_count": len(sentences),
            "avg_word_length": self._avg_word_length(tokens),
            "avg_sentence_length": len(tokens) / max(len(sentences), 1),
            "vocab_richness": len(set(tokens)) / max(len(tokens), 1),
            "keywords": self._extract_keywords(content_tokens, top_n=10),
            "bigrams": self.preprocessor.get_ngrams(content_tokens, 2)[:5],
            "readability_score": self._readability_score(tokens, sentences),
        }}

    def _split_sentences(self, text: str) -> List[str]:
        """Split text into sentences."""
        sentences = re.split(r"[.!?]+", text)
        return [s.strip() for s in sentences if s.strip()]

    def _avg_word_length(self, tokens: List[str]) -> float:
        if not tokens:
            return 0.0
        return sum(len(t) for t in tokens) / len(tokens)

    def _extract_keywords(self, tokens: List[str], top_n: int = 10) -> List[str]:
        """Extract top keywords by frequency."""
        counter = Counter(tokens)
        return [word for word, _ in counter.most_common(top_n)]

    def _readability_score(self, tokens: List[str], sentences: List[str]) -> float:
        """Calculate a simplified readability score (0-100)."""
        if not tokens or not sentences:
            return 0.0
        avg_sentence_len = len(tokens) / len(sentences)
        avg_word_len = self._avg_word_length(tokens)
        # Simplified Flesch-like formula (higher = more readable)
        score = max(0, min(100, 206.835 - 1.015 * avg_sentence_len - 84.6 * (avg_word_len / 5)))
        return round(score, 1)
