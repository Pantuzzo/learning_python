"""
Rotas de Posts
Similar a pages/api/posts no Next.js
"""

from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from app.models.post import PostCreate, PostUpdate, PostResponse
from app.services.post_service import post_service

router = APIRouter()

def get_post_service():
    """Dependency para injetar service"""
    return post_service

@router.get("", response_model=List[PostResponse])
def list_posts(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    author_id: Optional[int] = Query(None),
    service = Depends(get_post_service)
):
    """Lista posts"""
    posts = service.get_all(skip=skip, limit=limit, author_id=author_id)
    return posts

@router.get("/{post_id}", response_model=PostResponse)
def get_post(post_id: int, service = Depends(get_post_service)):
    """Busca post por ID"""
    post = service.get_by_id(post_id)
    
    if not post:
        raise HTTPException(404, f"Post {post_id} not found")
    
    return post

@router.post("", response_model=PostResponse, status_code=201)
def create_post(post_data: PostCreate, service = Depends(get_post_service)):
    """Cria novo post"""
    post = service.create(post_data)
    return post

@router.put("/{post_id}", response_model=PostResponse)
def update_post(
    post_id: int,
    post_update: PostUpdate,
    service = Depends(get_post_service)
):
    """Atualiza post"""
    post = service.update(post_id, post_update)
    
    if not post:
        raise HTTPException(404, f"Post {post_id} not found")
    
    return post

@router.delete("/{post_id}", status_code=204)
def delete_post(post_id: int, service = Depends(get_post_service)):
    """Deleta post"""
    success = service.delete(post_id)
    
    if not success:
        raise HTTPException(404, f"Post {post_id} not found")
    
    return None

