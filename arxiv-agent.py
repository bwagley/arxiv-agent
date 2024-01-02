import arxiv

client = arxiv.Client()


#A String representing your interests for LLM processing
research_interests = "I am intersted in large language models and LLM agents, specifically how they retrieve and process data"

# Query for broad arxiv search
queries = ['"Large Language Models"', 'Agents']

# How many docs to retrieve per query. 
query_k = 10

# Journal to limit query to
journal = "CS"


# Build the arxiv query.
query = ""
for q in queries:
    if query == "":
        query = query + "(all:" + q
    else:
        query = query + " OR  all:" + q
query = query + ")"

query = query + " AND jr:" + journal

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
