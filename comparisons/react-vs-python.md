# Comparações: React/JavaScript vs Python

Este documento contém comparações detalhadas entre conceitos React/JavaScript e Python.

## 📋 Índice

1. [Estruturas de Dados](#estruturas-de-dados)
2. [Funções e Métodos](#funções-e-métodos)
3. [Async/Await](#asyncawait)
4. [Classes e Componentes](#classes-e-componentes)
5. [API e HTTP](#api-e-http)
6. [Estado e Gerenciamento](#estado-e-gerenciamento)
7. [Validação de Dados](#validação-de-dados)

---

## 1. Estruturas de Dados

### Arrays → Lists

**JavaScript:**
```javascript
const fruits = ["apple", "banana"];
fruits.push("orange");
fruits.pop();
fruits.map(f => f.toUpperCase());
fruits.filter(f => f.length > 5);
```

**Python:**
```python
fruits = ["apple", "banana"]
fruits.append("orange")  # push
fruits.pop()  # pop
[f.upper() for f in fruits]  # map
[f for f in fruits if len(f) > 5]  # filter
```

### Objects → Dictionaries

**JavaScript:**
```javascript
const user = { name: "João", age: 30 };
user.name;  // ou user["name"]
user.city = "SP";
```

**Python:**
```python
user = {"name": "João", "age": 30}
user["name"]  # SEMPRE colchetes!
user.get("name", "Default")  # Com padrão
user["city"] = "SP"
```

---

## 2. Funções e Métodos

### Funções Básicas

**JavaScript:**
```javascript
function greet(name) {
    return `Hello, ${name}!`;
}

const greetArrow = (name) => {
    return `Hello, ${name}!`;
};
```

**Python:**
```python
def greet(name):
    return f"Hello, {name}!"

# Lambda (similar a arrow function, mas limitado)
greet_lambda = lambda name: f"Hello, {name}!"
```

### Higher-Order Functions

**JavaScript:**
```javascript
const numbers = [1, 2, 3];
const doubled = numbers.map(n => n * 2);
const evens = numbers.filter(n => n % 2 === 0);
const sum = numbers.reduce((acc, n) => acc + n, 0);
```

**Python:**
```python
numbers = [1, 2, 3]
doubled = [n * 2 for n in numbers]  # map
evens = [n for n in numbers if n % 2 == 0]  # filter
total = sum(numbers)  # reduce (mais simples)
```

---

## 3. Async/Await

### Promise → Coroutine

**JavaScript:**
```javascript
async function fetchUser(id) {
    const response = await fetch(`/api/users/${id}`);
    const user = await response.json();
    return user;
}

// Múltiplas promises
const [user1, user2] = await Promise.all([
    fetchUser(1),
    fetchUser(2)
]);
```

**Python:**
```python
import httpx

async def fetch_user(id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"/api/users/{id}")
        return response.json()

# Múltiplas coroutines
import asyncio

user1, user2 = await asyncio.gather(
    fetch_user(1),
    fetch_user(2)
)
```

---

## 4. Classes e Componentes

### React Component → Python Class

**React:**
```typescript
interface UserProps {
    name: string;
    age: number;
}

function UserComponent({ name, age }: UserProps) {
    const [likes, setLikes] = useState(0);
    
    return (
        <div>
            <h1>{name}</h1>
            <button onClick={() => setLikes(likes + 1)}>
                Likes: {likes}
            </button>
        </div>
    );
}
```

**Python Class (similar, mas conceito diferente):**
```python
from pydantic import BaseModel

class UserProps(BaseModel):
    name: str
    age: int

class UserComponent:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.likes = 0
    
    def increment_likes(self):
        self.likes += 1
    
    def render(self):
        return f"<div><h1>{self.name}</h1></div>"
```

**Nota:** Python classes não são exatamente como React components. Em Python backend, você usa classes para organizar lógica, não UI.

---

## 5. API e HTTP

### Fetch → httpx

**JavaScript:**
```javascript
// GET
const response = await fetch('/api/users');
const users = await response.json();

// POST
const newUser = await fetch('/api/users', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name: 'João', age: 30 })
});
```

**Python:**
```python
import httpx

# GET
async with httpx.AsyncClient() as client:
    response = await client.get('/api/users')
    users = response.json()

# POST
async with httpx.AsyncClient() as client:
    new_user = await client.post(
        '/api/users',
        json={"name": "João", "age": 30}
    )
```

### Express Routes → FastAPI Routes

**Express.js:**
```javascript
const express = require('express');
const router = express.Router();

router.get('/users', async (req, res) => {
    const users = await getUsers();
    res.json(users);
});

router.post('/users', async (req, res) => {
    const user = await createUser(req.body);
    res.status(201).json(user);
});
```

**FastAPI:**
```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
async def get_users():
    users = await get_users()
    return users

@router.post("/users")
async def create_user(user: UserCreate):
    new_user = await create_user(user)
    return new_user  # Status 201 automático com status_code=201
```

---

## 6. Estado e Gerenciamento

### useState → Service State

**React:**
```typescript
function UserList() {
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(false);
    
    useEffect(() => {
        setLoading(true);
        fetchUsers().then(data => {
            setUsers(data);
            setLoading(false);
        });
    }, []);
    
    return <div>{users.map(...)}</div>;
}
```

**Python Service:**
```python
class UserService:
    def __init__(self):
        self.users = []
        self.loading = False
    
    async def load_users(self):
        self.loading = True
        self.users = await fetch_users()
        self.loading = False
```

**Nota:** Em Python backend, estado geralmente está no banco de dados, não em memória como no React.

---

## 7. Validação de Dados

### Zod → Pydantic

**TypeScript/Zod:**
```typescript
import { z } from 'zod';

const UserSchema = z.object({
    name: z.string().min(2),
    email: z.string().email(),
    age: z.number().min(18)
});

// Validação manual
try {
    const user = UserSchema.parse(data);
} catch (error) {
    // erro de validação
}
```

**Python/Pydantic:**
```python
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    age: int = Field(..., ge=18)

# Validação automática no FastAPI
@router.post("/users")
def create_user(user: User):  # Validação automática!
    return user
```

**Vantagem do Pydantic:** Validação automática no FastAPI, não precisa try/catch manual!

---

## 📝 Resumo Rápido

| Conceito | JavaScript/React | Python |
|----------|-----------------|--------|
| Arrays | `[]` | `[]` (list) |
| Objects | `{}` | `{}` (dict) |
| Funções | `function` ou `=>` | `def` ou `lambda` |
| Async | `async/await` | `async/await` |
| Classes | Componentes | Classes de lógica |
| Validação | Zod manual | Pydantic automático |
| HTTP Client | `fetch` | `httpx` |
| API Framework | Express | FastAPI |

---

## 🎯 Próximos Passos

1. Pratique os conceitos comparados
2. Veja exemplos práticos nos módulos
3. Faça os exercícios
4. Construa um projeto real

