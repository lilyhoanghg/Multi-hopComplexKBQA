import rdflib

g = rdflib.Graph()

g.parse("data/METAQA2/rdf_kb_v4.2.owl", format="xml")

sparql_query = """SELECT DISTINCT ?e1 ?p ?e2 WHERE {?e1 ?p ?e2.} LIMIT 2"""

q_result = g.query(sparql_query)