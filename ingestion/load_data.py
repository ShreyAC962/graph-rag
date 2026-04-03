from ingestion.entity_extractor import extract_relations
from ingestion.graph_builder import GraphBuilder

def load_data(file_path):
    with open(file_path, "r") as f:
        text = f.read()

    relations = extract_relations(text)

    graph = GraphBuilder()
    graph.insert(relations)
    graph.close()

if __name__ == "__main__":
    load_data("data/sample.txt")