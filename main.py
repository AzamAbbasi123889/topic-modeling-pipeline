"""
Topic Modeling Pipeline - Main Entry Point

Demonstrates NLP text processing pipeline with tokenization,
feature extraction, and analysis.
"""

import json
from src.preprocessor import TextPreprocessor
from src.analyzer import TextAnalyzer
from src.config import SAMPLE_TEXTS


def main():
    """Run the NLP pipeline on sample texts."""
    print("=" * 60)
    print("Topic Modeling Pipeline")
    print("=" * 60)

    preprocessor = TextPreprocessor()
    analyzer = TextAnalyzer()

    for i, text in enumerate(SAMPLE_TEXTS, 1):
        print(f"\n--- Document {i} ---")
        print(f"Input: {text[:80]}...")

        # Preprocess
        tokens = preprocessor.tokenize(text)
        cleaned = preprocessor.clean(text)

        # Analyze
        result = analyzer.analyze(cleaned)

        print(f"Tokens: {len(tokens)}")
        print(f"Sentences: {result['sentence_count']}")
        print(f"Avg word length: {result['avg_word_length']:.1f}")
        print(f"Vocabulary richness: {result['vocab_richness']:.3f}")
        print(f"Top keywords: {', '.join(result['keywords'][:5])}")

    print("\n" + "=" * 60)
    print("Analysis complete.")


if __name__ == "__main__":
    main()
