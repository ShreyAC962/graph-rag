def build_context(graph_data):
    context = ""

    for record in graph_data:
        context += f"{record['a.name']} {record['r.type']} {record['b.name']}\n"

    return context