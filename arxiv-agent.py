# A basic agents structure for retreiving relevant articles for arXiv
# Uses a broad search through the arXiv API before scoring article relevance

import arxiv
import text_generation
import re

from inference import llama_prompt
from inference import InferenceClient


arxiv_client = arxiv.Client()
tgi_client = InferenceClient(inference_url="http://istanbul:8080/", prompt=llama_prompt)


#A String representing your interests for LLM processing
research_interests = '''
I am interested in large language models and LLM agents, 
specifically how they retrieve and process data
'''

# Query for broad arxiv search
queries = ['"Large Language Model"', 'Agents']

# How many docs to retrieve per query. 
query_k = 100

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

results = arxiv_client.results(search)

scored_results = []
rex = re.compile('score\s*\[(.*)\]', re.IGNORECASE)
for r in results:

    score_out = tgi_client.infer({"abstract": r.summary, "interests": research_interests})
    score = int(rex.search(score_out.generated_text).group(1))
    scored_results.append({"title": r.title, "abstract": r.summary, "url": r.entry_id, "score": score})


scored_results = sorted(scored_results, key=lambda x: x["score"])

for r in scored_results:
    print("Title:", r["title"])
    print("Abstract:", r["abstract"])
    print("Score:", r["score"])
    print("url:", r["url"])

