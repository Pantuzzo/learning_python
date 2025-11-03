# Módulo 05: FastAPI Basics

FastAPI é um framework web moderno para Python, similar ao Express.js no Node.js. É perfeito para criar APIs REST.

## 📋 Índice

1. [FastAPI vs Express.js](#fastapi-vs-expressjs)
2. [Primeira API](#primeira-api)
3. [Routes e Decorators](#routes-e-decorators)
4. [Request/Response Models](#requestresponse-models)
5. [Dependency Injection](#dependency-injection)

---

## 1. FastAPI vs Express.js

### Comparação Rápida

| Express.js (Node.js) | FastAPI (Python) | Conceito |
|---------------------|------------------|----------|
| `app.get('/path')` | `@router.get('/path')` | Roteamento |
| `req.body` | `body: Model` | Request body |
| `res.json()` | `return model` | Response |
| Middleware | Dependencies | Middleware/DI |
| `app.listen(3000)` | `uvicorn.run()` | Servidor |

---

## 2. Primeira API

### Express.js
```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.json({ message: 'Hello World!' });
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
```

### FastAPI
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

# Para rodar: uvicorn main:app --reload
```

**Diferenças principais:**
- FastAPI usa **decorators** (`@app.get`) em vez de métodos (`app.get`)
- Retorno direto (não precisa `res.json()`)
- Documentação automática em `/docs`

---

## 3. Routes e Decorators

### Criando Rotas

**Express.js:**
```javascript
// routes/users.js
const router = express.Router();

router.get('/', (req, res) => {
    res.json({ users: [] });
});

router.post('/', (req, res) => {
    const user = req.body;
    res.json({ created: user });
});
```

**FastAPI:**
```python
# routes/users.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_users():
    return {"users": []}

@router.post("/")
def create_user(user: UserModel):
    return {"created": user}
```

### Incluir Rotas

**Express.js:**
```javascript
app.use('/api/users', router);
```

**FastAPI:**
```python
app.include_router(router, prefix="/api/users", tags=["users"])
```

---

## 4. Request/Response Models

### Com Pydantic (similar ao Zod)

**Express.js (com Zod):**
```javascript
const { z } = require('zod');

const UserSchema = z.object({
    name: z.string(),
    email: z.string().email(),
    age: z.number().min(18)
});

app.post('/users', (req, res) => {
    try {
        const user = UserSchema.parse(req.body);
        res.json({ created: user });
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});
```

**FastAPI (com Pydantic):**
```python
from pydantic import BaseModel, EmailStr
from fastapi import HTTPException

class User(BaseModel):
    name: str
    email: EmailStr
    age: int
    
    @field_validator('age')
    @classmethod
    def validate_age(cls, v):
        if v < 18:
            raise ValueError('Age must be 18 or older')
        return v

@app.post("/users")
def create_user(user: User):
    # Validação automática! Se inválido, retorna 422
    return {"created": user}
```

**Vantagens do FastAPI:**
- ✅ Validação automática (não precisa try/catch manual)
- ✅ Documentação automática no Swagger
- ✅ Type hints integradas

---

## 5. Dependency Injection

### Express.js (sem DI nativo, usa middlewares)
```javascript
// middleware/auth.js
const authenticate = (req, res, next) => {
    const token = req.headers.authorization;
    if (!token) {
        return res.status(401).json({ error: 'Unauthorized' });
    }
    req.user = { id: 1, name: 'João' };
    next();
};

app.get('/profile', authenticate, (req, res) => {
    res.json({ user: req.user });
});
```

### FastAPI (Dependency Injection)
```python
from fastapi import Depends, HTTPException, Header

def get_current_user(authorization: str = Header()):
    if not authorization:
        raise HTTPException(401, "Unauthorized")
    return {"id": 1, "name": "João"}

@app.get("/profile")
def get_profile(user: dict = Depends(get_current_user)):
    return {"user": user}
```

**Vantagens:**
- ✅ Type-safe dependencies
- ✅ Fácil de testar (mock dependencies)
- ✅ Reutilizável (similar a Custom Hooks no React)

---

## 📝 Exemplo Completo

Veja `main.py` para um exemplo completo funcionando!

---

## 🎯 Próximos Passos

1. Execute `main.py`
2. Acesse `http://localhost:8000/docs` para ver a documentação automática
3. Teste os endpoints
4. Avance para o Módulo 06: API Project Completo

