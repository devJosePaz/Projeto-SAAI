from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class UserCreate(BaseModel):
    email: str 
    password: str 

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: UUID
    email: str

    class Config:
        from_attributes = True 


class TokenData(BaseModel):
    email: Optional[str] = None 

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

