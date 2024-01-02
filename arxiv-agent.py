# A basic agents structure for retreiving relevant articles for arXiv
# Uses a broad search through the arXiv API before scoring article relevance

import arxiv

client = arxiv.Client()


#A String representing your interests for LLM processing
research_interests = '''
I am intersted in large language models and LLM agents, 
specifically how they retrieve and process data
'''

# Query for broad arxiv search
queries = ['"Large Language Model"', 'Agents']

# How many docs to retrieve per query. 
query_k = 10

# category to limit query to
categories = ["cs.AI", "cs.HC", "cs.IR", "cs.LG", "cs.MA"]


# Build the arxiv query.
query = ""
for q in queries:
    if query == "":
        query = query + "(all:" + q
    else:
        query = query + " OR  all:" + q
query = query + ")"

for i, c in enumerate(categories):
    if i == 0:
        query = query + " AND (cat:" + c
    else:
        query = query + " OR cat:" + c

query = query + ")"


print(query)

search = arxiv.Search(
    query  = query,
    max_results = query_k,
    sort_by = arxiv.SortCriterion.SubmittedDate)

results = client.results(search)

for r in results:
    print(r.title)
    print(r.summary)
    print(r.updated)
