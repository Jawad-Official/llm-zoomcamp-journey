# LLM Zoomcamp 2026: my code

My work for [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp), using **Azure OpenAI (gpt-5-nano)** and the **Responses API**.

## Setup

1. Install dependencies: `uv sync`
2. Create a `.env` file in the project root:

   ```bash
   AZURE_API_KEY=your-key-here
   ```

3. Check the connection: `uv run --env-file .env python 01-agentic-rag/02_environment_check.py`

## Module 1: Agentic RAG (`01-agentic-rag/`)

**Part 1: RAG.** Build a robot that looks up the answer in the course FAQ, then answers.

| Lesson | Topic | File |
| --- | --- | --- |
| 1 | Introduction | `01-07_rag_from_scratch.ipynb` |
| 2 | Environment setup | `01-07_rag_from_scratch.ipynb`, `02_environment_check.py` |
| 3 | What is RAG | `01-07_rag_from_scratch.ipynb` |
| 4 | The course FAQ dataset | `01-07_rag_from_scratch.ipynb` |
| 5 | Search | `01-07_rag_from_scratch.ipynb` |
| 6 | Building a prompt | `01-07_rag_from_scratch.ipynb` |
| 7 | RAG pipeline | `01-07_rag_from_scratch.ipynb` |
| 8 | RAG helper | `08_rag_helper.ipynb`, `rag_helper.py`, `ingest.py` |
| 9 | Data ingestion | `09a_data_ingestion.ipynb` (run once, creates `faq.db`), then `09b_persistent_rag.ipynb` |
| 10 | Wrap-up of Part 1 | end of `09b_persistent_rag.ipynb` |

**Part 2: Agents.** Let the AI decide what to search, and how many times.

| Lesson | Topic | File |
| --- | --- | --- |
| 11 | Agents | `11-16_agents.ipynb` |
| 12 | Quick RAG revision | `11-16_agents.ipynb` |
| 13 | Function calling | `11-16_agents.ipynb` |
| 14 | The agentic loop | `11-16_agents.ipynb` |
| 15 | ToyAIKit | `11-16_agents.ipynb` |
| 16 | Other frameworks | `11-16_agents.ipynb` |

Each notebook marks where every lesson starts (`Lesson N`) and ends (`End of Lesson N`).
