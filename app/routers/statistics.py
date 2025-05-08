from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, security
from app.database import get_db

router = APIRouter(tags=["Statistics"], prefix="/statistics")

@router.get("/", response_model=dict)
async def get_statistics_endpoint(db: Session = Depends(get_db), api_key: str = Depends(security.get_api_key)):
    stats = crud.get_statistics(db)
    return stats