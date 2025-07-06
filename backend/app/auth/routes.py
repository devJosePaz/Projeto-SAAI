from fastapi import APIRouter, Request, Depends, Form
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

@router.post('/register')
async def processar_cadastro(db: Session = Depends(get_db), username: str = Form(...), password: str = Form(...)):
    pass
   
