import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import pandas as pd
import os
import pandas as pd
import nltk
import syllapy
from textstat import flesch_reading_ease, textstat
nltk.download('punkt')


df = pd.read_excel("E:/intern/master dictionary/Input.xlsx")


for index, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']

    response = requests.get(url)

    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    td_container = soup.find("div", class_="td-post-content tagdiv-type")
    if td_container:
        td_container_text = td_container.get_text()  # Extract text content from td-container

        with open(f'E:/intern/blackassign/{url_id}.txt', 'w', encoding='utf-8') as file:    # make sure to create a folder named intern
            file.write(td_container_text)
            print(f"Article text for URL ID '{url_id}' has been saved to '{url_id}.txt'.")
    else:
        print(f"Failed to extract content from URL ID '{url_id}'. No 'td-container' found.")

# Initialize an empty set to store all stop words
all_stop_words = set()

# List of file names for stop words
stopwords_files = [
    "E:/intern/StopWords_Auditor.txt",
    "E:/intern/StopWords_Currencies.txt",
    "E:/intern/StopWords_DatesandNumbers.txt",
    "E:/intern/StopWords_Generic.txt",
    "E:/intern/StopWords_GenericLong.txt",
    "E:/intern/StopWords_Geographic.txt",
    "E:/intern/StopWords_Names.txt"
]

for filename in stopwords_files:
    with open(filename, "r", encoding="latin-1") as file:
        for line in file:
            all_stop_words.add(line.strip())

text_folder = "E:/intern/blackassign"
text_files = os.listdir(text_folder)

filter_folder = r"E:\intern\filtered files"  # Using raw string literal for file path

for text_file in text_files:
    if text_file.endswith(".txt"):
        with open(os.path.join(text_folder, text_file), "r", encoding="latin-1") as file:
            text = file.read()

        # Tokenize the text into words
        words = text.split()

        # Remove stop words from the text
        filtered_words = [word for word in words if word.lower() not in all_stop_words]

        # Join the filtered words back into a single string
        filtered_text = " ".join(filtered_words)

        # Construct the filtered text file path correctly
        filtered_text_file = os.path.join(filter_folder, f"filtered_{text_file}")

        with open(filtered_text_file, "w", encoding="latin-1") as file:
            file.write(filtered_text)

        print(f"Processed '{text_file}' and saved filtered text to '{filtered_text_file}'")



def calculate_metrics(text, positive_words, negative_words):

    # Convert text to lowercase
    text = text.lower()
    
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    sentences = nltk.sent_tokenize(text)

    # Get the number of sentences
    num_sentences = len(sentences) 
    
    # Initialize counters for positive and negative words
    positive_count = 0
    negative_count = 0
    
    # Calculate positive and negative scores
    for word in words:
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1

    
    # Calculate positive and negative scores
    positive_score = positive_count 
    negative_score= negative_count

    polarity_score = positive_score - negative_score
    subjectivity_score =(positive_score + negative_score)/ (len(words) + 0.000001)
    avg_sentence_length = len(words)/num_sentences
    
    def is_complex(word):
        
        return len(word) > 3 and word.lower() not in all_stop_words

    # Count the number of complex words
    complex_word_count = sum(1 for word in words if is_complex(word))
    percentage_of_complex_words = complex_word_count/ len(words) 
    fog_index = 0.4*(avg_sentence_length+percentage_of_complex_words)
    avg_words_per_sentence = len(words) / num_sentences
    
    word_count = len(words)
    
    def syllables_per_word(words):
        total_syllables = 0 
        for word in words:
            total_syllables += syllapy.count(word)
    

        if len(words) > 0:
            avg_syllables_per_word = total_syllables / len(words)
        else:
            avg_syllables_per_word = 0  
    
        return avg_syllables_per_word       

    avg_syllables_per_word = syllables_per_word(words)
    personal_pronouns = sum(word.lower() in ['i', 'we', 'my', 'ours', 'us'] for word in words)
    avg_word_length = sum(len(word) for word in words) / word_count

    return [positive_score, negative_score, polarity_score, subjectivity_score, avg_sentence_length,
            percentage_of_complex_words, fog_index, avg_words_per_sentence, complex_word_count,
            word_count, avg_syllables_per_word, personal_pronouns, avg_word_length]

# Read the positive and negative words files
positive_words_file = r"E:\intern\master dictionary\negative-words.txt"
negative_words_file = r"E:\intern\master dictionary\positive-words.txt"

with open(positive_words_file, "r") as file:
    positive_words = set(word.strip().lower() for word in file)

with open(negative_words_file, "r") as file:
    negative_words = set(word.strip().lower() for word in file)


metrics_data = []


filtered_files_folder = r"E:\intern\filtered files"
filtered_files = os.listdir(filtered_files_folder)


for filtered_file in filtered_files:
    if filtered_file.endswith(".txt"):
        with open(os.path.join(filtered_files_folder, filtered_file), "r", encoding="latin-1") as file:
            text = file.read()

        
        metrics = calculate_metrics(text, positive_words, negative_words)

        
        metrics_data.append([filtered_file] + metrics)


columns = ["File Name", "Positive Score", "Negative Score", "Polarity Score", "Subjectivity Score",
           "Avg Sentence Length", "Percentage of Complex Words", "Fog Index",
           "Avg Number of Words per Sentence", "Complex Word Count", "Word Count",
           "Syllables per Word", "Personal Pronouns", "Avg Word Length"]


metrics_df = pd.DataFrame(metrics_data, columns=columns)


input_df = pd.read_excel("E:/intern/master dictionary/Input.xlsx", usecols=["URL_ID", "URL"])


metrics_df = pd.concat([input_df, metrics_df], axis=1)


output_excel_file = r"E:\intern\output\output_data_structure.xlsx"
metrics_df.to_excel(output_excel_file, index=False)

print("output data structure is being created")
