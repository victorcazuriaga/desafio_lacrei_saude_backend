# Lacrei Saúde


## Índice

- [Visão Geral](#visão-geral)
- [Requisitos](#requisitos)
- [Tecnologias](#tecnologias-utilizadas)
- [Configuração do Ambiente Virtual](#configuração-do-ambiente-virtual)
- [Configuração de Variáveis de ambiente ](#configuração-de-variáveis-de-ambiente)
- [Instalação das Dependências](#instalação-das-dependências)
- [Executando o Projeto](#executando-o-projeto)
- [Executando com Docker](#executando-com-docker)
- [Testes](#testes)
- [Uso](#uso)
- [Licença](#licença)


## Visão Geral
Esta é uma API de gerenciamento de clínica que permite cadastrar pacientes, médicos e agendar consultas com data e hora. Ela oferece funcionalidades para facilitar o gerenciamento de uma clínica médica, permitindo o registro e a consulta de informações

## Tecnologias Utilizadas
A API foi desenvolvida utilizando as seguintes tecnologias:

- Linguagem de Programação: [Python]
- Framework: [Django]
- Banco de Dados: [Postgres, SQLite]
- Outras Bibliotecas: [Django Rest Framework, DRF-Spectacular, Django Filter, Django Rest Auth, Ipdb, Gunicorn, Python-dotenv, Dj-database-url]



## Requisitos

- Python (versão 3.10.X)
- Docker (versão 23.0.X)
- Docker Compose (versão 2.17.X)
- Postgres (versão 15.X.X)



## Configuração do Ambiente Virtual
É recomendado utilizar um ambiente virtual para isolar as dependências do projeto. Siga os passos abaixo para criar e ativar um ambiente virtual:

1. No diretório raiz do projeto, crie um ambiente virtual:

```
python -m venv myvenv
```
2. Ative o ambiente virtual:

* Windows:
```
myvenv\Scripts\activate
```
* macOS/Linux:
```
source myvenv/bin/activate
```
## Configuração de Variáveis de ambiente
1. crie na raiz do projeto o arquivo .env

2. preencha a .env de acordo com .env.example
   
```
SECRET_KEY={insira uma secret_key}
POSTGRES_DB={nome banco de dados}
POSTGRES_USER={usuário do banco de dados}
POSTGRES_PASSWORD={senha do banco de dados}
POSTGRES_HOST={endereço do banco de dados}
POSTGRES_PORT={porta do banco de dados }

```
** Observação: caso utilize docker compose para executar o projeto, insira POSTGRES_HOST='db'.

## Instalação das Dependências
Para instalar as dependências do projeto, execute o seguinte comando:

```
pip install -r requirements.txt

```

## Executando o Projeto
Siga os passos abaixo para executar o projeto:

1. Gerar as migrações
```
python manage.py makemigrations
```

2. Execute as migrações do banco de dados:

```
python manage.py migrate
```
2. Inicie o servidor de desenvolvimento:
```
python manage.py runserver
```

O servidor estará disponível em http://localhost:8000.

## Executando com Docker
Siga os passos abaixo para executar o projeto utilizando o Docker:

1. Execute o comando para construir as imagens e iniciar os containers:

```
docker compose up
```
Isso irá construir as imagens e iniciar os containers necessários para o projeto.

2. O servidor estará disponível em http://localhost:8000.

## Testes
Para executar os testes do projeto, utilize o seguinte comando:
```
python manage.py test
```
## Uso
1. Necessário criar usuário
```
Method POST: localhost:8000/api/register
payload example:
{"username": "seu_usuario", password"sua_senha"}

```
2. Realizar login e autenticação

 ```
Method POST: localhost:8000/api/login
payload example:
{"username": "seu_usuario", password"sua_senha"}

response example:
{"token": "seu_token"}

```
3. Consultar a documentação
```
localhost:8000/api/docs/redoc/
```



## Licença
[MIT License](LICENSE)

[Linkedin](https://www.linkedin.com/in/victorcazuriaga/)
