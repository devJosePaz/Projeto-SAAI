# SAAI/backend/app/auth/dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from ..database import get_db 
from ..auth import models, schemas
from backend.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])

        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception

        expire_timestamp = payload.get("exp")
        if expire_timestamp:
            expire_datetime = datetime.fromtimestamp(expire_timestamp, tz=timezone.utc)
            if expire_datetime < datetime.now(timezone.utc):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token expirado",
                    headers={"WWW-Authenticate": "Bearer"},
                )

        token_data = schemas.TokenData(username=username) 
    except JWTError:
        raise credentials_exception

    user = db.query(models.User).filter(models.User.username == token_data.username).first()
    if user is None:
        raise credentials_exception

    return user