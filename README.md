
# 📚 Documentação da API – Diário de Humor

Todas as rotas do diário exigem autenticação via JWT:

```
Authorization: Bearer <token>
```

> Use um token JWT fictício para testes.

---

## 1. Criar nova entrada do diário

**Endpoint:**  
`POST /diary/`

**Request:**

```json
{
  "text": "Dia de estudo intenso para a faculdade!",
  "mood": "focado",
  "entry_date": "2024-06-12"
}
```

**Response (201 Created):**

```json
{
  "message": "Entrada criada com sucesso."
}
```

**Erros possíveis:**

- `400 Bad Request`: Campos obrigatórios faltando ou data inválida
- `409 Conflict`: Já existe entrada para essa data

---

## 2. Listar todas as entradas do usuário

**Endpoint:**  
`GET /diary/`

**Request:**  
Apenas o header `Authorization`.

**Response (200 OK):**

```json
[
  {
    "id": 1,
    "text": "Dia de estudo intenso para a faculdade!",
    "mood": "focado",
    "entry_date": "2024-06-12",
    "created_at": "2024-06-12T10:24:13.000Z"
  },
  {
    "id": 2,
    "text": "Fui ao parque e relaxei.",
    "mood": "tranquilo",
    "entry_date": "2024-06-11",
    "created_at": "2024-06-11T14:00:01.000Z"
  }
]
```

---

## 3. Editar uma entrada do diário

**Endpoint:**  
`PUT /diary/<entry_id>`

**Request:**

```json
{
  "text": "Atualizei meu dia!",
  "mood": "animado",
  "entry_date": "2024-06-12"
}
```

**Response (200 OK):**

```json
{
  "message": "Entrada atualizada com sucesso."
}
```

**Erros possíveis:**

- `404 Not Found`: Entrada não encontrada
- `409 Conflict`: Já existe outra entrada nesta data

---

## 4. Excluir uma entrada do diário

**Endpoint:**  
`DELETE /diary/<entry_id>`

**Request:**  
Apenas o header `Authorization`.

**Response (200 OK):**

```json
{
  "message": "Entrada excluída com sucesso."
}
```

**Erros possíveis:**

- `404 Not Found`: Entrada não encontrada

---

## Resumo dos endpoints

| Método | Rota                | Descrição                 |
|--------|---------------------|---------------------------|
| POST   | `/diary/`           | Cria nova entrada         |
| GET    | `/diary/`           | Lista todas as entradas   |
| PUT    | `/diary/<entry_id>` | Edita uma entrada         |
| DELETE | `/diary/<entry_id>` | Exclui uma entrada        |

---

### Fluxo sugerido para testes no frontend

1. **Login fictício**: gere ou use um JWT fake.
2. **Criar entrada**: simule o retorno conforme exemplos.
3. **Listar entradas**: use um array mock igual ao exemplo.
4. **Editar** e **excluir**: simule os retornos conforme acima.

---
