# Conversão de JSON para Ontologia com RDFLib

## Autor
### Pedro Azevedo

## Descrição
Este projeto visa a criação de uma ontologia baseada num dos exemplos do ficheiro JSON fornecido. Com isso, utilizamos Python e a biblioteca RDFLib para converter todo o JSON numa ontologia em formato Turtle (.ttl).

## Como Funciona
1. **Criar a Ontologia Base**
   - O ficheiro `exameMedico.ttl` contém a estrutura básica da ontologia.
   
2. **Executar o Script de Conversão**
   - O script `convertor.py` carrega os dados do ficheiro `exames.json` e adiciona a informação à ontologia.
   - O ficheiro gerado `final.ttl` conterá todos os exames convertidos.

### Execução
Para executar a conversão, utilizar o comando:
```bash
python3 convertor.py
```
Isso irá gerar um ficheiro `final.ttl` contendo os dados convertidos para RDF/Turtle.

## Exemplo de Saída
```ttl
@prefix : <http://www.semanticweb.org/rui/ontologies/2025/TPC/> .

:Pessoa/60b3ee0ee00725274024d5a2 a :Pessoa ;
    :temPrimeiroNome "Emily" ;
    :temUltimoNome "Terrell" ;
    :temIdade 28 ;
    :temGenero "F" ;
    :pratica :Modalidade/Futebol .

:Exame/60b3ee0ee00725274024d5a2 a :Exame ;
    :temData "2020-07-27" ;
    :temResultado true .
```

## Conclusão
Este projeto demonstrou como podemos estruturar dados JSON numa ontologia e converter esses dados de forma automatizada com Python e RDFLib. 