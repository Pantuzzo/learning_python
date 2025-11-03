"""
Módulo 01: Basics - Soluções dos Exercícios

Compare estas soluções com o que você implementou e com JavaScript.
"""

# ============================================================================
# SOLUÇÃO 1: Função de Saudação
# ============================================================================

def greet_user(name: str, time_of_day: str = "dia") -> str:
    """
    Solução usando dicionário para mapear períodos do dia.
    """
    greetings = {
        "manhã": "Bom dia",
        "tarde": "Boa tarde",
        "noite": "Boa noite",
        "dia": "Bom dia"  # padrão
    }
    
    greeting = greetings.get(time_of_day, "Bom dia")
    return f"{greeting}, {name}!"


# ============================================================================
# SOLUÇÃO 2: Processar Lista de Usuários
# ============================================================================

def get_active_users(users: list) -> list:
    """
    Solução usando List Comprehension (equivalente a filter em JavaScript).
    """
    return [user for user in users if user.get("is_active", False)]


# ============================================================================
# SOLUÇÃO 3: Calcular Total de Preços
# ============================================================================

def calculate_total_price(items: list) -> float:
    """
    Solução usando sum() com List Comprehension (equivalente a reduce em JavaScript).
    """
    return sum(item.get("price", 0) for item in items)


# ============================================================================
# SOLUÇÃO 4: Criar Mapa de Usuários por Cidade
# ============================================================================

def group_users_by_city(users: list) -> dict:
    """
    Solução usando loop tradicional (poderia usar defaultdict também).
    """
    grouped = {}
    for user in users:
        city = user.get("city")
        if city:
            if city not in grouped:
                grouped[city] = []
            grouped[city].append(user)
    return grouped

# Alternativa mais Pythonic usando defaultdict:
# from collections import defaultdict
# def group_users_by_city(users: list) -> dict:
#     grouped = defaultdict(list)
#     for user in users:
#         city = user.get("city")
#         if city:
#             grouped[city].append(user)
#     return dict(grouped)


# ============================================================================
# SOLUÇÃO 5: Transformar Lista de Strings
# ============================================================================

def transform_strings(strings: list, transform: str = "upper") -> list:
    """
    Solução usando List Comprehension com condições.
    """
    if transform == "upper":
        return [s.upper() for s in strings]
    elif transform == "lower":
        return [s.lower() for s in strings]
    elif transform == "capitalize":
        return [s.capitalize() for s in strings]
    else:
        return strings

# Alternativa mais elegante usando dicionário de funções:
# def transform_strings(strings: list, transform: str = "upper") -> list:
#     transformers = {
#         "upper": str.upper,
#         "lower": str.lower,
#         "capitalize": str.capitalize
#     }
#     transformer = transformers.get(transform, lambda x: x)
#     return [transformer(s) for s in strings]


# ============================================================================
# SOLUÇÃO 6: Validar Email
# ============================================================================

def is_valid_email(email: str) -> bool:
    """
    Solução verificando formato básico de email.
    """
    if not email or not isinstance(email, str):
        return False
    
    # Deve conter @ e .
    if "@" not in email or "." not in email:
        return False
    
    # @ deve vir antes do último .
    at_index = email.index("@")
    dot_index = email.rindex(".")  # rindex pega o último ponto
    
    if at_index >= dot_index:
        return False
    
    # Deve ter algo antes do @ e depois do @
    if at_index == 0 or at_index == len(email) - 1:
        return False
    
    return True


# ============================================================================
# TESTES
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("TESTANDO SOLUÇÕES")
    print("=" * 60)
    
    # Teste 1
    print("\n1. Teste greet_user:")
    print(f"   {greet_user('João', 'manhã')}")
    print(f"   {greet_user('Maria', 'tarde')}")
    print(f"   {greet_user('Pedro')}")  # Usa padrão
    
    # Teste 2
    print("\n2. Teste get_active_users:")
    users = [
        {"name": "João", "is_active": True},
        {"name": "Maria", "is_active": False},
        {"name": "Pedro", "is_active": True}
    ]
    active = get_active_users(users)
    print(f"   Usuários ativos: {[u['name'] for u in active]}")
    
    # Teste 3
    print("\n3. Teste calculate_total_price:")
    items = [
        {"name": "Produto 1", "price": 10.50},
        {"name": "Produto 2", "price": 20.00},
        {"name": "Produto 3", "price": 5.75}
    ]
    total = calculate_total_price(items)
    print(f"   Total: R$ {total:.2f}")
    
    # Teste 4
    print("\n4. Teste group_users_by_city:")
    users = [
        {"name": "João", "city": "São Paulo"},
        {"name": "Maria", "city": "Rio de Janeiro"},
        {"name": "Pedro", "city": "São Paulo"},
        {"name": "Ana", "city": "Rio de Janeiro"}
    ]
    grouped = group_users_by_city(users)
    for city, city_users in grouped.items():
        names = [u["name"] for u in city_users]
        print(f"   {city}: {', '.join(names)}")
    
    # Teste 5
    print("\n5. Teste transform_strings:")
    strings = ["hello", "world", "python"]
    print(f"   Upper: {transform_strings(strings, 'upper')}")
    print(f"   Lower: {transform_strings(strings, 'lower')}")
    print(f"   Capitalize: {transform_strings(strings, 'capitalize')}")
    
    # Teste 6
    print("\n6. Teste is_valid_email:")
    emails = [
        "joao@email.com",
        "invalid-email",
        "@email.com",
        "email@",
        "valid@example.com"
    ]
    for email in emails:
        result = is_valid_email(email)
        print(f"   {email}: {result}")
    
    print("\n" + "=" * 60)
    print("Todos os testes concluídos!")
    print("=" * 60)

