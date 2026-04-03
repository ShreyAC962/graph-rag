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
```
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
│
└── data/
    └── sample.txt
```


## How to Run End-to-End
    1. Start Neo4j
    ```neo4j start```
    2. Start Ollama
    ```ollama run mistral```
    3. Load data
    ```python ingestion/load_data.py```
    4. Run app
    ```python app.py```

    Example Queries
    Ask: Apple acquisitions?
    → Apple acquired Beats

    Ask: Who did Google acquire?
    → Google acquired YouTube

 ##   Strengths
    Graph DB (Neo4j) → scalable relationships
    Modular architecture
    Replaceable LLM (Ollama → OpenAI)
    Clear ingestion + retrieval separation

## Real-World Improvements
    1. Better Entity Extraction
    Use: LLM-based extraction instead of spaCy
    2. Add Embeddings
    Hybrid: Graph + Vector DB (FAISS)
    3. Advanced Querying
    Multi-hop traversal
    Cypher optimization
    1. Caching
    Redis for query results
    1. API Layer
    Use: FastAPI

    Pros
    Strong reasoning over relationships
    Multi-hop inference
    Ideal for legal/medical graphs
    
    Cons
    Complex pipeline
    Graph DB overhead
    Higher compute cost