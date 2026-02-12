# 🐾 PetCenter API

API REST desenvolvida em Django para gerenciamento de: - Responsáveis -
Pets - Vacinas - Vacinações

Projeto containerizado com Docker para garantir padronização de ambiente
e facilidade de execução.

------------------------------------------------------------------------

# 🚀 Tecnologias Utilizadas

-   Python 3.11
-   Django 5
-   Django REST Framework
-   SQLite
-   Docker
-   Docker Compose

------------------------------------------------------------------------

# 📦 Como Executar o Projeto com Docker

## ✅ 1. Pré-requisitos

Antes de começar, você precisa ter instalado:

-   Docker Desktop (Windows/Mac)\
    Download: https://www.docker.com/products/docker-desktop/

Após instalar, confirme no terminal:

docker --version docker compose version

------------------------------------------------------------------------

## ✅ 2. Clonar o Repositório

git clone https://github.com/RamonSSilva/Desafio-API.git cd
Desafio-API/petcenter_api

------------------------------------------------------------------------

## ✅ 3. Subir o Projeto

Dentro da pasta onde está o arquivo `docker-compose.yml`, execute:

docker compose up --build

Na primeira execução pode demorar alguns minutos.

Se tudo estiver correto, você verá:

Starting development server at http://0.0.0.0:8000/

------------------------------------------------------------------------

## ✅ 4. Acessar a Aplicação

Abra no navegador:

http://127.0.0.1:8000/

Rotas principais:

-   Admin: http://127.0.0.1:8000/admin/
-   Responsáveis: http://127.0.0.1:8000/api/responsaveis/
-   Pets: http://127.0.0.1:8000/api/pets/
-   Vacinas: http://127.0.0.1:8000/api/vacinas/

------------------------------------------------------------------------

## ✅ 5. Rodar Migrations (se necessário)

Se for a primeira execução:

docker compose exec web python manage.py migrate

------------------------------------------------------------------------

## ✅ 6. Criar Superusuário

docker compose exec web python manage.py createsuperuser

------------------------------------------------------------------------

## 🛑 Parar o Projeto

docker compose down

------------------------------------------------------------------------

# 🔐 Autenticação

A API utiliza autenticação JWT.

Para obter o token:

POST /api/token/

Depois utilize no Header:

Authorization: Bearer `<seu_token>`{=html}

------------------------------------------------------------------------

# 🧠 Decisões Técnicas

-   Utilização de Django REST Framework para construção da API.
-   Uso de SQLite para simplicidade e adequação ao escopo do desafio.
-   Containerização com Docker para padronização e portabilidade.
-   Estrutura organizada em apps para separação de responsabilidades.

------------------------------------------------------------------------

# 📌 Observação

Atualmente o projeto está configurado para ambiente de desenvolvimento.
Para produção recomenda-se:

-   Utilizar PostgreSQL
-   Utilizar Gunicorn
-   Configurar variáveis de ambiente
-   Implementar servidor reverso (Nginx)

------------------------------------------------------------------------

# 👨‍💻 Autor

Ramon Simão Silva
