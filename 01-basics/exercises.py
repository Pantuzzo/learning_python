"""
Módulo 01: Basics - Exercícios Práticos

Complete as funções abaixo. Compare com o que você faria em JavaScript/React.
"""

# ============================================================================
# EXERCÍCIO 1: Função de Saudação
# ============================================================================

def greet_user(name: str, time_of_day: str = "dia") -> str:
    """
    Crie uma função que retorna uma saudação personalizada.
    
    Exemplo:
    greet_user("João", "manhã") -> "Bom dia, João!"
    greet_user("Maria") -> "Bom dia, Maria!"
    
    JavaScript equivalente:
    function greetUser(name, timeOfDay = "dia") {
        const greetings = { manhã: "Bom dia", tarde: "Boa tarde", noite: "Boa noite" };
        return `${greetings[timeOfDay] || "Bom dia"}, ${name}!`;
    }
    """
    # TODO: Implemente a função aqui
    # Dica: Use um dicionário para mapear períodos do dia
    pass


# ============================================================================
# EXERCÍCIO 2: Processar Lista de Usuários
# ============================================================================

def get_active_users(users: list) -> list:
    """
    Filtre apenas os usuários ativos (is_active = True).
    
    Exemplo:
    users = [
        {"name": "João", "is_active": True},
        {"name": "Maria", "is_active": False},
        {"name": "Pedro", "is_active": True}
    ]
    get_active_users(users) -> [{"name": "João", "is_active": True}, {"name": "Pedro", "is_active": True}]
    
    JavaScript equivalente:
    const activeUsers = users.filter(user => user.is_active);
    """
    # TODO: Use List Comprehension para filtrar
    pass


# ============================================================================
# EXERCÍCIO 3: Calcular Total de Preços
# ============================================================================

def calculate_total_price(items: list) -> float:
    """
    Calcule o total dos preços de uma lista de itens.
    
    Exemplo:
    items = [
        {"name": "Produto 1", "price": 10.50},
        {"name": "Produto 2", "price": 20.00},
        {"name": "Produto 3", "price": 5.75}
    ]
    calculate_total_price(items) -> 36.25
    
    JavaScript equivalente:
    const total = items.reduce((sum, item) => sum + item.price, 0);
    """
    # TODO: Use sum() com List Comprehension ou for loop
    pass


# ============================================================================
# EXERCÍCIO 4: Criar Mapa de Usuários por Cidade
# ============================================================================

def group_users_by_city(users: list) -> dict:
    """
    Agrupe usuários por cidade em um dicionário.
    
    Exemplo:
    users = [
        {"name": "João", "city": "São Paulo"},
        {"name": "Maria", "city": "Rio de Janeiro"},
        {"name": "Pedro", "city": "São Paulo"}
    ]
    group_users_by_city(users) -> {
        "São Paulo": [{"name": "João", "city": "São Paulo"}, {"name": "Pedro", "city": "São Paulo"}],
        "Rio de Janeiro": [{"name": "Maria", "city": "Rio de Janeiro"}]
    }
    
    JavaScript equivalente:
    const grouped = users.reduce((acc, user) => {
        if (!acc[user.city]) acc[user.city] = [];
        acc[user.city].push(user);
        return acc;
    }, {});
    """
    # TODO: Use um dicionário e loops ou Dict Comprehension
    pass


# ============================================================================
# EXERCÍCIO 5: Transformar Lista de Strings
# ============================================================================

def transform_strings(strings: list, transform: str = "upper") -> list:
    """
    Transforme uma lista de strings (upper, lower, capitalize).
    
    Exemplo:
    transform_strings(["hello", "world"], "upper") -> ["HELLO", "WORLD"]
    transform_strings(["HELLO", "WORLD"], "lower") -> ["hello", "world"]
    transform_strings(["hello", "world"], "capitalize") -> ["Hello", "World"]
    
    JavaScript equivalente:
    const transformed = strings.map(s => {
        if (transform === "upper") return s.toUpperCase();
        if (transform === "lower") return s.toLowerCase();
        if (transform === "capitalize") return s.charAt(0).toUpperCase() + s.slice(1);
        return s;
    });
    """
    # TODO: Use List Comprehension com condições
    pass


# ============================================================================
# EXERCÍCIO 6: Validar Email
# ============================================================================

def is_valid_email(email: str) -> bool:
    """
    Valide se um email tem formato básico válido (contém @ e .).
    
    Exemplo:
    is_valid_email("joao@email.com") -> True
    is_valid_email("invalid-email") -> False
    is_valid_email("@email.com") -> False
    
    JavaScript equivalente:
    const isValidEmail = (email) => {
        return email.includes("@") && email.includes(".") && email.indexOf("@") < email.indexOf(".");
    };
    """
    # TODO: Verifique se contém @ e . (e @ vem antes do .)
    pass


# ============================================================================
# TESTES (Execute para verificar suas respostas)
# ============================================================================

if __name__ == "__main__":
    print("Testando suas soluções...")
    print("\nExecute solutions.py para ver as respostas!")
    
    # Teste 1
    result1 = greet_user("João", "manhã")
    print(f"Teste 1: {result1}")
    
    # Teste 2
    users = [
        {"name": "João", "is_active": True},
        {"name": "Maria", "is_active": False}
    ]
    result2 = get_active_users(users)
    print(f"Teste 2: {result2}")
    
    # Continue testando as outras funções...

