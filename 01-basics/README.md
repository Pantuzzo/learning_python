# Módulo 01: Basics - Python para React Developers

Este módulo ensina os fundamentos de Python comparando com JavaScript que você já conhece.

## 📋 Índice

1. [Variáveis e Tipos](#variáveis-e-tipos)
2. [Estruturas de Dados](#estruturas-de-dados)
3. [Funções](#funções)
4. [List Comprehensions](#list-comprehensions)
5. [Type Hints](#type-hints)

---

## 1. Variáveis e Tipos

### JavaScript → Python

**JavaScript:**
```javascript
// Tipos dinâmicos
let name = "João";
let age = 30;
let isActive = true;
let data = null;
let user = undefined;
```

**Python:**
```python
# Tipos dinâmicos (similar ao JavaScript)
name = "João"          # str (string)
age = 30               # int (integer)
is_active = True       # bool (boolean) - Note: True/False com maiúscula!
data = None            # NoneType (equivalente a null/undefined)
# Python não tem undefined separado, usa None
```

### Diferenças Importantes:

1. **Nomenclatura**: Python usa `snake_case` (não `camelCase`)
2. **Booleanos**: `True`/`False` com maiúscula (não `true`/`false`)
3. **Null/Undefined**: Python só tem `None`
4. **Ponto e vírgula**: Não são necessários em Python

### Exemplo Prático

**JavaScript (React):**
```javascript
const [count, setCount] = useState(0);
const userName = "React Dev";
const items = [];
```

**Python:**
```python
count = 0
user_name = "React Dev"
items = []
```

---

## 2. Estruturas de Dados

### Arrays → Lists

**JavaScript:**
```javascript
const fruits = ["apple", "banana", "orange"];
fruits.push("grape");        // Adiciona
fruits.pop();                // Remove último
fruits.map(f => f.toUpperCase()); // Transforma
```

**Python:**
```python
fruits = ["apple", "banana", "orange"]
fruits.append("grape")                    # Adiciona (similar a push)
fruits.pop()                              # Remove último (igual)
[f.upper() for f in fruits]               # Transforma (ver List Comprehensions)
```

### Objects → Dictionaries

**JavaScript:**
```javascript
const user = {
  name: "João",
  age: 30,
  email: "joao@email.com"
};

user.name              // Acesso
user["name"]           // Acesso alternativo
user.city = "SP"        // Adiciona propriedade
```

**Python:**
```python
user = {
    "name": "João",
    "age": 30,
    "email": "joao@email.com"
}

user["name"]                    # Acesso (sempre com colchetes!)
user.get("name", "Default")     # Com valor padrão
user["city"] = "SP"             # Adiciona propriedade
```

**IMPORTANTE**: Em Python, você sempre usa colchetes `[]` para acessar dicionários, não ponto `.`

### Tuples (Imutáveis)

**Python tem algo que JavaScript não tem - Tuples (listas imutáveis):**

```python
# Tuple (imutável, similar a const array, mas não é array)
point = (10, 20)
point[0]  # 10
# point[0] = 30  # ERRO! Tuples são imutáveis

# Útil para retornar múltiplos valores
def get_user():
    return ("João", 30, "joao@email.com")

name, age, email = get_user()  # Desempacotamento
```

---

## 3. Funções

### Funções Básicas

**JavaScript:**
```javascript
function greet(name) {
    return `Hello, ${name}!`;
}

const greetArrow = (name) => {
    return `Hello, ${name}!`;
};

// Arrow function simplificada
const add = (a, b) => a + b;
```

**Python:**
```python
def greet(name):
    return f"Hello, {name}!"

# Python não tem arrow functions, mas tem lambda (similar)
add = lambda a, b: a + b

# Mas geralmente usa-se def mesmo para coisas simples
def add(a, b):
    return a + b
```

### Funções com Valores Padrão

**JavaScript:**
```javascript
function greet(name = "Guest") {
    return `Hello, ${name}!`;
}
```

**Python:**
```python
def greet(name="Guest"):
    return f"Hello, {name}!"
```

### Arrow Functions vs Lambda

**JavaScript:**
```javascript
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(n => n * 2);
```

**Python:**
```python
numbers = [1, 2, 3, 4]
doubled = list(map(lambda n: n * 2, numbers))
# Mas é mais comum usar List Comprehension:
doubled = [n * 2 for n in numbers]
```

---

## 4. List Comprehensions

**List Comprehensions são uma das coisas mais Pythonic e substituem muito do que você faz com `map`, `filter` no JavaScript.**

### Map Equivalent

**JavaScript:**
```javascript
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2);
```

**Python:**
```python
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
```

### Filter Equivalent

**JavaScript:**
```javascript
const numbers = [1, 2, 3, 4, 5];
const evens = numbers.filter(n => n % 2 === 0);
```

**Python:**
```python
numbers = [1, 2, 3, 4, 5]
evens = [n for n in numbers if n % 2 == 0]
```

### Map + Filter Combinado

**JavaScript:**
```javascript
const numbers = [1, 2, 3, 4, 5];
const doubledEvens = numbers
    .filter(n => n % 2 === 0)
    .map(n => n * 2);
```

**Python:**
```python
numbers = [1, 2, 3, 4, 5]
doubled_evens = [n * 2 for n in numbers if n % 2 == 0]
```

### Dictionary Comprehensions

**JavaScript:**
```javascript
const users = [{name: "João", age: 30}, {name: "Maria", age: 25}];
const userMap = users.reduce((acc, user) => {
    acc[user.name] = user.age;
    return acc;
}, {});
```

**Python:**
```python
users = [{"name": "João", "age": 30}, {"name": "Maria", "age": 25}]
user_map = {user["name"]: user["age"] for user in users}
```

---

## 5. Type Hints

**Python tem Type Hints (similar ao TypeScript, mas opcional):**

**TypeScript:**
```typescript
interface User {
    name: string;
    age: number;
    email?: string;
}

function greet(user: User): string {
    return `Hello, ${user.name}!`;
}
```

**Python:**
```python
from typing import Optional, Dict, List

# Type hints (opcional, mas recomendado)
def greet(user: Dict[str, any]) -> str:
    return f"Hello, {user['name']}!"

# Com Pydantic (similar a interfaces TypeScript)
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: Optional[str] = None

def greet(user: User) -> str:
    return f"Hello, {user.name}!"  # Agora pode usar .name!
```

---

## 🎯 Próximos Passos

1. Execute os exemplos em `examples.py`
2. Faça os exercícios em `exercises.py`
3. Compare com seus conhecimentos de React
4. Avance para o Módulo 02: Async Programming

---

## 📝 Resumo das Diferenças Principais

| Conceito | JavaScript | Python |
|----------|-----------|--------|
| Variáveis | `const`, `let` | Sempre variável (sem const) |
| Arrays | `[]` | `[]` (mas chamado de list) |
| Objects | `{}` | `{}` (mas chamado de dict) |
| Null | `null`, `undefined` | `None` |
| Booleanos | `true`, `false` | `True`, `False` |
| Funções | `function` ou `=>` | `def` ou `lambda` |
| Nomenclatura | `camelCase` | `snake_case` |
| Acesso dict | `obj.key` ou `obj["key"]` | `obj["key"]` apenas |
| Transformação | `.map()`, `.filter()` | List comprehensions |

