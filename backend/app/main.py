from fastapi import FastAPI
from backend.config import settings
from backend.app.database import engine

app = FastAPI(title="API do Projeto de TCC")

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
        

