import uuid
import datetime
from sqlalchemy import String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from backend.app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    create_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    study_plans = relationship("StudyPlan", back_populates="owner")


class StudyPlan(Base):
    __tablename__ = "study_plans"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    theme: Mapped[str] = mapped_column(String(80), nullable=False)
    daily_time: Mapped[int] = mapped_column(nullable=False)
    objective: Mapped[str] = mapped_column(String(100), nullable=False)
    learning_style: Mapped[str] = mapped_column(String(80), nullable=False)

    owner_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"))
    owner = relationship("User", back_populates="study_plans")
