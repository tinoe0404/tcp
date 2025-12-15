from fastapi import APIRouter, Depends

from app.core.security import get_current_user

router = APIRouter()

@router.get("/protected")
def protected_route(user: dict = Depends(get_current_user)):
    return {
        "message": "Access granted",
        "user": user["username"],
    }
