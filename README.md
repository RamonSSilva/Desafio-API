#  Sistema de Vacinação de Pets - API REST

API REST desenvolvida em Django para controle de vacinação de pets.

Este projeto foi desenvolvido como parte de um desafio técnico, com foco em modelagem de dados, arquitetura e boas práticas de desenvolvimento.

---

## 📌 Visão Geral

O sistema permite:

- Cadastro de responsáveis (tutores)
- Cadastro de pets
- Cadastro de vacinas
- Registro de vacinações
- Relacionamento entre pets e seus responsáveis
- Controle do histórico de vacinação

---

## 🛠 Tecnologias Utilizadas

- Python 3.11
- Django 5.2
- Django Rest Framework
- SQLite (banco padrão do Django)
- JWT (autenticação)

---

## 🧱 Arquitetura

O projeto segue uma arquitetura baseada em separação por domínio (apps Django):

- `accounts` → Responsáveis
- `pets` → Pets
- `vaccines` → Vacinas
- `vaccination` → Registros de Vacinação

Organização em camadas:

- Models → Modelagem de dados
- Serializers → Conversão para JSON
- Views → Lógica da API
- URLs → Rotas

---

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
cd desafio-api
