"""
Módulo 01: Basics - Exemplos Práticos
Comparação JavaScript/React vs Python

Execute este arquivo: python examples.py
"""

# ============================================================================
# 1. VARIÁVEIS E TIPOS
# ============================================================================

print("=" * 60)
print("1. VARIÁVEIS E TIPOS")
print("=" * 60)

# JavaScript: const name = "João";
# Python:
name = "João"
age = 30
is_active = True  # Note: True com maiúscula!
salary = 1500.50

print(f"Nome: {name}, Tipo: {type(name)}")
print(f"Idade: {age}, Tipo: {type(age)}")
print(f"Ativo: {is_active}, Tipo: {type(is_active)}")
print(f"Salário: {salary}, Tipo: {type(salary)}")

# None é equivalente a null/undefined no JavaScript
data = None
print(f"Data: {data}, Tipo: {type(data)}")

# ============================================================================
# 2. ESTRUTURAS DE DADOS - LISTAS (Arrays)
# ============================================================================

print("\n" + "=" * 60)
print("2. LISTAS (Arrays em JavaScript)")
print("=" * 60)

# JavaScript: const fruits = ["apple", "banana"];
# Python:
fruits = ["apple", "banana", "orange"]
print(f"Frutas: {fruits}")

# Adicionar item (similar a push)
fruits.append("grape")  # JavaScript: fruits.push("grape")
print(f"Após append: {fruits}")

# Remover último (igual ao JavaScript)
last = fruits.pop()  # JavaScript: fruits.pop()
print(f"Item removido: {last}")
print(f"Frutas restantes: {fruits}")

# Acessar por índice (igual)
print(f"Primeira fruta: {fruits[0]}")  # JavaScript: fruits[0]

# Tamanho (método diferente)
print(f"Quantidade: {len(fruits)}")  # JavaScript: fruits.length

# ============================================================================
# 3. ESTRUTURAS DE DADOS - DICIONÁRIOS (Objects)
# ============================================================================

print("\n" + "=" * 60)
print("3. DICIONÁRIOS (Objects em JavaScript)")
print("=" * 60)

# JavaScript: const user = { name: "João", age: 30 };
# Python:
user = {
    "name": "João",
    "age": 30,
    "email": "joao@email.com"
}

print(f"Usuário: {user}")

# Acesso - IMPORTANTE: sempre com colchetes em Python!
# JavaScript: user.name ou user["name"]
# Python: APENAS user["name"]
print(f"Nome: {user['name']}")
print(f"Idade: {user['age']}")

# Acesso seguro com valor padrão
city = user.get("city", "Não informado")  # JavaScript: user.city ?? "Não informado"
print(f"Cidade: {city}")

# Adicionar propriedade (igual)
user["city"] = "São Paulo"  # JavaScript: user.city = "São Paulo"
print(f"Usuário atualizado: {user}")

# ============================================================================
# 4. FUNÇÕES
# ============================================================================

print("\n" + "=" * 60)
print("4. FUNÇÕES")
print("=" * 60)

# JavaScript: function greet(name) { return `Hello, ${name}!`; }
# Python:
def greet(name):
    """Função simples - similar a function no JavaScript"""
    return f"Hello, {name}!"

print(greet("João"))

# Função com valor padrão
def greet_with_default(name="Guest"):
    """Função com parâmetro padrão"""
    return f"Hello, {name}!"

print(greet_with_default())  # Usa valor padrão
print(greet_with_default("Maria"))

# Função com múltiplos retornos (usando tuple)
def get_name_and_age():
    """Retorna múltiplos valores (em JavaScript seria um objeto)"""
    return "João", 30

name, age = get_name_and_age()  # Desempacotamento
print(f"Nome: {name}, Idade: {age}")

# Lambda (similar a arrow function, mas mais limitado)
# JavaScript: const add = (a, b) => a + b;
# Python:
add = lambda a, b: a + b
print(f"Soma (lambda): {add(5, 3)}")

# Mas geralmente usa-se def mesmo para coisas simples
def add_function(a, b):
    """Versão com def (mais comum)"""
    return a + b

print(f"Soma (def): {add_function(5, 3)}")

# ============================================================================
# 5. LIST COMPREHENSIONS (Map/Filter)
# ============================================================================

print("\n" + "=" * 60)
print("5. LIST COMPREHENSIONS")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]
print(f"Números originais: {numbers}")

# Map - JavaScript: numbers.map(n => n * 2)
# Python:
doubled = [n * 2 for n in numbers]
print(f"Dobrado (map equivalente): {doubled}")

# Filter - JavaScript: numbers.filter(n => n % 2 === 0)
# Python:
evens = [n for n in numbers if n % 2 == 0]
print(f"Pares (filter equivalente): {evens}")

# Map + Filter combinado
# JavaScript: numbers.filter(n => n % 2 === 0).map(n => n * 2)
# Python:
doubled_evens = [n * 2 for n in numbers if n % 2 == 0]
print(f"Pares dobrados: {doubled_evens}")

# Dictionary Comprehension
# JavaScript: const userMap = users.reduce((acc, u) => { acc[u.name] = u.age; return acc; }, {});
# Python:
users = [
    {"name": "João", "age": 30},
    {"name": "Maria", "age": 25},
    {"name": "Pedro", "age": 35}
]

user_map = {user["name"]: user["age"] for user in users}
print(f"User map (dict comprehension): {user_map}")

# ============================================================================
# 6. TYPE HINTS (Opcional, mas recomendado)
# ============================================================================

print("\n" + "=" * 60)
print("6. TYPE HINTS")
print("=" * 60)

from typing import Dict, List, Optional

# Type hints (similar ao TypeScript, mas opcional)
def process_user(user: Dict[str, any]) -> str:
    """Função com type hints"""
    return f"Processando: {user['name']}"

result = process_user({"name": "João", "age": 30})
print(result)

# Com múltiplos tipos
def calculate_total(items: List[Dict[str, float]]) -> float:
    """Soma valores de uma lista de itens"""
    return sum(item.get("price", 0) for item in items)

items = [
    {"name": "Item 1", "price": 10.50},
    {"name": "Item 2", "price": 20.00},
    {"name": "Item 3", "price": 5.75}
]

total = calculate_total(items)
print(f"Total: R$ {total:.2f}")

# ============================================================================
# RESUMO - Comparação JavaScript vs Python
# ============================================================================

print("\n" + "=" * 60)
print("RESUMO DAS PRINCIPAIS DIFERENÇAS")
print("=" * 60)

comparison = {
    "JavaScript": {
        "arrays": "const arr = []",
        "objects": "const obj = { key: 'value' }",
        "access_object": "obj.key ou obj['key']",
        "functions": "function fn() {} ou () => {}",
        "null": "null ou undefined",
        "boolean": "true, false"
    },
    "Python": {
        "arrays": "arr = []  # List",
        "objects": "obj = { 'key': 'value' }  # Dict",
        "access_object": "obj['key']  # Sempre colchetes!",
        "functions": "def fn():",
        "null": "None",
        "boolean": "True, False"
    }
}

for lang, examples in comparison.items():
    print(f"\n{lang}:")
    for key, value in examples.items():
        print(f"  {key}: {value}")

print("\n" + "=" * 60)
print("Execute os exercícios em exercises.py para praticar!")
print("=" * 60)

