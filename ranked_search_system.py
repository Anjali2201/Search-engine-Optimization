from collections import defaultdict 
from inverted_index import inverted_index, term_frequency_index

# Function to perform ranked search and retrieve relevant documents
def ranked_search(query):
    query = query.lower()
    query_terms = query.split()
    doc_scores = defaultdict(float)
    
    for term in query_terms:
        if term in inverted_index:
            for doc_index in inverted_index[term]:
                doc_scores[doc_index] += term_frequency_index[doc_index].get(term, 0)
    
    # Sort documents by scores in descending order
    sorted_docs = sorted(doc_scores.items(), key=lambda x: x[1], reverse=True)
    return [doc_index for doc_index, _ in sorted_docs]

# Example ranked search query
query = input("Enter your search query: ")
ranked_results = ranked_search(query)

# Display ranked documents with links
for doc_index in ranked_results:
    doc_name = f"document_{doc_index}.txt"
    doc_link = f"documents/{doc_name}"
    print(f"Document: {doc_name} (Link: {doc_link})")
