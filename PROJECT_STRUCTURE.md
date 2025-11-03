# 📁 Estrutura do Projeto

## Visão Geral

```
my_learning_project/
│
├── 📄 START_HERE.md              ← COMECE AQUI!
├── 📄 README.md                  ← Guia principal completo
├── 📄 PROJECT_PLAN.md            ← Plano detalhado do projeto
├── 📄 requirements.txt           ← Dependências Python
│
├── 📂 01-basics/                 ← SEMANA 1-2: Fundamentos Python
│   ├── README.md                 ← Guia do módulo
│   ├── examples.py               ← Exemplos práticos
│   ├── exercises.py              ← Exercícios para praticar
│   └── solutions.py              ← Soluções dos exercícios
│
├── 📂 02-async/                  ← SEMANA 3: Programação Assíncrona (Opcional)
│   └── README.md
│
├── 📂 03-classes-oop/            ← OOP e Classes (Opcional)
│   └── README.md
│
├── 📂 04-error-validation/        ← Tratamento de Erros (Opcional)
│   └── README.md
│
├── 📂 05-fastapi-basics/         ← SEMANA 4: FastAPI (IMPORTANTE!)
│   ├── README.md
│   └── main.py                   ← API de exemplo funcionando
│
├── 📂 06-api-project/            ← SEMANA 5-6: Projeto Completo
│   ├── README.md
│   ├── main.py                   ← Entry point da aplicação
│   └── app/
│       ├── api/                  ← Rotas (similar a pages/routes no React)
│       │   ├── users.py          ← Rotas de usuários
│       │   └── posts.py          ← Rotas de posts
│       ├── models/               ← Modelos (similar a types/interfaces)
│       │   ├── user.py
│       │   └── post.py
│       ├── services/              ← Lógica de negócio (similar a hooks)
│       │   ├── user_service.py
│       │   └── post_service.py
│       └── config/                ← Configurações
│           └── settings.py
│
├── 📂 comparisons/               ← Comparações React vs Python
│   └── react-vs-python.md        ← Guia de comparações
│
└── 📂 exercises/                  ← Exercícios adicionais
```

## 🎯 Fluxo de Aprendizado Recomendado

### Para Iniciantes Completos
```
START_HERE.md
    ↓
01-basics/ (Fundamentos)
    ↓
05-fastapi-basics/ (API básica)
    ↓
06-api-project/ (Projeto completo)
```

### Para Quem Já Conhece Backend (Node.js/Express)
```
START_HERE.md
    ↓
01-basics/ (Apenas referência rápida)
    ↓
05-fastapi-basics/ (Foco aqui!)
    ↓
06-api-project/ (Aprofundar)
```

## 📚 Mapeamento de Conceitos

### React/JavaScript → Python/FastAPI

| React/JS | Python | Localização |
|----------|--------|-------------|
| `useState()` | `state: Dict` | `01-basics/` |
| `async/await` | `async def` | `02-async/` |
| Components | Classes | `03-classes-oop/` |
| `try/catch` | `try/except` | `04-error-validation/` |
| Express routes | FastAPI routes | `05-fastapi-basics/` |
| Custom Hooks | Services | `06-api-project/app/services/` |
| TypeScript interfaces | Pydantic models | `06-api-project/app/models/` |
| `fetch()` | `httpx` | `comparisons/react-vs-python.md` |

## 🚀 Executando Projetos

### Módulo 01 (Basics)
```bash
python 01-basics/examples.py
python 01-basics/exercises.py
```

### Módulo 05 (FastAPI)
```bash
cd 05-fastapi-basics
uvicorn main:app --reload
# Acesse: http://localhost:8000/docs
```

### Módulo 06 (Projeto Completo)
```bash
cd 06-api-project
uvicorn main:app --reload
# Acesse: http://localhost:8000/docs
```

## 💡 Dicas de Navegação

1. **Comece sempre pelo README.md** de cada módulo
2. **Execute os exemplos** antes de fazer exercícios
3. **Use comparisons/** quando tiver dúvidas sobre equivalências
4. **Consulte o projeto original** (`ai-api-smarthow`) para ver padrões reais

## 📝 Notas Importantes

- ✅ Todos os módulos são independentes (exceto 06 que usa conceitos anteriores)
- ✅ Você pode pular módulos que não são essenciais
- ✅ O foco principal deve ser: **01 → 05 → 06**
- ✅ Use `comparisons/` como referência rápida

