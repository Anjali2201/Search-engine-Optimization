import re
from nltk.corpus import stopwords
from collections import defaultdict
from web_scrapping import urls

# Download NLTK stopwords data
import nltk
nltk.download("stopwords")

# Load stopwords and create a set for faster lookup
stop_words = set(stopwords.words("english"))

# Initialize the inverted index
inverted_index = defaultdict(list)
term_frequency_index = defaultdict(dict)

# Process each document and build the inverted index and term frequency index
num_documents = len(urls)  # number of documents
for i in range(num_documents):
    with open(f"documents/document_{i}.txt", "r", encoding="utf-8") as file:
        doc = file.read()
        words = re.findall(r'\b\w+\b', doc.lower())  # Tokenization and lowercase
        words = [word for word in words if word not in stop_words]  # Remove stopwords
        term_frequency = defaultdict(int)  # To keep track of term frequency within each document
        for word in words:
            inverted_index[word].append(i)  # Store document index
            term_frequency[word] += 1
        term_frequency_index[i] = term_frequency

# Convert lists to sets for faster membership testing
for term, doc_indices in inverted_index.items():
    inverted_index[term] = set(doc_indices)