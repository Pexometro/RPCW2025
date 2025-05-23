
## 11.  Uma vez criada a ontologia (última versão: med_doentes.ttl), especifica queries SPARQL que permitam responder às seguintes questões:

### Quantas doenças estão presentes na ontologia?

PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.example.org/disease-ontology#>

SELECT (COUNT(DISTINCT ?doenca) AS ?n_doencas)
WHERE {
  ?doenca a :Disease .
}

### Que doenças estão associadas ao sintoma "yellowish_skin"?

PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.example.org/disease-ontology#>

SELECT DISTINCT ?doenca
WHERE {
  ?doenca a :Disease .
  ?doenca :hasSymptom :yellowish_skin .
}

### Que doenças estão associadas ao tratamento "exercise"?

PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.example.org/disease-ontology#>

SELECT DISTINCT ?doenca
WHERE {
  ?doenca a :Disease .
  ?doenca :hasTreatment :exercise .
}

### Produz uma lista ordenada alfabeticamente com o nome dos doentes.

PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.example.org/disease-ontology#>

SELECT ?nome
WHERE {
  ?doente a :Patient .
  ?doente :nome ?nome
}ORDER BY ?nome


## 12. Cria uma query CONSTRUCT que diagnostique a doença de cada pessoa, ou seja, produza uma lista de triplos com a  orma :patientX :hasDisease :diseaseY. No fim, acrescenta estes triplos à ontologia;

PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.example.org/disease-ontology#>

CONSTRUCT {
  ?paciente :hasDisease ?doenca .
}
WHERE {
  ?paciente a :Patient ;
            :exhibitsSymptom ?sintoma .
  ?doenca a :Disease ;
          :hasSymptom ?sintoma .
}

INSERT {
  ?paciente :hasDisease ?doenca .
}
WHERE {
  ?paciente a :Patient ;
            :exhibitsSymptom ?sintoma .
  ?doenca a :Disease ;
          :hasSymptom ?sintoma .
}

## 13. Cria um query SPARQL que poduza uma distribuição dos doentes pelas doenças, ou seja, dá como resultado uma lista de pares (doença, nº de doentes);

PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.example.org/disease-ontology#>

SELECT ?doenca (COUNT(DISTINCT ?doente) AS ?n_doentes)
WHERE {
  ?doente a :Patient .
  ?doente :hasDisease ?doenca .
}
GROUP BY ?doenca
ORDER BY DESC(?n_doentes)

## 14.  Cria um query SPARQL que poduza uma distribuição das doenças pelos sintomas, ou seja, dá como resultado uma lista de pares (sintoma, nº de doenças com o sintoma);

PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.example.org/disease-ontology#>

SELECT ?sintoma (COUNT(DISTINCT ?doenca) AS ?n_doencas)
WHERE {
  ?doenca a :Disease .
  ?doenca :hasSymptom ?sintoma .
}
GROUP BY ?sintoma
ORDER BY DESC(?n_doencas)

## 15.  Cria um query SPARQL que poduza uma distribuição das doenças pelos tratamentos, ou seja, dá como resultado uma lista de pares (tratamento, nº de doenças com o tratamento).

PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.example.org/disease-ontology#>

SELECT ?tratamento (COUNT(DISTINCT ?doenca) AS ?n_doencas)
WHERE {
  ?doenca a :Disease .
  ?doenca :hasTreatment ?tratamento .
}
GROUP BY ?tratamento
ORDER BY DESC(?n_doencas)

