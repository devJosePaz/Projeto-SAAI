from pydantic import BaseModel

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
