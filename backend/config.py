from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    
    JWT_SECRET: str
    JWT_ALGORITHM: str

    class Config:
        env_file = "backend/.env"

settings = Settings()
