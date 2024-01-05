# ArXiv Agent
This project is a RAG agent to assist the user in finding new, relevant research
papers. Using the arXiv API, it utilizes a broad search for recent papers. Then,
using a small description of the users research interests in combination with
each papers abstract, an LLM scores paper relevance, outputing a list of
relevant papers for the user to read. 

## Requirements
- [`arxiv`](https://github.com/lukasschwab/arxiv.py) -- For searching recent 
arXiv papers
- [`text-generation-inference`](https://github.com/huggingface/text-generation-inference)
-- For providing LLM Inference. Support for other inference methods will be added in the future. 

## Input JSON format
To facilitate flexibility this project reads configuration data from a JSON file.
This JSON file must contain the following fields.

- `research_interests`: An English language sentence describing your research interests.
- `queries`: A list of queries for the arXiv API, such as "LLMs" or "knowledge graphs".
- `query_k`: The number of documents to retrieve from arXiv.
- `categories`: A list of categories to limit arXiv search to. If empty will query all of arXiv. See [arxiv taxonomy](https://arxiv.org/category_taxonomy).
- `inference_url`: The URL of your `text-generation-inference` server.
- `model_type`: The type of model used (for prompt formatting). Current options are llama and mistral.

See `example-config.json` for an example of how to configure your personal agent. 

## Usage
To use the arXiv agent, first customize a config as described above.  To execute arXiv agent:

```
python arxiv-agent.py your-config.json
```

If no config is provided, it will use `config.json, if it exists.

## Output
Currently, arXiv agent outputs a markdown formatted list of the retrieved articles to `stdout`,
sorted by LLM ranking. File output will be added soon. 
The output include the article title, abstract, llm score, and its url. 

Without file output support it is advised to save your article list using redirections in your shell of choice. 

## Todo
- Add File output
- Add basic interactive shell for exploring output. 
- Add Truncation on output based on score
- Add Other LLM APIs
- Add Support for modifying research interest statement and queries based on 
retrieval and relevant documents

