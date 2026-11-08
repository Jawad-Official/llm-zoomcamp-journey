"""Lesson 8: RAG helper (the robot blueprint).

Simple version: RAGBase is a blueprint for a question-answering robot.
Every robot built from it does the same 3 steps:
    1. search()       -> find the best FAQ cards for the question
    2. build_prompt() -> write a note: question + those cards
    3. llm()          -> ask the AI (Azure gpt-5-nano) to answer using the note
rag() runs all 3 steps with one call.

Used by: 08_rag_helper.ipynb, 09b_persistent_rag.ipynb, 11-16_agents.ipynb
"""
from ingest import load_faq_data, build_index
from openai import OpenAI
from dotenv import load_dotenv
from os import getenv

load_dotenv()

openai_client = OpenAI(
    base_url="https://26120057-2478-resource.openai.azure.com/openai/v1",
    api_key=getenv("AZURE_API_KEY"),
)


documents = load_faq_data()
index = build_index(documents)


INSTRUCTIONS = """
Your task is to answer questions from the course participants based on the provided context.

Use the context to find relevant information and provide accurate answers. If the answer is not found in the context, respond with "I don't know."
"""

USER_PROMPT_TEMPLATE = '''

Question: {question}

Context: {context}
'''


search_tool = {
    "type": "function",
    "name": "search",
    "description": "Search the FAQ database for entries matching the given query.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query text to look up in the course FAQ."
            }
        },
        "required": ["query"],
        "additionalProperties": False
    }
}


class RAGBase:
    def __init__(
        self,
        index,
        llm_client,
        instructions=INSTRUCTIONS,
        course="llm-zoomcamp",
        prompt_template=USER_PROMPT_TEMPLATE,
        model="gpt-5-nano",
        tools = [search_tool]
    ):
        self.index = index
        self.llm_client = llm_client
        self.instructions = instructions
        self.course = course
        self.prompt_template = prompt_template
        self. model = model
        self.tools = tools



    def search(self, query, num_results=5):
        boost_dict = {'question': 3.0, 'section': 0.5}
        filter_dict = {'course': self.course}

        return self.index.search(
            query,
            num_results = num_results,
            boost_dict = boost_dict,
            filter_dict = filter_dict,
        )


    def build_context(self, search_results):
        lines = []

        for doc in search_results:
            lines.append(doc["section"])
            lines.append("Q: " + doc["question"])
            lines.append("A: " + doc["answer"])
            lines.append("")

        return "\n".join(lines).strip()

    def build_prompt(self, query, search_results):
        context = self.build_context(search_results)
        return self.prompt_template.format(
            question=query, context=context
        )


    def llm(self, prompt):
        input_messages = [
            {"role": "developer", "content": self.instructions},
            {"role": "user", "content": prompt}
        ]

        response = self.llm_client.responses.create(
            model=self.model,
            input=input_messages
        )

        return response.output_text
    

    def rag(self, query):
        search_results = self.search(query)
        prompt = self.build_prompt(query, search_results)
        answer = self.llm(prompt)
        return answer


#changing llme provider
'''
class OllamaRAG(RAGBase):
    def llm(self, prompt):
        return super().llm(prompt)
'''