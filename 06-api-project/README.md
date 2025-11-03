# Módulo 06: API Project Completo

Este módulo contém um projeto completo seguindo a estrutura do `ai-api-smarthow`, mas adaptado para aprendizado.

## 🏗️ Estrutura do Projeto

```
06-api-project/
├── app/
│   ├── api/              # Rotas (similar a pages/routes no React Router)
│   │   ├── __init__.py
│   │   ├── users.py       # Rotas de usuários
│   │   └── posts.py       # Rotas de posts
│   ├── models/            # Modelos de dados (similar a types/interfaces)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── post.py
│   ├── services/          # Lógica de negócio (similar a hooks/utils)
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── post_service.py
│   └── config/            # Configurações (similar a .env/config)
│       ├── __init__.py
│       └── settings.py
├── main.py                # Entry point (similar a App.js)
└── requirements.txt       # Dependências
```

## 📋 Conceitos Aplicados

### 1. Separação de Responsabilidades

**Similar ao React:**
- **Components** (React) → **Routes** (FastAPI)
- **Hooks/Custom Hooks** → **Services**
- **Types/Interfaces** → **Models**
- **Context/Props** → **Dependency Injection**

### 2. Padrão de Organização

#### Routes (API Layer)
- Recebem requests HTTP
- Validam entrada (automaticamente via Pydantic)
- Chamam services
- Retornam responses

**Similar a:** Componentes de página no Next.js que chamam hooks

#### Services (Business Logic)
- Contém a lógica de negócio
- Não conhece HTTP/requests
- Reutilizável

**Similar a:** Custom Hooks no React (`useUsers`, `usePosts`)

#### Models (Data Models)
- Definem estrutura de dados
- Validação automática
- Type hints

**Similar a:** TypeScript interfaces ou Zod schemas

## 🔄 Comparação com React

### React Component Structure
```typescript
// Component
function UserList() {
  const { users, loading } = useUsers();  // Service/Hook
  return <div>{users.map(...)}</div>;
}

// Hook (Service)
function useUsers() {
  const [users, setUsers] = useState([]);
  useEffect(() => {
    fetchUsers().then(setUsers);
  }, []);
  return { users, loading };
}
```

### FastAPI Structure
```python
# Route (Component)
@router.get("/users")
def list_users(service: UserService = Depends()):
    users = service.get_all()  # Service
    return {"users": users}

# Service (Hook)
class UserService:
    def get_all(self):
        return self.db.query_users()
```

## 🚀 Como Usar

1. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

2. **Execute o servidor:**
```bash
uvicorn main:app --reload
```

3. **Acesse a documentação:**
```
http://localhost:8000/docs
```

## 📝 Exercícios

1. Adicione uma rota de comentários (`/api/comments`)
2. Crie um service para comentários
3. Adicione validação customizada
4. Implemente paginação real
5. Adicione testes unitários

## 🎯 Próximos Passos

Após entender esta estrutura:
- Adicione autenticação real (JWT)
- Conecte com banco de dados real (PostgreSQL)
- Adicione WebSocket (similar a Socket.io)
- Implemente cache (Redis)
- Adicione testes (pytest)

