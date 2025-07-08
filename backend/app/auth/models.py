# SAAI/backend/app/auth/models.py
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey # Adicionado DateTime e func
from sqlalchemy.orm import relationship
from ..database import Base # Importa Base do seu database.py

# Seu modelo User existente
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    create_at = Column(DateTime(timezone=True), server_default=func.now()) # Sua coluna existente

    study_plans = relationship("StudyPlan", back_populates="owner")

# Seu novo modelo StudyPlan
class StudyPlan(Base):
    __tablename__ = "study_plans"

    id = Column(Integer, primary_key=True, index=True)
    theme = Column(String, index=True)
    daily_time = Column(Integer)
    objective = Column(String)
    learning_style = Column(String)

    owner_id = Column(Integer, ForeignKey("users.id")) 

    owner = relationship("User", back_populates="study_plans")
