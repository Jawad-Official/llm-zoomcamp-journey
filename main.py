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