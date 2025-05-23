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
g.parse("medical.ttl", format="turtle")

# --------------------------------------------------------------------
# Processar ficheiro CSV com reader
# --------------------------------------------------------------------
ficheiro = "Disease_Syntoms.csv"
doencas = []
sintomas = []

with open(ficheiro, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)  
    
    for linha in reader:
        nome_doenca = linha[0].strip().replace(" ", "_").replace("(","").replace(")","")
        doenca_uri = URIRef(f"{n}{nome_doenca}")

        if nome_doenca not in doencas:
            g.add((doenca_uri, RDF.type, n.Disease))
            doencas.append(nome_doenca)

        # Processar colunas de sintomas (colunas 1 em diante)
        for sintoma in linha[1:]:
            if sintoma:
                nome_sintoma = sintoma.strip().replace(" ", "_")
                sintoma_uri = URIRef(f"{n}{nome_sintoma}")
                if nome_sintoma not in sintomas:
                    g.add((sintoma_uri, RDF.type, n.Symptom))
                    sintomas.append(nome_sintoma)
                
                    # Associar doença ao sintoma
                g.add((doenca_uri, n.hasSymptom, sintoma_uri))

print(g.serialize())
