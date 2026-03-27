import os
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return os.getenv("HELLO_TEXT") or "Hello from Effective Mobile!"
