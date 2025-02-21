from langchain.llms import HuggingFacePipeline
from transformers import pipeline

# Load the model
hf_pipeline = pipeline("text-generation", model="facebook/opt-2.7b")
llm = HuggingFacePipeline(pipeline=hf_pipeline)

def get_response(query):
    return llm(query)
