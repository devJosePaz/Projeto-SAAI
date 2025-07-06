from sqlalchemy import Column, Integer, String, DateTime, func
from backend.app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    create_at = Column(DateTime(timezone=True), server_default=func.now())