# 🐾 PetCenter API

API REST desenvolvida em Django para gerenciamento de:

-   Responsáveis
-   Pets
-   Vacinas
-   Vacinações

O projeto está totalmente containerizado com Docker, permitindo que
qualquer pessoa consiga executar sem precisar instalar Python ou
dependências manualmente.

------------------------------------------------------------------------

# 🚀 Tecnologias Utilizadas

-   Python 3.11
-   Django 5
-   Django REST Framework
-   SQLite
-   Docker
-   Docker Compose
-   JWT (SimpleJWT)

------------------------------------------------------------------------

# 📦 Como Baixar e Executar o Projeto (Passo a Passo Completo)

## ✅ 1️⃣ Instalar o Docker

Antes de tudo, você precisa instalar o Docker Desktop.

Download oficial: https://www.docker.com/products/docker-desktop/

Após instalar:

1.  Reinicie o computador (se solicitado).
2.  Abra o Docker Desktop.
3.  Aguarde até aparecer: "Docker Desktop is running".

Confirme no terminal:

docker --version docker compose version

Se aparecer a versão, está instalado corretamente.

------------------------------------------------------------------------

## ✅ 2️⃣ Clonar o Repositório

Abra o terminal (Git Bash, PowerShell ou CMD) e execute:

git clone https://github.com/RamonSSilva/Desafio-API.git

Depois entre na pasta do projeto:

cd Desafio-API/petcenter_api

Verifique se existem os arquivos:

-   Dockerfile
-   docker-compose.yml
-   manage.py

------------------------------------------------------------------------

## ✅ 3️⃣ Construir e Subir o Projeto

Dentro da pasta onde está o arquivo docker-compose.yml execute:

docker compose up --build

Na primeira execução pode demorar alguns minutos, pois o Docker irá:

-   Baixar a imagem do Python
-   Instalar dependencias
-   Criar o container
-   Iniciar o servidor Django

Quando aparecer:

Starting development server at http://0.0.0.0:8000/

O projeto está rodando.

------------------------------------------------------------------------

## ✅ 4️⃣ Acessar a Aplicação

Abra o navegador e acesse:

 Admin: http://127.0.0.1:8000/admin/
 
Rotas disponíveis no projeto:


-   Responsáveis: http://127.0.0.1:8000/api/responsaveis/

-   Pets: http://127.0.0.1:8000/api/pets/

-   Vacinas: http://127.0.0.1:8000/api/vacinas/

-   Vacinações: http://127.0.0.1:8000/api/vacinacoes/

------------------------------------------------------------------------

## ✅ 5️⃣ Rodar Migrations (Primeira Execução)

Se for a primeira vez executando:

docker compose exec web python manage.py migrate

------------------------------------------------------------------------

## ✅ 6️⃣ Criar Superusuário (Opcional)

Para acessar o painel administrativo:

docker compose exec web python manage.py createsuperuser

Depois acesse:

http://127.0.0.1:8000/admin/

------------------------------------------------------------------------

# 🔐 Autenticação JWT

Para obter um token de acesso:

POST http://127.0.0.1:8000/api/token/

Exemplo de envio no corpo da requisição:

{
    "username": "ramon.silva",
    "password": "masterkey"
}

A resposta retornará:

{ "refresh": "...", "access": "..." }

Para acessar rotas protegidas, utilize no Header:

Authorization: Bearer `<seu_token>`{=html}

------------------------------------------------------------------------

## 🛑 Parar o Projeto

Para encerrar o container:

docker compose down

------------------------------------------------------------------------

# 🧠 Estrutura do Projeto

O sistema permite:

-   Cadastro e gerenciamento de responsáveis
-   Associação de pets aos responsáveis
-   Cadastro de vacinas
-   Registro de vacinações
-   Consumo de dados via API REST
-   Autenticação com JWT

------------------------------------------------------------------------

# 📌 Observações Técnicas

-   Banco de dados utilizado: SQLite (arquivo local db.sqlite3).
-   Projeto containerizado para garantir padronização de ambiente.
-   Configurado para ambiente de desenvolvimento.
-   Pode ser facilmente adaptado para PostgreSQL em produção.

------------------------------------------------------------------------

# 👨‍💻 Autor

Ramon Simão Silva
