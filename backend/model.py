from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from config import MODEL_NAME

# Load the Hugging Face model
def load_model():
    """Loads the AI model for text generation."""
    hf_pipeline = pipeline("text-generation", model=MODEL_NAME, max_length=100)
    return HuggingFacePipeline(pipeline=hf_pipeline)

llm = load_model()

def get_response(query):
    """Generates a response using the AI model."""
    return llm(query)

