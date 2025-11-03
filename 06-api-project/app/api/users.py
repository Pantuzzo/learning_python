"""
Rotas de Usuários
Similar a pages/api/users no Next.js ou routes/users.js no Express
"""

from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from app.models.user import UserCreate, UserUpdate, UserResponse, UserRole
from app.services.user_service import user_service

# Criar router (similar a const router = express.Router())
router = APIRouter()

# Dependency injection (similar a middleware ou context no React/Express)
def get_user_service():
    """Dependency para injetar service (similar a useContext no React)"""
    return user_service

@router.get("", response_model=List[UserResponse])
def list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    role: Optional[UserRole] = Query(None),
    service = Depends(get_user_service)
):
    """
    Lista usuários (similar a GET /api/users no React/Express)
    
    - Query parameters (similar a req.query)
    - Dependency injection do service
    """
    users = service.get_all(skip=skip, limit=limit, role=role)
    return users

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, service = Depends(get_user_service)):
    """
    Busca usuário por ID (similar a GET /api/users/:id)
    """
    user = service.get_by_id(user_id)
    
    if not user:
        raise HTTPException(404, f"User {user_id} not found")
    
    return user

@router.post("", response_model=UserResponse, status_code=201)
def create_user(user_data: UserCreate, service = Depends(get_user_service)):
    """
    Cria novo usuário (similar a POST /api/users)
    
    - Request body é validado automaticamente pelo Pydantic
    """
    user = service.create(user_data)
    return user

@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user_update: UserUpdate,
    service = Depends(get_user_service)
):
    """
    Atualiza usuário (similar a PUT /api/users/:id)
    """
    user = service.update(user_id, user_update)
    
    if not user:
        raise HTTPException(404, f"User {user_id} not found")
    
    return user

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, service = Depends(get_user_service)):
    """
    Deleta usuário (similar a DELETE /api/users/:id)
    """
    success = service.delete(user_id)
    
    if not success:
        raise HTTPException(404, f"User {user_id} not found")
    
    return None

