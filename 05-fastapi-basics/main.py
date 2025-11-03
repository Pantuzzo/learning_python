"""
Módulo 05: FastAPI Basics - Exemplo Completo

Execute: uvicorn main:app --reload
Acesse: http://localhost:8000/docs (documentação automática)
"""

from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from enum import Enum

# Criar aplicação FastAPI
app = FastAPI(
    title="Learning FastAPI",
    description="API de exemplo para aprender FastAPI",
    version="1.0.0"
)

# ============================================================================
# MODELOS (Pydantic) - Similar a interfaces TypeScript ou Zod schemas
# ============================================================================

class UserRole(str, Enum):
    """Enum para roles (similar a union types no TypeScript)"""
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

class User(BaseModel):
    """Modelo de usuário (similar a interface User no TypeScript)"""
    name: str = Field(..., description="Nome do usuário", min_length=2)
    email: EmailStr
    age: int = Field(..., ge=18, description="Idade mínima: 18")
    role: UserRole = UserRole.USER
    
    class Config:
        """Configuração do modelo"""
        json_schema_extra = {
            "example": {
                "name": "João Silva",
                "email": "joao@example.com",
                "age": 30,
                "role": "user"
            }
        }

class UserResponse(BaseModel):
    """Modelo de resposta (pode ter campos diferentes do request)"""
    id: int
    name: str
    email: str
    role: UserRole
    created_at: str

class UpdateUser(BaseModel):
    """Modelo para atualização parcial (campos opcionais)"""
    name: Optional[str] = None
    age: Optional[int] = Field(None, ge=18)

# ============================================================================
# BANCO DE DADOS SIMULADO (em produção, usaria PostgreSQL, MongoDB, etc.)
# ============================================================================

# Simulando um banco de dados em memória
fake_db: List[dict] = []
next_id = 1

# ============================================================================
# DEPENDENCY INJECTION (Similar a Context API ou Custom Hooks no React)
# ============================================================================

def get_current_user(authorization: Optional[str] = Header(None)) -> dict:
    """
    Dependency para autenticação (similar a middleware/context no Express/React)
    
    Em uma aplicação real, você verificaria um JWT token aqui.
    """
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Authorization header required"
        )
    
    # Simulando usuário autenticado
    return {
        "id": 1,
        "name": "João",
        "role": "admin"
    }

def require_admin(current_user: dict = Depends(get_current_user)) -> dict:
    """Dependency que verifica se usuário é admin"""
    if current_user["role"] != "admin":
        raise HTTPException(403, "Admin access required")
    return current_user

# ============================================================================
# ROTAS - Similar a routes no React Router ou Express
# ============================================================================

@app.get("/")
def read_root():
    """Endpoint raiz (similar a app.get('/') no Express)"""
    return {
        "message": "Hello FastAPI!",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

# ============================================================================
# CRUD de Usuários
# ============================================================================

@app.get("/users", response_model=List[UserResponse])
def list_users(
    skip: int = 0,
    limit: int = 10,
    role: Optional[UserRole] = None
):
    """
    Lista usuários (similar a GET /api/users no Express)
    
    - Query parameters (similar a req.query)
    - Validação automática de tipos
    """
    users = fake_db.copy()
    
    # Filtro por role (se fornecido)
    if role:
        users = [u for u in users if u.get("role") == role]
    
    # Paginação
    return users[skip:skip + limit]

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    """
    Busca um usuário por ID (similar a GET /api/users/:id no Express)
    
    - Path parameters (similar a req.params)
    """
    user = next((u for u in fake_db if u.get("id") == user_id), None)
    
    if not user:
        raise HTTPException(404, f"User {user_id} not found")
    
    return user

@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: User):
    """
    Cria um novo usuário (similar a POST /api/users no Express)
    
    - Request body (similar a req.body)
    - Validação automática via Pydantic
    """
    global next_id
    
    # Criar usuário
    user_data = {
        "id": next_id,
        **user.model_dump(),
        "created_at": "2024-01-01T00:00:00"  # Em produção, usaria datetime.now()
    }
    
    fake_db.append(user_data)
    next_id += 1
    
    return user_data

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UpdateUser, current_user: dict = Depends(get_current_user)):
    """
    Atualiza um usuário (similar a PUT /api/users/:id no Express)
    
    - Dependency Injection (similar a middleware/context)
    """
    user = next((u for u in fake_db if u.get("id") == user_id), None)
    
    if not user:
        raise HTTPException(404, f"User {user_id} not found")
    
    # Apenas admin ou o próprio usuário pode atualizar
    if current_user["id"] != user_id and current_user["role"] != "admin":
        raise HTTPException(403, "You can only update your own profile")
    
    # Atualizar campos fornecidos
    update_data = user_update.model_dump(exclude_unset=True)
    user.update(update_data)
    
    return user

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, admin: dict = Depends(require_admin)):
    """
    Deleta um usuário (similar a DELETE /api/users/:id no Express)
    
    - Usa dependency require_admin (apenas admins podem deletar)
    """
    global fake_db
    
    user = next((u for u in fake_db if u.get("id") == user_id), None)
    
    if not user:
        raise HTTPException(404, f"User {user_id} not found")
    
    fake_db.remove(user)
    return None  # 204 No Content

# ============================================================================
# ROTA COM MÚLTIPLAS DEPENDENCIAS
# ============================================================================

@app.get("/users/{user_id}/profile")
def get_user_profile(user_id: int, current_user: dict = Depends(get_current_user)):
    """
    Exemplo de rota com dependency injection
    
    - current_user é injetado automaticamente
    - Similar a useContext(AuthContext) no React
    """
    if current_user["id"] != user_id and current_user["role"] != "admin":
        raise HTTPException(403, "You can only view your own profile")
    
    user = next((u for u in fake_db if u.get("id") == user_id), None)
    
    if not user:
        raise HTTPException(404, f"User {user_id} not found")
    
    return {
        "user": user,
        "viewed_by": current_user["name"]
    }

# ============================================================================
# COMPARAÇÃO COM EXPRESS.JS
# ============================================================================

"""
EXPRESS.JS EQUIVALENTE (para referência):

const express = require('express');
const app = express();

// Middleware de autenticação
const authenticate = (req, res, next) => {
    const auth = req.headers.authorization;
    if (!auth) return res.status(401).json({ error: 'Unauthorized' });
    req.user = { id: 1, name: 'João', role: 'admin' };
    next();
};

app.get('/users', (req, res) => {
    const { skip, limit } = req.query;
    res.json(fakeDb.slice(skip, skip + limit));
});

app.post('/users', (req, res) => {
    // Validação manual necessária
    const user = req.body;
    fakeDb.push({ id: nextId++, ...user });
    res.status(201).json(user);
});

FASTAPI VANTAGENS:
✅ Validação automática (não precisa validação manual)
✅ Documentação automática (/docs)
✅ Type hints integradas
✅ Dependency Injection nativo
✅ Performance superior (usa Starlette + Pydantic)
"""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

