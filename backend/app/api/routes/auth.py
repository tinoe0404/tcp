from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.security import (
    verify_password,
    hash_password,
    create_access_token,
)

router = APIRouter()

# 🔐 Hardcoded admin credentials for Stage 4
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD_HASH = hash_password("adminpass")


@router.post("/login")
async def login(
    username: str,
    password: str,
    db: AsyncSession = Depends(get_db),
):
    if username != ADMIN_USERNAME:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    if not verify_password(password, ADMIN_PASSWORD_HASH):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    access_token = create_access_token({"sub": username})

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
