from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://localhost:7200/repositories/repo-test-1")
sparql.setReturnFormat(JSON)

print("sparql: {}".format(sparql))

# sparql_query = """SELECT  (COUNT(?p) AS ?cnt) WHERE { ?s ?p ?o}"""
# sparql_query = """
#     SELECT *
#     WHERE {
#         ?e1 ?p ?e2 .
#     }
#     LIMIT 3
#     """
# sparql_query = """
#     SELECT *
#     WHERE {
#         ?e1 ?p ?e2 .
#     }
#     """
sparql_query = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX : <http://www.semanticweb.org/wikimovies#> SELECT DISTINCT ?uri  WHERE {     ?intermediate_ent_1 :written_by :entity24121;     :starred_actors ?uri;     rdf:type :Movie.          :movie12868 :starred_actors ?uri.          ?uri rdf:type :Actor. }"""

sparql.setQuery(sparql_query)

try:
    ret = sparql.queryAndConvert()

    for r in ret["results"]["bindings"]:
        print(r)
except Exception as e:
    print(e)