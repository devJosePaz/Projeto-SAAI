from pydantic import BaseModel, Field
from typing import Optional

# --- Schemas para Autenticação (Usuários e Token) ---

# Schema para criação de um novo usuário (recebe username e password)
class UserCreate(BaseModel):
    username: str 
    password: str 

# Schema para login de usuário (recebe username e password)
class UserLogin(BaseModel):
    username: str
    password: str

# Schema para a resposta de um usuário (não inclui a senha hash)
class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True 

# Schema para os dados contidos no token JWT
class TokenData(BaseModel):
    username: Optional[str] = None 

# --- Schemas para Planos de Estudo ---

class StudyPlanBase(BaseModel):
    theme: str 
    daily_time: int 
    objective: str 
    learning_style: str 


class StudyPlanCreate(StudyPlanBase):
    pass

class StudyPlanResponse(StudyPlanBase):
    id: int 
    owner_id: int 

    class Config:
        from_attributes = True
