from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.auth import models, schemas, utils

router = APIRouter(
    prefix="/auth",
    tags=["Autenticação"]
)

@router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="usuário já existente.")
    
    hashed_pw = utils.hash_password(user.password)
    new_user = models.User(username=user.username, hashed_password=hashed_pw)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login")
def login(data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == data.username).first()

    if not user:
        raise HTTPException(status_code=400, detail="usuário não encontrado.")
    
    if not utils.verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="senha incorreta.")
    
    access_token = utils.create_access_token({"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}


