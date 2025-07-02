# Diário do Humor - API Documentation

Esta API fornece os recursos de autenticação e manipulação de entradas de diário pessoal. Ela é utilizada por um frontend (Vue.js) para interações com o usuário. O backend é executado em Flask, e o ambiente pode ser iniciado completamente via Docker.

---

## 🔐 Autenticação (`/auth`)

### 📥 Registrar usuário

**Endpoint**: `POST /auth/register`

**Payload JSON**:

```json
{
  "name": "João",
  "email": "joao@email.com",
  "password": "123456"
}
```

**Respostas**:

- `201`: Usuário registrado com sucesso.
- `409`: Email já cadastrado.

---

### 🔑 Login

**Endpoint**: `POST /auth/login`

**Payload JSON**:

```json
{
  "email": "joao@email.com",
  "password": "123456"
}
```

**Resposta (200)**:

```json
{
  "access_token": "JWT_TOKEN"
}
```

---

## 📓 Entradas de Diário (`/diary`)

Todos os endpoints abaixo exigem o token JWT retornado no login, enviado no cabeçalho:

```
Authorization: Bearer <access_token>
```

### 🆕 Criar entrada

**Endpoint**: `POST /diary/`

**Payload JSON**:

```json
{
  "text": "Hoje me senti muito bem.",
  "mood": "feliz",
  "entry_date": "2024-06-10"
}
```

**Respostas**:

- `201`: Entrada criada com sucesso.
- `400`: Dados faltando ou formato inválido.
- `409`: Já existe entrada para esta data.

---

### 📄 Listar entradas

**Endpoint**: `GET /diary/`

**Resposta (200)**:

```json
[
  {
    "id": 1,
    "text": "Hoje me senti muito bem.",
    "mood": "feliz",
    "entry_date": "2024-06-10",
    "created_at": "2024-06-10T14:00:00"
  }
]
```

---

### ✏️ Atualizar entrada

**Endpoint**: `PUT /diary/<entry_id>`

**Payload JSON** (parcial ou completo):

```json
{
  "text": "Atualizei meu humor.",
  "mood": "motivado",
  "entry_date": "2024-06-11"
}
```

**Respostas**:

- `200`: Entrada atualizada.
- `404`: Entrada não encontrada.
- `409`: Já existe outra entrada nesta data.

---

### ❌ Excluir entrada

**Endpoint**: `DELETE /diary/<entry_id>`

**Resposta**:

- `200`: Entrada excluída com sucesso.
- `404`: Entrada não encontrada.

---

## ✅ Testes Locais via Docker

Após rodar `docker-compose up`, você poderá acessar:

- **Frontend**: [http://localhost:3000](http://localhost:3000)
- **Backend**: `http://localhost:5001`

Para testar os endpoints via Postman ou similar, use:

```
http://localhost:5001/auth/...
http://localhost:5001/diary/...
```

---

## 🐳 Observações

- Use o token JWT do login em todas as requisições protegidas.
- Certifique-se de que o banco de dados foi inicializado corretamente.

---

Feito com 💙 para a integração Vue.js + Flask.
