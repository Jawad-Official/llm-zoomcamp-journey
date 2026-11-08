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

## Module 2: Vector Search (`02-vector-search/`)

Search by **meaning** instead of exact words: turn text into vectors (embeddings) and find the closest ones.

| Lesson | Topic | File |
| --- | --- | --- |
| 1 | What is vector search | `01-07_vector_search.ipynb` |
| 2 | Embeddings | `01-07_vector_search.ipynb` |
| 3 | Embedding our dataset | `01-07_vector_search.ipynb` |
| 4 | Vector search with numpy | `01-07_vector_search.ipynb` |
| 5 | Vector search with minsearch | `01-07_vector_search.ipynb` |
| 6 | RAG with vector search | `01-07_vector_search.ipynb` |
| 7 | Vector search with sqlitesearch | end of `01-07_vector_search.ipynb` (creates `faq_vectors2.db`), then `07b_sqlitesearch_persistent.ipynb` |
| 8 | Vector search with PGVector | `08_pgvector.ipynb` (needs Postgres with pgvector on port 5433) |
| 9 (optional) | ONNX embedder | `09_onnx_embedder.ipynb`, `download.py`, `embedder.py`. **Not my work:** I skipped this optional lesson, and Claude added it at my request. |
| 10 | Next steps | end of `09_onnx_embedder.ipynb` |

`ingest.py` and `rag_helper.py` are intentional copies of the Module 1 files (notebooks can only import from their own folder).
