# TPC5

## Autor : Pedro Azevedo
## Número : PG57897

## Run

### Fazer download dos datasets

```sh
./get_imdb_movie_files
```

### Concatenar a informação

- Isto irá criar um ficheiro `movies.json` na diretoria `data` com a informação sobre os mesmos concatenada.

```sh
python3 concatenate_data.py
```

### Criar um novo ficheiro ttl

Para verificar como ficaria a ontologia populada corra o comando:

```sh
python3 populate.py
```

```sh
python3 populate.py > cinema.ttl
```

## Resultados

### Script de concatenação

Ficheiro `data/movies.json`:

```json
{
    "movies": [
        {
            "id": "tt0000147",
            "originalTitle": "The Corbett-Fitzsimmons Fight",
            "duration": 100,
            "releaseYear": 1897,
            "genres": [
                "Documentary",
                "News",
                "Sport"
            ],
            "originalLanguage": null,
            "originalCountry": "US",
            "peopleInvolved": [
                {
                    "nconst": "nm0103755",
                    "category": "producer",
                    "job": "producer",
                    "name": "William A. Brady"
                }
            ]
        }, ...
    ]
}
```

### Ontologia populada

Ficheiro `cinema.ttl` com os novos indivíduos e as suas relações.
