from langchain_openai import AzureOpenAI
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

llm = AzureOpenAI(
    deployment_name="gpt-4o",
)

llm.invoke("What is the capital of France?")
