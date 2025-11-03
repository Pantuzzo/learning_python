"""
Modelos de Post
Similar a interfaces TypeScript
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class PostBase(BaseModel):
    """Base model para posts"""
    title: str = Field(..., min_length=3, max_length=200)
    content: str = Field(..., min_length=10)
    author_id: int

class PostCreate(PostBase):
    """Model para criação de post"""
    tags: List[str] = Field(default_factory=list, max_items=10)

class PostUpdate(BaseModel):
    """Model para atualização parcial"""
    title: Optional[str] = Field(None, min_length=3, max_length=200)
    content: Optional[str] = Field(None, min_length=10)
    tags: Optional[List[str]] = Field(None, max_items=10)

class PostResponse(PostBase):
    """Model de resposta"""
    id: int
    tags: List[str]
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True

