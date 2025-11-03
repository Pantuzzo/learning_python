"""
User Service - Lógica de negócio
Similar a Custom Hooks no React (useUsers, useUserById, etc.)
"""

from typing import List, Optional
from app.models.user import UserCreate, UserUpdate, UserResponse, UserRole
from datetime import datetime

# Banco de dados simulado (em produção, use PostgreSQL, MongoDB, etc.)
fake_users_db: List[dict] = []
next_user_id = 1

class UserService:
    """
    Service de usuários (similar a Custom Hook no React)
    
    Em React:
    function useUsers() {
        const [users, setUsers] = useState([]);
        // lógica de busca, criação, etc.
        return { users, createUser, updateUser, ... };
    }
    """
    
    def get_all(self, skip: int = 0, limit: int = 10, role: Optional[UserRole] = None) -> List[UserResponse]:
        """
        Busca todos os usuários (similar a fetch('/api/users') no React)
        """
        users = fake_users_db.copy()
        
        # Filtro por role
        if role:
            users = [u for u in users if u.get("role") == role.value]
        
        # Paginação
        paginated = users[skip:skip + limit]
        
        # Converter para UserResponse
        return [UserResponse(**user) for user in paginated]
    
    def get_by_id(self, user_id: int) -> Optional[UserResponse]:
        """
        Busca usuário por ID (similar a fetch(`/api/users/${id}`) no React)
        """
        user = next((u for u in fake_users_db if u.get("id") == user_id), None)
        
        if not user:
            return None
        
        return UserResponse(**user)
    
    def create(self, user_data: UserCreate) -> UserResponse:
        """
        Cria novo usuário (similar a POST /api/users no React)
        """
        global next_user_id
        
        user_dict = {
            "id": next_user_id,
            "name": user_data.name,
            "email": user_data.email,
            "age": user_data.age,
            "role": user_data.role,
            "created_at": datetime.now()
        }
        
        fake_users_db.append(user_dict)
        next_user_id += 1
        
        return UserResponse(**user_dict)
    
    def update(self, user_id: int, user_update: UserUpdate) -> Optional[UserResponse]:
        """
        Atualiza usuário (similar a PUT /api/users/:id no React)
        """
        user = next((u for u in fake_users_db if u.get("id") == user_id), None)
        
        if not user:
            return None
        
        # Atualizar apenas campos fornecidos
        update_data = user_update.model_dump(exclude_unset=True)
        user.update(update_data)
        
        return UserResponse(**user)
    
    def delete(self, user_id: int) -> bool:
        """
        Deleta usuário (similar a DELETE /api/users/:id no React)
        """
        global fake_users_db
        
        user = next((u for u in fake_users_db if u.get("id") == user_id), None)
        
        if not user:
            return False
        
        fake_users_db.remove(user)
        return True

# Instância singleton (similar a export const userService no Node.js)
user_service = UserService()

