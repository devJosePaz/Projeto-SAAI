from fastapi import APIRouter, Request, Depends, Form
from sqlalchemy.orm import Session
from models import User
from database import get_db

router = APIRouter()

@router.post('/login')
async def processar_login(db: Session = Depends(get_db), username: str = Form(...), password: str = Form(...)):
    usuario_existente = db.query(User.username).filter(User.username == username).first()
    if usuario_existente:
        pass

    
@router.post('/cadastro')
async def processar_cadastro(db: Session = Depends(get_db), username: str = Form(...), password: str = Form(...)):
    pass
   
