from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config import settings
from backend.app.database import engine

app = FastAPI(title="API do Projeto de TCC")

origins = [
    "http://localhost:5173",  # ou 3000, dependendo da porta do React
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




# rotas de teste
@app.get("/")
def home():
    return {"mensagem": "API rodando com sucesso!"}

@app.get("/config")
def config():
    return {
        "banco": settings.DATABASE_URL,
        "jwt_secret": settings.JWT_SECRET
    }

@app.get('/teste-db')
def teste_conexao():
    try:
        with engine.connect() as conn:
            return {"status": "conectado com sucesso!" }
    except Exception as e:
        return {"erro": str(e)}
    


    


        

