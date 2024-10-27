# Sentimental Analysis

This project was developed as part of an assignment for Blackcoffer company. The aim of the project is to extract, clean, and analyze text data from multiple URLs to derive semantic insights.

## Overview

This project is designed to scrape content from specified URLs, filter out stop words, and calculate various text metrics. The results, including the processed text and calculated metrics, are then saved into an Excel file for further analysis. This project can be useful for tasks such as sentiment analysis, readability assessment, and text quality evaluation.

## Requirements

To run this project, ensure you have the following packages installed:

- `requests`
- `BeautifulSoup4`
- `pandas`
- `nltk`
- `syllapy`
- `textstat`

You can install the required packages using pip:

```bash
pip install requests beautifulsoup4 pandas nltk syllapy textstat openpyxl
```

Additionally, download the NLTK data files by running the following command within your Python environment:

```python
import nltk
nltk.download('punkt')
```

## Input Files

1. **Input Excel File**: Place an Excel file named `Input.xlsx` in the path `E:/intern/master dictionary/`. This file should contain a sheet with the following columns:
   - `URL_ID`: A unique identifier for each URL.
   - `URL`: The URL of the web page from which to scrape content.

2. **Stop Words Files**: Create a folder named `E:/intern/` and place the following stop words files in it:
   - `StopWords_Auditor.txt`
   - `StopWords_Currencies.txt`
   - `StopWords_DatesandNumbers.txt`
   - `StopWords_Generic.txt`
   - `StopWords_GenericLong.txt`
   - `StopWords_Geographic.txt`
   - `StopWords_Names.txt`

3. **Positive and Negative Words Files**: Place two text files containing positive and negative words in the path `E:/intern/master dictionary/`:
   - `positive-words.txt`
   - `negative-words.txt`

## Output

The program will create a folder named `E:/intern/output/` and generate an Excel file named `output_data_structure.xlsx` within it. This file will contain the following columns:

- `File Name`: The name of the processed text file.
- `Positive Score`: The count of positive words in the text.
- `Negative Score`: The count of negative words in the text.
- `Polarity Score`: The difference between positive and negative counts.
- `Subjectivity Score`: The ratio of subjective words to total words.
- `Avg Sentence Length`: The average length of sentences in words.
- `Percentage of Complex Words`: The ratio of complex words to total words.
- `Fog Index`: A readability metric based on sentence length and complex words.
- `Avg Number of Words per Sentence`: The average number of words per sentence.
- `Complex Word Count`: The count of complex words in the text.
- `Word Count`: The total number of words in the text.
- `Syllables per Word`: The average number of syllables per word.
- `Personal Pronouns`: The count of personal pronouns used in the text.
- `Avg Word Length`: The average length of words.

## How to Run

1. Ensure all required files and directories are in place as specified above.
2. Run the Python script containing the provided code.
3. Check the `E:/intern/output/` directory for the generated output Excel file.

## Example of Usage

You can run the script from the command line or an IDE:

```bash
python senti_analysis.py
```

Replace `senti_analysis.py` with the actual name of your Python file.

