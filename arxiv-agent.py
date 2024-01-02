# A basic agents structure for retreiving relevant articles for arXiv
# Uses a broad search through the arXiv API before scoring article relevance

import arxiv
import text_generation
import re
import json
import sys

from inference import prompt_select
from inference import InferenceClient

config_file = "config.json"

if len(sys.argv) < 2:
    print("No config specified, defaulting to config.json")
else:
    config_file = sys.argv[1]


try: 
    f = open(config_file)
except:
    print("Error opening config file")
    exit()

config_data = json.load(f)

research_interests = config_data["research_interests"]
queries = config_data["queries"]
query_k = config_data["query_k"]
categories = config_data["categories"]
inference_url = config_data["inference_url"]
model_type = config_data["model_type"]
model_prompt = prompt_select(model_type)

arxiv_client = arxiv.Client()
tgi_client = InferenceClient(inference_url=inference_url, prompt=model_prompt)


# Build the arxiv query.
query = ""
for q in queries:
    if ' ' in q:
        q = '"' + q + '"'

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


scored_results = sorted(scored_results, key=lambda x: x["score"], reverse=True)

for r in scored_results:
    print("#", r["title"])
    print("## Abstract: \n", r["abstract"])
    print("## Score: ", r["score"])
    print("[", r["url"], "](", r["url"], ")\n\n")

