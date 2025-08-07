from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.auth import models, schemas, utils


router = APIRouter(
    prefix="/auth",
    tags=["Autenticação"]
)

@router.post("/register", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="usuário já existente.")
    
    hashed_pw = utils.hash_password(user.password)
    new_user = models.User(email=user.email, hashed_password=hashed_pw)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login", response_model=schemas.TokenResponse, status_code=status.HTTP_200_OK)
def login(user_data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_data.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"erro: usuário '{user}' não encontrado.")
    
    if not utils.verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="erro: senha incorreta.")
    
    access_token = utils.create_access_token({"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}


