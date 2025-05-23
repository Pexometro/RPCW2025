# --------------------------------------------------------------------
# Geração da ontologia médica a partir de Disease_Syntoms.csv
# RPCW 2025 - Ficha Medicina - Exercício 2
# --------------------------------------------------------------------
import csv
from rdflib import Graph, Namespace, URIRef, RDF

# --------------------------------------------------------------------
# Carregar ontologia base
# --------------------------------------------------------------------
n = Namespace("http://www.example.org/disease-ontology#")
g = Graph()
g.parse("med_doencas2.ttl", format="turtle")

# --------------------------------------------------------------------
# Processar ficheiro CSV com reader
# --------------------------------------------------------------------
ficheiro = "Disease_Treatment.csv"
# A partir de Disease_Treatment.csv vais criar uma instância para cada tratamento se esta ainda não existir; Vais associar cada doença criada aos respetivos tratamentos;

doencas = []
tratamentos = []
with open(ficheiro, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)  
    
    for linha in reader:
        nome_doenca = linha[0].strip().replace(" ", "_")
        doenca_uri = URIRef(f"{n}{nome_doenca}")

        if nome_doenca not in doencas:
            g.add((doenca_uri, RDF.type, n.Disease))
            doencas.append(nome_doenca)

        # Processar colunas de tratamentos (colunas 1 em diante)
        for tratamento in linha[1:]:
            nome_tratamento = tratamento.strip().replace(" ", "_")
            tratamento_uri = URIRef(f"{n}{nome_tratamento}")
            if nome_tratamento not in tratamentos:
                g.add((tratamento_uri, RDF.type, n.Treatment))
                tratamentos.append(nome_tratamento)

                # Associar doença ao tratamento
            g.add((doenca_uri, n.hasTreatment, tratamento_uri))

print(g.serialize())
