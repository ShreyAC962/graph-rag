from neo4j import GraphDatabase
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

class GraphBuilder:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD)
        )

    def close(self):
        self.driver.close()

    def create_entity(self, tx, name):
        tx.run("MERGE (e:Entity {name: $name})", name=name)

    def create_relation(self, tx, subj, rel, obj):
        tx.run(
            """
            MERGE (a:Entity {name: $subj})
            MERGE (b:Entity {name: $obj})
            MERGE (a)-[:REL {type: $rel}]->(b)
            """,
            subj=subj,
            obj=obj,
            rel=rel,
        )

    def insert(self, relations):
        with self.driver.session() as session:
            for subj, rel, obj in relations:
                session.write_transaction(
                    self.create_relation, subj, rel, obj
                )