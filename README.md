# 🌍 travel\_planner\_api

API Django para planejamento de viagens, com funcionalidades de autenticação de usuários, gerenciamento de planos de viagem, conversão de moedas e busca de informações de localização.

-----

## 📌 Funcionalidades

✅ **Autenticação de Usuários com JWT:** Cadastro, login, visualização de perfil e exclusão de conta.  

✅ **Gerenciamento de Planos de Viagem (CRUD):** Criação, listagem, detalhamento, atualização e exclusão de planos de viagem.  

✅ **Consulta de Endereço via CEP:** Integração com [ViaCEP](https://viacep.com.br/) para auto-preenchimento de dados de localização.  

✅ **Consulta de Cotações de Moedas:** Integração com [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas) para obter cotações de moedas em relação ao Real Brasileiro (BRL).  

✅ **API Interna de Gerenciamento de Países e Moedas:** Permite o CRUD de registros de países e seus respectivos códigos ISO de moedas (ex: EUR, USD, BRL).  
 

-----
## 🛠️ Tecnologias utilizadas

  - Python  
  - Django  
  - Django REST Framework  
  - SQLite (para desenvolvimento local)   
  - VS Code  

-----

## 🚀 Como rodar o projeto

### 1\. Clone o repositório

```bash
git clone https://github.com/seu-usuario/travel_planner_api.git
cd travel_planner_api
```

### 2\. Crie e ative um ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# Ou no Linux/macOS:
# source venv/bin/activate
```

### 3\. Instale as dependências

```bash
pip install -r requirements.txt
```


### 4\. Execute as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5\. Crie um superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 6\. Inicie o servidor

```bash
python manage.py runserver
```

## 📡 Principais Endpoints

Aqui estão os principais endpoints disponíveis na API, com descrições e requisitos de autenticação. Para endpoints que requerem autenticação, inclua o token JWT no cabeçalho `Authorization: Bearer <seu_token_de_acesso_jwt>`.

### Autenticação (`/api/auth/`)

  * **`POST /api/auth/signup/`**
      * **Descrição:** Registra um novo usuário no sistema.
      * **Permissão:** Livre (Não requer autenticação)
  * **`POST /api/auth/login/`**
      * **Descrição:** Realiza o login de um usuário existente e retorna os tokens JWT (`access` e `refresh`).
      * **Permissão:** Livre (Não requer autenticação)
  * **`GET /api/auth/me/`**
      * **Descrição:** Retorna os dados do perfil do usuário autenticado.
      * **Permissão:** Requer autenticação
  * **`DELETE /api/auth/delete/`**
      * **Descrição:** Exclui a conta do usuário autenticado. Requer a senha do usuário para confirmação.
      * **Permissão:** Requer autenticação

### Planos de Viagem (`/api/trip-plans/`)

  * **`GET /api/trip-plans/`**
      * **Descrição:** Lista todos os planos de viagem pertencentes ao usuário autenticado.
      * **Permissão:** Requer autenticação
  * **`POST /api/trip-plans/`**
      * **Descrição:** Cria um novo plano de viagem. Automaticamente busca informações de endereço via CEP e cotação de moeda para o destino.
      * **Parâmetros de Requisição (JSON):** `cep_origem`, `data_ida`, `orcamento`, `destino`.
      * **Permissão:** Requer autenticação
  * **`GET /api/trip-plans/{id}/`**
      * **Descrição:** Retorna os detalhes de um plano de viagem específico pelo seu `id` (UUID).
      * **Permissão:** Requer autenticação
  * **`PUT /api/trip-plans/{id}/`**
      * **Descrição:** Atualiza *completamente* um plano de viagem existente pelo seu `id`.
      * **Permissão:** Requer autenticação
  * **`PATCH /api/trip-plans/{id}/`**
      * **Descrição:** Atualiza *parcialmente* um plano de viagem existente pelo seu `id`.
      * **Permissão:** Requer autenticação
  * **`DELETE /api/trip-plans/{id}/`**
      * **Descrição:** Exclui um plano de viagem pelo seu `id`.
      * **Permissão:** Requer autenticação

##

## 🧑‍💻 Autor

Desenvolvido por **Lucas Ferreira** — estudante de Ciência da Computação  
[LinkedIn](https://linkedin.com/in/lucas-ferreira-051723270/)

-----