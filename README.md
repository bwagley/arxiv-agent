# Arxiv Agent
This project is a RAG agent to assist the user in finding new, relevant research
papers. Using the arXiv API, it utilizes a broad search for recent papers. Then,
using a small description of the users research interests in combination with
each papers abstract, an LLM scores paper relevance, outputing a list of
relevant papers for the user to read. 

## Requirements
- [arxiv](https://github.com/lukasschwab/arxiv.py) -- For searching recent 
arXiv papers
- [text-generation-inference](https://github.com/huggingface/text-generation-inference)
-- For providing LLM Inference. Support for other inference methods will be added in the future. 

## Todo
- Add LLM Ranking
- Add Support for other LLM APIs
- Add Support for storing Research Interest and query metadata in a file
- Add Support for modifying research interest statement and queries based on 
retrevial and relevant documents

