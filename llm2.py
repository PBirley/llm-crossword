from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os


load_dotenv()

llm = init_chat_model(
    "openai:gpt-4.1",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.0,
)

response = llm.invoke("What is the capital of France?")
print(response)
