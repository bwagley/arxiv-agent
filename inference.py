from text_generation import Client


basic_prompt = '''
{interests}
Given the following abstract, rank the article relevance on a scale of 0 to 10
0 being not relevant at all
5 being relevant to some, but not all research interests
10 being extremely relevant to the given research interests
The abstract is:
    
{abstract}
'''

llama_prompt = "[INST]\n\n" + basic_prompt + "[/INST]"

# Use basic string formatting to populate prompt. 
def format_prompt(prompt, abstract, interests):
    return prompt.format(abstract=abstract, interests=interests)

# Packaged text_gen_inferences client for easy calling
class InferenceClient:
    
    # Uses basic prompt, recommend using a tailored prompts
    def __init__(self, inference_url="http://localhost:8080/", prompt=basic_prompt):
        self.client = Client(inference_url)
        self.prompt = prompt

    # Calls client.generate. Will add support for more arguments in future
    def infer(self, input_dict, temperature=0):
        formatted_prompt = format_prompt(self.prompt, **input_dict)
        return self.client.generate(formatted_prompt, temperature=temperature)


