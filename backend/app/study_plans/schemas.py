from pydantic import BaseModel
from uuid import UUID

class StudyPlanCreate(BaseModel):
    theme: str 
    daily_time: int 
    objective: str 
    learning_style: str 
    

class StudyPlanResponse(BaseModel):
    id: UUID 
    owner_id: int 

    class Config:
        from_attributes = True
