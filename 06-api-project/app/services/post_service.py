"""
Post Service - Lógica de negócio para posts
Similar a Custom Hook usePosts no React
"""

from typing import List, Optional
from app.models.post import PostCreate, PostUpdate, PostResponse
from datetime import datetime

# Banco de dados simulado
fake_posts_db: List[dict] = []
next_post_id = 1

class PostService:
    """Service de posts (similar a usePosts hook no React)"""
    
    def get_all(self, skip: int = 0, limit: int = 10, author_id: Optional[int] = None) -> List[PostResponse]:
        """Busca todos os posts"""
        posts = fake_posts_db.copy()
        
        if author_id:
            posts = [p for p in posts if p.get("author_id") == author_id]
        
        paginated = posts[skip:skip + limit]
        return [PostResponse(**post) for post in paginated]
    
    def get_by_id(self, post_id: int) -> Optional[PostResponse]:
        """Busca post por ID"""
        post = next((p for p in fake_posts_db if p.get("id") == post_id), None)
        
        if not post:
            return None
        
        return PostResponse(**post)
    
    def create(self, post_data: PostCreate) -> PostResponse:
        """Cria novo post"""
        global next_post_id
        
        post_dict = {
            "id": next_post_id,
            "title": post_data.title,
            "content": post_data.content,
            "author_id": post_data.author_id,
            "tags": post_data.tags,
            "created_at": datetime.now(),
            "updated_at": None
        }
        
        fake_posts_db.append(post_dict)
        next_post_id += 1
        
        return PostResponse(**post_dict)
    
    def update(self, post_id: int, post_update: PostUpdate) -> Optional[PostResponse]:
        """Atualiza post"""
        post = next((p for p in fake_posts_db if p.get("id") == post_id), None)
        
        if not post:
            return None
        
        update_data = post_update.model_dump(exclude_unset=True)
        post.update(update_data)
        post["updated_at"] = datetime.now()
        
        return PostResponse(**post)
    
    def delete(self, post_id: int) -> bool:
        """Deleta post"""
        global fake_posts_db
        
        post = next((p for p in fake_posts_db if p.get("id") == post_id), None)
        
        if not post:
            return False
        
        fake_posts_db.remove(post)
        return True

post_service = PostService()

