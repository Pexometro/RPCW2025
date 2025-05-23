# --------------------------------------------------------------------
# Geração da ontologia médica: adicionar descrições às doenças
# RPCW 2025 - Ficha Medicina - Exercício 2
# --------------------------------------------------------------------
import csv
from rdflib import Graph, Namespace, URIRef, RDF, Literal
from rdflib.namespace import XSD, OWL, RDFS

# --------------------------------------------------------------------
# Carregar ontologia atualizada com sintomas
# --------------------------------------------------------------------
n = Namespace("http://www.example.org/disease-ontology#")
g = Graph()
g.parse("med_doencas.ttl", format="turtle")

# --------------------------------------------------------------------
# Criar a propriedade :description se ainda não existir
# --------------------------------------------------------------------
g.add((n.description, RDF.type, OWL.DatatypeProperty))
g.add((n.description, RDFS.domain, n.Disease))
g.add((n.description, RDFS.range, XSD.string))

# --------------------------------------------------------------------
# Processar ficheiro CSV com as descrições
# --------------------------------------------------------------------
ficheiro = "Disease_Description.csv"
linhas = []

with open(ficheiro, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)  
    
    for linha in reader:
        disease_name = linha[0].strip().replace(" ", "_")
        disease_uri = URIRef(f"{n}{disease_name}")
        description_text = linha[1].strip()

        if disease_name not in linhas:
            g.add((disease_uri, RDF.type, n.Disease))  # reforço, mesmo que já exista
            g.add((disease_uri, n.description, Literal(description_text, datatype=XSD.string)))
            linhas.append(disease_name)

print(g.serialize())
