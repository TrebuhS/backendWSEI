from fastapi import APIRouter

router = APIRouter()


@router.get("/auth")
def verify_token():
    return 1
