import uuid
from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.database import Base


class StudyPlan(Base):
    __tablename__ = "study_plans"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    theme: Mapped[str] = mapped_column(String(80), nullable=False)
    daily_time: Mapped[int] = mapped_column(nullable=False)
    objective: Mapped[str] = mapped_column(String(100), nullable=False)
    learning_style: Mapped[str] = mapped_column(String(80), nullable=False)

    owner_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"))
    owner = relationship("User", back_populates="study_plans")
