import unittest

from text_analyzer import analyze_text


class TestTextAnalyzer(unittest.TestCase):

    def test_word_count(self):
        result = analyze_text("Python is easy.")
        self.assertEqual(result["words"], 3)

    def test_sentence_count(self):
        result = analyze_text("Hello! How are you?")
        self.assertEqual(result["sentences"], 2)

    def test_vowel_count(self):
        result = analyze_text("apple")
        self.assertEqual(result["vowels"], 2)

    def test_consonant_count(self):
        result = analyze_text("apple")
        self.assertEqual(result["consonants"], 3)

    def test_most_common_word(self):
        result = analyze_text("Python is fun. Python is easy.")
        self.assertEqual(result["most_common_word"], "python")
        self.assertEqual(result["word_frequency"], 2)

    def test_empty_text(self):
        result = analyze_text("")
        self.assertEqual(result["words"], 0)
        self.assertEqual(result["paragraphs"], 0)
        self.assertEqual(result["most_common_word"], "None")


if __name__ == "__main__":
    unittest.main()
