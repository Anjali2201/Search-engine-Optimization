from inverted_index import inverted_index
from web_scrapping import urls

# Function to perform search and retrieve relevant documents
def search(query):
    query = query.lower()
    query_terms = query.split()
    relevant_docs = set(range(len(urls)))  
    matching_docs = {}
    for term in query_terms:
        if term in inverted_index:
            relevant_docs &= inverted_index[term]
            for doc_index in inverted_index[term]:
                if doc_index in matching_docs:
                    matching_docs[doc_index].add(term)
                else:
                    matching_docs[doc_index] = {term}
    return relevant_docs, matching_docs

# Example search query
query = input("Enter your search query: ")
results, matching_docs = search(query)

# Display documents or names with links
for doc_index in results:
    doc_name = f"document_{doc_index}.txt"
    doc_link = f"documents/{doc_name}"
    matched_terms = ", ".join(matching_docs[doc_index])
    print(f"Document: {doc_name} (Matching terms: {matched_terms})")
    print(f"Link: {doc_link}\n")