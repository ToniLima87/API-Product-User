# 🚀 FastAPI Products & Users API

API REST desenvolvida com **FastAPI**, **PostgreSQL**, **Docker** e **SQLAlchemy** para gerenciamento de usuários e produtos.

Este projeto foi criado com foco em boas práticas de backend, arquitetura limpa e ambiente pronto para produção.

---

## 📌 Tecnologias Utilizadas

* **Python 3.11**
* **FastAPI**
* **PostgreSQL**
* **SQLAlchemy**
* **Pydantic**
* **Docker & Docker Compose**
* **Uvicorn**
* **Passlib (bcrypt)**

---

## 🏗️ Arquitetura do Projeto

```
app/
│
├── main.py        # Rotas da aplicação
├── database.py    # Conexão com banco
├── models.py      # Modelos SQLAlchemy
├── schemas.py     # Schemas Pydantic
└── crud.py        # Regras de negócio (CRUD)
```

Fluxo da aplicação:

```
Request → Schema → CRUD → Model → Database
```

---

## ⚙️ Como executar o projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/NOME-REPO.git
cd NOME-REPO
```

---

### 2️⃣ Subir containers Docker

```bash
docker compose up --build
```

---

### 3️⃣ Acessar a API

API:

```
http://localhost:8000
```

Documentação interativa (Swagger):

```
http://localhost:8000/docs
```

---

## 🗄️ Banco de Dados

* Banco: **PostgreSQL**
* Porta padrão: **5432**
* Tabelas criadas automaticamente via:

```python
Base.metadata.create_all(bind=engine)
```

---

## 👤 Endpoints de Usuário

### Criar usuário

**POST** `/users/`

#### Request

```json
{
  "name": "Antonio",
  "email": "antonio@email.com",
  "password": "123456"
}
```

#### Response

```json
{
  "id": 1,
  "name": "Antonio",
  "email": "antonio@email.com"
}
```

> 🔒 A senha é armazenada criptografada (bcrypt).

---

## 📦 Endpoints de Produtos

### Criar produto

**POST** `/products`

```json
{
  "name": "Notebook",
  "price": 3500
}
```

---

### Listar produtos

**GET** `/products`

---

### Buscar produto por ID

**GET** `/products/{id}`

---

### Atualizar produto

**PUT** `/products/{id}`

---

### Deletar produto

**DELETE** `/products/{id}`

---

## ✅ Validações

* Validação automática via **Pydantic**
* Tipagem forte
* Email validado automaticamente
* Serialização segura de respostas

---

## 🔐 Segurança

* Senhas criptografadas com **bcrypt**
* Separação entre schemas de entrada e saída
* ORM evita SQL Injection

---

## 🧪 Testes da API

A API pode ser testada via:

* Swagger UI (`/docs`)
* Insomnia
* Postman
* curl

---

## 📈 Melhorias Futuras

* [ ] Autenticação JWT
* [ ] Rotas protegidas
* [ ] Paginação
* [ ] Testes automatizados
* [ ] CI/CD
* [ ] Deploy em AWS

---

## 👨‍💻 Autor

Desenvolvido por **Antonio Lima**

---

## 📄 Licença

Este projeto está sob licença MIT.
