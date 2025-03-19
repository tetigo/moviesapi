# moviesapi

Para instalar o projeto, crie um diretorio e rode no terminal de comando um git clone dentro desse diretorio criado.
<br>
Crie uma venv: python -m venv venv
<br>
Ative a venv: ./venv/Scripts/activate
<br>
Instale as dependências nesse ambiente virtual: pip install -r requirements.txt
<br>
Ainda no terminal, rode: python manage.py migrate para instalar as dependencias do django relativo a banco de dados.
<br>
Rode: python manage.py createsuperuser para criar um usuario admin para sua aplicação.
<br>
Rode: python manage.py runserver para rodar o servidor.
<br>
No browser: http://localhost:8000/admin
<br>
Agora entre as credenciais do usuario criado no passo logo acima.
<br>
Agora vc está dentro do gerenciador da sua aplicação.
<br>
Vc consegue criar users, groups, movies, genres, reviews, actors dentro desse dashboard.
<br>
Para carregar uma lista de atores na tabela actors:
<br>
No terminal rode: python manage.py import_actors actors.csv
<br>
Depois de rodar o comando acima no terminal, se entrar no dashboard e entrar na tabela actors, pode-se visualizar uma lista de atores criadas.
<br>
Todas as rotas da API estão protegidas por Token JWT.


### Lista de rotas:

-------------------------------------------------

#### Token:

POST http://localhost:8000/api/v1/authentication/token/ --> gera token para ser usada nas rotas abaixo

-------------------------------------------------

#### Genres:

GET http://localhost:8000/api/v1/genres/

GET http://localhost:8000/api/v1/genres/1/

POST http://localhost:8000/api/v1/genres/
BODY {
        "id": 13,
        "name": "Teste"
    }

PUT http://localhost:8000/api/v1/genres/2/
BODY {
        "name":"Suspense Again"
    }

DELETE http://localhost:8000/api/v1/genres/3/

OPTIONS http://localhost:8000/api/v1/genres/1

-------------------------------------------------

#### Reviews:

POST http://localhost:8000/api/v1/reviews
BODY {
    "stars": 5,
    "comment":"some comment"
}

As demais rotas seguem o mesmo padrão Restful descrito em gênero

-------------------------------------------------

#### Actors:

POST http://localhost:8000/api/v1/actors
BODY {
    "name": "Mickey",
    "nationality": "USA",
    "birthday": "1970-01-01"
}

As demais rotas seguem o mesmo padrão Restful descrito em gênero

-------------------------------------------------

#### Movies:

POST http://localhost:8000/api/v1/movies
BODY {
        "id": 2,
        "title": "Matrix",
        "release_date": "2021-01-30",
        "resume": "Best movie of all time",
        "genre": 3,
        "actors": [
            1
        ]
    }

As demais rotas seguem o mesmo padrão Restful descrito em gênero

-------------------------------------------------

#### Statistics:

GET http://localhost:8000/api/v1/movies/stats/

-------------------------------------------------

Para entrar em contato: tetigo@gmail.com
<br><br>





