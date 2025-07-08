# SAAI/backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.auth import routes as auth_routes
from backend.app.study_plans import routes as study_plans_routes # Certifique-se que esta linha existe
from backend.app.database import Base, engine

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    print("Tabelas do banco de dados criadas/verificadas.")

app.include_router(auth_routes.router)
app.include_router(study_plans_routes.router) # Certifique-se que esta linha existe

@app.get("/")
async def root():
    return {"message": "Bem-vindo ao SAAI Backend!"}
