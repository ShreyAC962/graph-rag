from neo4j import GraphDatabase
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

class GraphQuery:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD)
        )

    def query(self, entity):
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (a:Entity)-[r]->(b:Entity)
                WHERE a.name CONTAINS $entity
                RETURN a.name, r.type, b.name
                """,
                entity=entity,
            )
            return result.data()