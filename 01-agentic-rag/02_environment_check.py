"""Lesson 2: environment check.

Simple version: before the real work, say "Hello" to the AI to make sure the
phone line works (correct Azure address, valid key, model deployed).

Run it from the project root:  uv run --env-file .env python 01-agentic-rag/02_environment_check.py
(--env-file loads AZURE_API_KEY from .env; in VS Code's terminal it's already loaded for you.)
"""
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://26120057-2478-resource.openai.azure.com/openai/v1",
    api_key=os.environ["AZURE_API_KEY"],
)

resp = client.responses.create(
    model="gpt-5-nano",  # deployment name
    input="Hello",
    reasoning={"effort": "minimal"},
)
print(resp.output_text)