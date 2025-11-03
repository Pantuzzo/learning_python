"""
Módulo 06: API Project Completo
Entry point da aplicação (similar a App.js no React)

Execute: uvicorn main:app --reload
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importar routers (similar a importar rotas no React Router)
from app.api import users, posts
from app.config.settings import get_settings

# Obter configurações
settings = get_settings()

# Criar aplicação FastAPI (similar a criar app React)
app = FastAPI(
    title="Learning API Project",
    description="Projeto completo para aprender estrutura de APIs Python",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS (similar a configurar CORS no Express/Next.js)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check (similar a /api/health em Next.js)
@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": "1.0.0"
    }

# Incluir routers (similar a <Route> no React Router)
app.include_router(
    users.router,
    prefix="/api/users",
    tags=["users"]
)

app.include_router(
    posts.router,
    prefix="/api/posts",
    tags=["posts"]
)

# ============================================================================
# COMPARAÇÃO COM REACT/EXPRESS
# ============================================================================

"""
REACT ROUTER (Next.js) EQUIVALENTE:

// app/layout.tsx
export default function Layout() {
  return (
    <div>
      <Route path="/api/users" component={UsersRoutes} />
      <Route path="/api/posts" component={PostsRoutes} />
    </div>
  );
}

EXPRESS.JS EQUIVALENTE:

const express = require('express');
const app = express();

app.use('/api/users', usersRouter);
app.use('/api/posts', postsRouter);

FASTAPI (ESTE PROJETO):
- app.include_router() é similar a app.use() no Express
- Prefix é similar a path base no React Router
- Tags são para organização na documentação
"""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

