# 🐍 Python Learning Project - Para Desenvolvedores React

Bem-vindo! Este projeto foi criado especialmente para desenvolvedores React que querem aprender Python backend.

## 🎯 Por que este projeto?

Este projeto foi baseado na estrutura do projeto `ai-api-smarthow` que você já conhece, mas foi adaptado para ser um guia educacional progressivo. Aqui você vai aprender Python conectando conceitos que já conhece do React/JavaScript.

## 🚀 Começando

### Pré-requisitos
- Python 3.11 ou superior instalado
- Conhecimento em React/JavaScript
- Editor de código (VS Code recomendado)

### Setup Inicial

1. **Crie um ambiente virtual** (similar ao `node_modules` no npm):
```bash
python -m venv venv
```

2. **Ative o ambiente virtual**:
   - Windows (PowerShell): `.\venv\Scripts\Activate.ps1`
   - Mac/Linux: `source venv/bin/activate`

3. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

## 📚 Roadmap de Aprendizado

### 📍 Módulo 01: Basics - Python para React Developers
**Tempo estimado: 1 semana**

Aprenda os fundamentos de Python comparando com JavaScript que você já conhece.

- [ ] Variáveis e tipos de dados
- [ ] Estruturas de dados (listas, dicionários)
- [ ] Funções e escopo
- [ ] List comprehensions
- [ ] Type hints

**Arquivos principais:**
- `01-basics/README.md` - Guia completo
- `01-basics/examples.py` - Exemplos práticos
- `01-basics/exercises.py` - Exercícios

---

### 📍 Módulo 02: Async Programming
**Tempo estimado: 1 semana**

Entenda programação assíncrona em Python (similar a async/await no JavaScript).

- [ ] async/await em Python
- [ ] Tasks e corrotinas
- [ ] Event loops
- [ ] Paralelismo

**Arquivos principais:**
- `02-async/README.md`
- `02-async/examples.py`

---

### 📍 Módulo 03: Classes e OOP
**Tempo estimado: 1 semana**

Aprenda Orientação a Objetos em Python (pense como React Components).

- [ ] Classes e objetos
- [ ] Herança (similar a composição de componentes)
- [ ] Decorators (@decorator vs HOCs)
- [ ] Dataclasses

**Arquivos principais:**
- `03-classes-oop/README.md`
- `03-classes-oop/examples.py`

---

### 📍 Módulo 04: Error Handling e Validation
**Tempo estimado: 1 semana**

Aprenda a tratar erros e validar dados (similar a try/catch e Zod/PropTypes).

- [ ] Try/except
- [ ] Pydantic (validação, similar ao Zod)
- [ ] Custom exceptions
- [ ] Error handling patterns

**Arquivos principais:**
- `04-error-validation/README.md`
- `04-error-validation/examples.py`

---

### 📍 Módulo 05: FastAPI Basics
**Tempo estimado: 1 semana**

Introdução ao FastAPI (framework web moderno, similar ao Express.js).

- [ ] FastAPI vs Express.js
- [ ] Routes e decorators
- [ ] Request/Response models
- [ ] Dependency injection

**Arquivos principais:**
- `05-fastapi-basics/README.md`
- `05-fastapi-basics/main.py`
- `05-fastapi-basics/examples/`

---

### 📍 Módulo 06: API Project Completo
**Tempo estimado: 2 semanas**

Projeto completo seguindo a estrutura do `ai-api-smarthow`.

- [ ] Estrutura de projeto
- [ ] Organização de rotas
- [ ] Services pattern
- [ ] State management
- [ ] WebSocket (similar a socket.io)

**Arquivos principais:**
- `06-api-project/README.md`
- `06-api-project/app/` - Estrutura completa

---

## 🔄 Comparações Rápidas

### React/JavaScript → Python

| JavaScript | Python | Conceito |
|-----------|--------|----------|
| `const arr = []` | `arr = []` | Arrays/Listas |
| `const obj = {}` | `obj = {}` | Objetos/Dicionários |
| `function func() {}` | `def func():` | Funções |
| `async function` | `async def` | Funções assíncronas |
| `await fetch()` | `await httpx.get()` | Requisições HTTP |
| `try/catch` | `try/except` | Tratamento de erros |
| `interface Props` | `class Props(BaseModel)` | Tipos/Validação |
| `useState()` | `state: Dict = {}` | Estado |
| `useEffect()` | Background tasks | Efeitos colaterais |

## 📖 Estrutura de Cada Módulo

Cada módulo segue esta estrutura:

```
XX-module-name/
├── README.md          # Explicações detalhadas
├── examples.py        # Exemplos práticos comentados
├── exercises.py       # Exercícios para praticar
├── solutions.py       # Soluções dos exercícios
└── comparisons/       # Comparações React vs Python
```

## 💡 Dicas de Aprendizado

1. **Leia o README primeiro** - Cada módulo tem explicações detalhadas
2. **Execute os exemplos** - Não apenas leia, execute e modifique
3. **Faça os exercícios** - Prática é essencial
4. **Compare com React** - Use seu conhecimento de React como referência
5. **Construa algo** - Aplique o que aprendeu criando projetos pequenos

## 🛠️ Ferramentas Úteis

- **Python REPL**: `python` no terminal (similar ao Node.js REPL)
- **IPython**: Interface interativa melhorada
- **VS Code**: Com extensão Python
- **Black**: Formatador de código (similar ao Prettier)
- **pytest**: Framework de testes (similar ao Jest)

## 📚 Recursos Adicionais

- [Documentação Python](https://docs.python.org/3/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)

## 🎯 Próximos Passos

1. Comece pelo **Módulo 01: Basics**
2. Leia o README do módulo
3. Execute os exemplos
4. Faça os exercícios
5. Avance para o próximo módulo

**Boa sorte na sua jornada de aprendizado! 🚀**

# learning_python
