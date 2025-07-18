import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from src.crossword.utils import load_puzzle
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
import json


# Load environment variables from .env file
load_dotenv()


llm = init_chat_model(
    "openai:gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.0,
)


def guess_crossword(clue: str, length: int) -> str:
    class GuessRequest(BaseModel):
        """You are an expert crossword solver. Given a clue and the length of the answer, provide your best guess."""

        guess: str = Field(
            ...,
            description="You are an expert crossword solver. Given a clue and the length of the answer, provide your best guess.",
            length=length,
        )

    expert_guesser = llm.with_structured_output(GuessRequest)

    guess = expert_guesser.invoke(
        json.dumps({"clue": clue, "length": length}, indent=2)
    )
    return guess.guess.upper()


# Load the puzzle
puzzle = load_puzzle("data/easy.json")


# Generate a guess for each clue
for clue in puzzle.clues:
    print(f"--- Guessing for clue: {clue.text} ---")
    guess = guess_crossword(clue.text, clue.length)
    print(f"Guess: {guess}")

    print("--- Set a guess ---")
    puzzle.set_clue_chars(clue, list(guess))
    print(puzzle)


print(puzzle.validate_all())


# See if there are any conflicting guesses
# In which case, resolve the conflict

# Once resolved submit the guess


# ----
# is there an agentic approach to this?
