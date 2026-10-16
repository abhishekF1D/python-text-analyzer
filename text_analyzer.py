"""
Project: Python Text Analyzer
Description: Analyzes text and calculates useful statistics.
"""

import re
from collections import Counter


def analyze_text(text):
    """Analyze text and return its statistics."""
    words = re.findall(r"\b[\w']+\b", text.lower())

    sentences = [
        sentence
        for sentence in re.split(r"[.!?]+", text.strip())
        if sentence.strip()
    ]

    paragraphs = [
        paragraph
        for paragraph in re.split(r"\n\s*\n", text.strip())
        if paragraph.strip()
    ]

    vowels = sum(1 for char in text.lower() if char in "aeiou")
    consonants = sum(
        1 for char in text.lower()
        if char.isalpha() and char not in "aeiou"
    )

    word_counts = Counter(words)
    most_common = word_counts.most_common(1)

    return {
        "words": len(words),
        "characters": len(text),
        "characters_without_whitespace": sum(
            1 for char in text if not char.isspace()
        ),
        "sentences": len(sentences),
        "paragraphs": len(paragraphs) if text.strip() else 0,
        "vowels": vowels,
        "consonants": consonants,
        "most_common_word": most_common[0][0] if most_common else "None",
        "word_frequency": most_common[0][1] if most_common else 0,
    }


def main():
    print("=" * 35)
    print("       PYTHON TEXT ANALYZER")
    print("=" * 35)

    text = input("\nEnter your text: ")

    if not text.strip():
        print("Error: Please enter some text.")
        return

    result = analyze_text(text)

    print("\n-------- ANALYSIS RESULTS --------")
    print("Total words:", result["words"])
    print("Total characters:", result["characters"])
    print(
        "Characters without whitespace:",
        result["characters_without_whitespace"],
    )
    print("Total sentences:", result["sentences"])
    print("Total paragraphs:", result["paragraphs"])
    print("Total vowels:", result["vowels"])
    print("Total consonants:", result["consonants"])
    print("Most frequent word:", result["most_common_word"])
    print("Word frequency:", result["word_frequency"])
    print("---------------------------------")


if __name__ == "__main__":
    main()
