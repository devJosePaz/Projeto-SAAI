from pydantic import BaseModel, Field
from typing import Optional

class UserCreate(BaseModel):
    username: str 
    password: str 

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True 

# Schema para os dados contidos no token JWT
class TokenData(BaseModel):
    username: Optional[str] = None 

