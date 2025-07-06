from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.auth import routes as auth_routes
from backend.app.database import Base, engine

# Criação das tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configuração do CORS para permitir requisições do React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusão das rotas de autenticação (registro)
app.include_router(auth_routes.router)
