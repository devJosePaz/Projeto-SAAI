from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.dependencies import get_current_user 

from app.auth import models as auth_models
from app.auth import schemas as auth_schemas
from app.study_plans.models import StudyPlan
from app.study_plans.schemas import StudyPlanCreate, StudyPlanResponse

router = APIRouter(
    prefix="/study_plans",
    tags=["Planos de Estudo"]
)

@router.post("/", response_model=StudyPlanResponse, status_code=status.HTTP_201_CREATED)
def create_study_plan(
    study_plan: StudyPlanCreate,
    current_user: auth_models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_study_plan = StudyPlan(
        theme=study_plan.theme,
        daily_time=study_plan.daily_time,
        objective=study_plan.objective,
        learning_style=study_plan.learning_style,
        owner_id=current_user.id
    )
    db.add(db_study_plan)
    db.commit()
    db.refresh(db_study_plan)

    return db_study_plan