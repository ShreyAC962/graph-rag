from retrieval.graph_query import GraphQuery
from retrieval.context_builder import build_context
from llm.ollama_client import generate_answer

def run_query(question):
    entity = question.split()[0]  # simple heuristic

    graph = GraphQuery()
    data = graph.query(entity)

    context = build_context(data)

    answer = generate_answer(context, question)

    return answer


if __name__ == "__main__":
    while True:
        q = input("Ask: ")
        print(run_query(q))