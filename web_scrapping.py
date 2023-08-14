import requests
from bs4 import BeautifulSoup
import os

# Define a list of URLs representing web pages
urls = [
    "https://www.bbc.com/news/world-asia-66414696",
    "https://www.bbc.com/news/world-asia-india-66402526",
    # Add URLs for other web pages here
]

# Create a directory to store documents
if not os.path.exists("documents"):
    os.makedirs("documents")

# Loop through each URL and extract the contents
for i, url in enumerate(urls):
    # response = requests.get(url)
    # soup = BeautifulSoup(response.text, "html.parser")
    # content = soup.get_text()

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract meaningful content from different HTML elements (you can customize this)
        title = soup.title.text.strip() if soup.title else ""
        paragraphs = [p.get_text().strip() for p in soup.find_all('p')]
        headings = [h.get_text().strip() for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
        
        # Combine extracted content into a single document
        doc_content = "\n".join([title] + headings + paragraphs)
    
        # Save the document to a text file
        filename = f"documents/document_{i}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(doc_content)
