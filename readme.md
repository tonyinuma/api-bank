# Banking API

API bancaria simple desarrollada con FastAPI para practicar arquitectura backend y lógica de negocio.

## Stack

* Python 3.10+
* FastAPI
* Pydantic
* Uvicorn
* Pytest
* Ruff

## Setup

```bash
sudo apt update
sudo apt install python3-venv

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Ejecutar:

```bash
uvicorn app.main:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

## Estructura

```text
app/
├── api/
│   └── routes/
├── dependencies/
├── repositories/
├── schemas/
├── services/
└── main.py
```

Flujo:

```text
Route → Service → Repository
```

## Endpoints

```http
POST /api/v1/accounts
GET  /api/v1/accounts
GET  /api/v1/accounts/{id}

POST /api/v1/accounts/{id}/deposit
```

Próximamente:

```http
GET  /api/v1/accounts/{id}/balance
POST /api/v1/accounts/{id}/withdraw
POST /api/v1/transfers
GET  /api/v1/accounts/{id}/transactions
```

## Lógica de negocio

Una cuenta tiene:

```text
id
customer_name
currency
status
balance
```

Reglas principales:

* monedas permitidas: `PEN` y `USD`;
* una cuenta inicia con saldo `0.00`;
* una cuenta debe estar activa para operar;
* depósitos, retiros y transferencias deben ser mayores que `0`;
* no se puede retirar o transferir más dinero del disponible;
* una cuenta no puede transferirse dinero a sí misma;
* los valores monetarios usan `Decimal`.

## Ejemplo

Crear cuenta:

```json
{
  "customer_name": "Tony Inuma",
  "currency": "PEN"
}
```

Depositar:

```json
{
  "amount": "500.00"
}
```

## Pendiente

```text
[ ] Withdrawals
[ ] Transfers
[ ] Transactions
[ ] PostgreSQL
[ ] SQLAlchemy
[ ] Alembic
[ ] Tests
[ ] Docker
```
