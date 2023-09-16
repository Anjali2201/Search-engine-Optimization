import requests
from bs4 import BeautifulSoup
import os

urls = [
    "https://www.g20.org/en/",
    "https://g20.mygov.in/",
    "https://sdg.iisd.org/events/g20-leaders-summit-2023/",
    "https://github.com/hrsh22/search-engine",
    "https://www.linkedin.com/feed/",
    "https://collegewit.netlify.app/",
    "https://en.wikipedia.org/wiki/Pakistan",
    "https://pwonlyias.com/what-is-g20/",
    "https://www.indiatoday.in/elections/story/pm-modi-meeting-bjp-headquarters-elections-g20-summit-2435196-2023-09-13",
    "https://www.whitehouse.gov/briefing-room/statements-releases/2022/11/16/g20-bali-leaders-declaration/",
    "https://www.whitehouse.gov/briefing-room/statements-releases/",
    "https://www.india.gov.in/",
    "https://www.britannica.com/place/India",
    "https://www.hrw.org/asia/india",
    "https://timesofindia.indiatimes.com/",
    "https://www.britannica.com/place/India/History",
    "https://global.oup.com/academic/category/arts-and-humanities/history/regional-and-national-history/asian-history/indian-history/",
    "https://www.aljazeera.com/news/2023/9/15/canada-hits-pause-on-trade-mission-to-india-after-tensions-at-g20-summit",
    "https://www.nalandaopenuniversity.com/g20-summit-2023-schedule-venue-dates",
    "https://www.g20.org/en/g20-india-2023/new-delhi-summit/"
]

# Creating a directory to store documents
if not os.path.exists("documents"):
    os.makedirs("documents")

# Looping through each URL and extracting the contents
for i, url in enumerate(urls):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extracting meaningful content from different HTML elements
        title = soup.title.text.strip() if soup.title else ""
        paragraphs = [p.get_text().strip() for p in soup.find_all('p')]
        headings = [h.get_text().strip() for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
        
        # Combining extracted content into a single document
        doc_content = "\n".join([title] + headings + paragraphs)
    
        # Saving the document to a text file
        filename = f"documents/document_{i}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(doc_content)
