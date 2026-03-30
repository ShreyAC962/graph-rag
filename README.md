## Graph RAG 

Traditional RAG = retrieve text chunks
Graph RAG = build a knowledge graph (entities + relationships)

Example:
```
"Amazon acquired Whole Foods"
→ Entities: Amazon, Whole Foods  
→ Relation: ACQUIRED
```
Now instead of: retrieving chunks we do graph traversal + reasoning

## Architecture Overview

                ┌──────────────┐
                │   Raw Docs   │
                └──────┬───────┘
                       ↓
              Entity + Relation Extraction (LLM)
                       ↓
                ┌──────────────┐
                │ Knowledge    │
                │ Graph (Neo4j)│
                └──────┬───────┘
                       ↓
User Query → Graph Query + Vector Search → Context → LLM → Answer

## Production-Ready File Structure
graph-rag/
│
├── app/
│   ├── main.py
│   ├── config.py
│
├── ingestion/
│   ├── loader.py
│   ├── chunker.py
│   ├── extractor.py
│   ├── graph_builder.py
│
├── retrieval/
│   ├── graph_query.py
│   ├── vector_store.py
│   ├── hybrid_retriever.py
│
├── llm/
│   ├── prompt.py
│   ├── generator.py
│
├── db/
│   ├── neo4j_client.py
│
├── utils/
│   ├── logger.py
│
├── requirements.txt
└── README.md