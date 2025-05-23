# --------------------------------------------------------------------
# Geração de instâncias de doentes a partir de doentes.json
# RPCW 2025 - Ficha Medicina - Exercício 2
# --------------------------------------------------------------------
import json
from rdflib import Graph, Namespace, URIRef, RDF, Literal
from rdflib.namespace import XSD

# --------------------------------------------------------------------
# Carregar ontologia base (com tratamentos)
# --------------------------------------------------------------------
n = Namespace("http://www.example.org/disease-ontology#")
g = Graph()
g.parse("med_tratamentos.ttl", format="turtle")

# --------------------------------------------------------------------
# Criar propriedades se ainda não existirem
# --------------------------------------------------------------------
g.add((n.nome, RDF.type, RDF.Property))
g.add((n.exhibitsSymptom, RDF.type, RDF.Property))  # já deves ter, mas por segurança
g.add((n.exhibitsSymptom, RDF.type, RDF.Property))
g.add((n.exhibitsSymptom, RDF.type, n.Symptom))

# --------------------------------------------------------------------
# Processar ficheiro JSON
# --------------------------------------------------------------------
with open("doentes.json", encoding='utf-8') as f:
    dados = json.load(f)

for idx, doente in enumerate(dados):
    id_doente = f"doente_{idx+1}"
    uri_doente = URIRef(f"{n}{id_doente}")
    
    g.add((uri_doente, RDF.type, n.Patient))
    g.add((uri_doente, n.nome, Literal(doente["nome"], datatype=XSD.string)))
    
    for sintoma in doente["sintomas"]:
        sintoma_uri = URIRef(f"{n}{sintoma.strip().replace(' ', '_')}")
        g.add((uri_doente, n.exhibitsSymptom, sintoma_uri))

print(g.serialize())