"""
Configurações da aplicação
Similar a arquivos .env/config no React/Node.js
"""

from pydantic import BaseModel
from typing import List

class Settings(BaseModel):
    """Configurações da aplicação (similar a process.env no Node.js)"""
    
    # API
    API_TITLE: str = "Learning API Project"
    API_VERSION: str = "1.0.0"
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000"
    ]
    
    # Database (em produção, use variáveis de ambiente)
    DATABASE_URL: str = "sqlite:///./app.db"
    
    # Security
    SECRET_KEY: str = "dev-secret-key-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

# Instância global (similar a export const settings no Node.js)
_settings = None

def get_settings() -> Settings:
    """Get settings singleton (similar a export default no Node.js)"""
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
