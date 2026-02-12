# 🐾 PetCenter API

API REST desenvolvida em **Django** para gerenciamento de pets,
responsáveis, vacinas e registros de vacinação.

O projeto foi construído seguindo boas práticas de organização,
separação por responsabilidades e padrões RESTful.

------------------------------------------------------------------------

# 📌 Objetivo

Disponibilizar uma API capaz de:

-   Gerenciar responsáveis
-   Gerenciar pets vinculados aos responsáveis
-   Gerenciar vacinas
-   Registrar vacinações
-   Proteger o acesso via autenticação JWT
-   Retornar dados em formato JSON

------------------------------------------------------------------------

# 🛠 Tecnologias Utilizadas

-   Python 3.11+
-   Django 5+
-   Django REST Framework
-   Simple JWT (Autenticação)
-   SQLite (Banco de dados relacional)

------------------------------------------------------------------------

# 🏗 Arquitetura do Projeto

O sistema foi organizado em múltiplas aplicações Django, seguindo o
princípio de separação de responsabilidades:

    petcenter_api/
    │
    ├── accounts/        # Responsáveis
    ├── pets/            # Pets
    ├── vaccines/        # Vacinas
    ├── vaccination/     # Registro de vacinações
    ├── petcenter_api/   # Configurações do projeto
    ├── manage.py
    └── requirements.txt

Foram utilizados:

-   ModelViewSet para CRUD automático
-   DefaultRouter para roteamento REST
-   Autenticação global via JWT
-   Banco relacional com Foreign Keys

------------------------------------------------------------------------

# 🚀 Como Executar o Projeto

## 1️⃣ Clonar o repositório

``` bash
git clone https://github.com/RamonSSilva/Desafio-API.git
cd Desafio-API
```

## 2️⃣ Criar e ativar ambiente virtual

``` bash
python -m venv petcenter
```

### Windows:

``` bash
petcenter\Scripts\activate
```

### Linux/Mac:

``` bash
source petcenter/bin/activate
```

## 3️⃣ Instalar dependências

``` bash
pip install -r requirements.txt
```

## 4️⃣ Aplicar migrações

``` bash
python manage.py migrate
```

## 5️⃣ Criar usuário administrador

``` bash
python manage.py createsuperuser
```

## 6️⃣ Executar servidor

``` bash
python manage.py runserver
```

A API estará disponível em:

http://127.0.0.1:8000/

------------------------------------------------------------------------

# 🔐 Autenticação

A API utiliza **JWT (JSON Web Token)**.

## Gerar Token

Endpoint:

POST /api/token/

Body:

``` json
{
    "username": "seu_usuario",
    "password": "sua_senha"
}
```

O retorno conterá:

-   access → utilizado nas requisições
-   refresh → utilizado para renovar o access token

## Utilizar Token

Adicionar no Header das requisições:

Authorization: Bearer SEU_ACCESS_TOKEN

Todas as rotas exigem autenticação.

------------------------------------------------------------------------

# 📡 Endpoints Disponíveis

## 🔹 Responsáveis

-   GET /api/responsaveis/
-   POST /api/responsaveis/
-   GET /api/responsaveis/{id}/
-   PUT /api/responsaveis/{id}/
-   DELETE /api/responsaveis/{id}/

## 🔹 Pets

-   GET /api/pets/
-   POST /api/pets/
-   GET /api/pets/{id}/
-   PUT /api/pets/{id}/
-   DELETE /api/pets/{id}/

Relacionamento: Cada pet pertence a um responsável.

## 🔹 Vacinas

-   GET /api/vacinas/
-   POST /api/vacinas/
-   GET /api/vacinas/{id}/
-   PUT /api/vacinas/{id}/
-   DELETE /api/vacinas/{id}/

Campos principais: - nome - descricao - fabricante - periodicidade_meses

## 🔹 Vacinações

-   GET /api/vacinacoes/
-   POST /api/vacinacoes/
-   GET /api/vacinacoes/{id}/
-   PUT /api/vacinacoes/{id}/
-   DELETE /api/vacinacoes/{id}/

Relacionamentos: - Pet - Vacina - Data de aplicação - Próxima dose

------------------------------------------------------------------------

# 🧠 Decisões Técnicas

-   Utilização de ModelViewSet para reduzir código repetitivo e manter
    padrão REST.
-   Separação do projeto em apps para melhor organização e
    escalabilidade.
-   Implementação de autenticação JWT como padrão de mercado.
-   Uso de banco relacional com integridade referencial via Foreign
    Keys.
-   Respostas padronizadas em JSON conforme boas práticas RESTful.

------------------------------------------------------------------------

# ✅ Status

✔ CRUD completo\
✔ Relacionamentos implementados\
✔ Autenticação JWT\
✔ API REST protegida\
✔ Banco relacional\
✔ Requisitos técnicos atendidos
