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

Traditional RAG = retrieve chunks → send to LLM
Graph RAG = build entity relationships → reason over graph → send structured context to LLM

Example:
"Apple acquired Beats in 2014"
Graph becomes:
Apple ──(acquired)──> Beats
        └──(year)──> 2014
Now LLM can answer:

“What companies did Apple acquire?”
“Which acquisitions happened in 2014?”

## Architecture Overview
    User Query
        ↓
    Query → Entity Extraction
        ↓
    Graph Traversal (Neo4j)
        ↓
    Relevant Subgraph
        ↓
    Context Builder
        ↓
    Ollama LLM (Mistral/Llama)
        ↓
    Final Answer

## Production-Ready File Structure
graph_rag/
│
├── app.py
├── config.py
├── requirements.txt
│
├── ingestion/
│   ├── load_data.py
│   ├── entity_extractor.py
│   ├── graph_builder.py
│
├── retrieval/
│   ├── graph_query.py
│   ├── context_builder.py
│
├── llm/
│   ├── ollama_client.py
│
├── utils/
│   ├── logger.py
│
└── data/
    └── sample.txt