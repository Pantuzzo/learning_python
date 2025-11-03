"""
Modelos de Usuário
Similar a interfaces TypeScript ou Zod schemas no React
"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum
from datetime import datetime

class UserRole(str, Enum):
    """Roles de usuário (similar a union types no TypeScript)"""
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

class UserBase(BaseModel):
    """Base model (similar a interface base no TypeScript)"""
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    age: int = Field(..., ge=18, le=120)

class UserCreate(UserBase):
    """Model para criação (similar a CreateUserDto no TypeScript)"""
    password: str = Field(..., min_length=8)
    role: UserRole = UserRole.USER

class UserUpdate(BaseModel):
    """Model para atualização parcial (similar a Partial<User> no TypeScript)"""
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, ge=18, le=120)

class UserResponse(UserBase):
    """Model de resposta (similar a UserResponseDto no TypeScript)"""
    id: int
    role: UserRole
    created_at: datetime
    
    class Config:
        """Configuração do modelo"""
        from_attributes = True  # Para ORMs como SQLAlchemy

