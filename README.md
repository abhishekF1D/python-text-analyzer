# Python Text Analyzer

A beginner-friendly Python project that analyzes text and displays useful statistics such as word count, character count, sentence count, vowels, consonants, and the most frequent word.

## About the Project

The Python Text Analyzer is a command-line application developed using Python. It accepts text from the user, processes it, and displays a summary of the text.

This project demonstrates fundamental Python programming concepts, including functions, strings, regular expressions, and the `Counter` class.

## Features

- Count total words.
- Count total characters.
- Count characters without whitespace.
- Count sentences and paragraphs.
- Count vowels and consonants.
- Find the most frequently used word.
- Handle empty input with an error message.

## Technologies Used

- **Language:** Python 3
- **Modules:** `re` and `collections`
- **Interface:** Command-line interface (CLI)

## Project Structure

```text
python-text-analyzer/
├── text_analyzer.py
├── README.md
├── requirements.txt
├── .gitignore
└── test_text_analyzer.py
```

## Requirements

- Python 3.8 or newer
- No third-party Python packages are required.

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project directory.
3. Run:

```bash
python text_analyzer.py
```

On some systems, use `python3` instead of `python`.

## Example

**Input:**

```text
Python is easy. Python is powerful!
```

**Output:**

```text
Total words: 6
Total characters: 35
Characters without whitespace: 30
Total sentences: 2
Total paragraphs: 1
Total vowels: 9
Total consonants: 19
Most frequent word: python
Word frequency: 2
```

## How It Works

1. The program accepts text from the user.
2. Regular expressions identify words and sentences.
3. String operations count characters, vowels, and consonants.
4. `Counter` identifies the most frequent word.
5. Results are displayed in the terminal.

## Run the Tests

```bash
python -m unittest -v
```

## Future Improvements

- Add a graphical user interface.
- Analyze text from uploaded files.
- Display a complete word-frequency table.
- Add sentiment analysis.
- Generate downloadable analysis reports.

## Learning Outcomes

This project helps beginners understand Python functions, string manipulation, regular expressions, collections, and basic text processing.

## Author

Abhishek kumar.

## License

This project is available for educational and learning purposes.
