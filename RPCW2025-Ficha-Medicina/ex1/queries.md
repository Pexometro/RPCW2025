
## 1. Quantas classes estão definidas na Ontologia?
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX : <http://www.semanticweb.org/pexo/ontologies/2025/ficha_afericao/>

select (COUNT(DISTINCT ?class) AS ?numclass ) where{
    ?class a owl:Class .
}

## 2. Quantas Object Properties estão definidas na Ontologia?

PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX : <http://www.semanticweb.org/pexo/ontologies/2025/ficha_afericao/>

select (COUNT(DISTINCT ?object) AS ?objectProperties ) where{
    ?object a owl:ObjectProperty .
}

## 3. Quantos indivíduos existem na Ontologia?

SELECT (COUNT(DISTINCT ?ind) AS ?numIndividuos)
WHERE {
  ?ind a ?type .
  FILTER (!isBlank(?ind) && !isBlank(?type) && ?type != owl:Class && ?type != owl:ObjectProperty && ?type != rdf:Property)
}

## 4. Quem planta tomates?
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX : <http://www.semanticweb.org/pexo/ontologies/2025/ficha_afericao/>

SELECT ?tom 
WHERE {
  ?tom a :Agricultor .
  ?tom :cultiva :Tomate
}


## 5. Quem contrata trabalhadores temporários?

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX : <http://www.semanticweb.org/pexo/ontologies/2025/ficha_afericao/>

SELECT ?tom 
WHERE {
  ?tom a :Agricultor .
  ?tom :contrata :Trabalhador .
}
