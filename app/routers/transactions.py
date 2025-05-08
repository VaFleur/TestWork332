from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, security
from app.database import get_db

router = APIRouter(tags=["Transactions"], prefix="/transactions")


@router.post("/", response_model=dict)
async def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db),
                             api_key: str = Depends(security.get_api_key)):
    if db.query(crud.models.Transaction).filter_by(transaction_id=transaction.transaction_id).first():
        raise HTTPException(status_code=400, detail="Transaction ID already exists")

    crud.create_transaction(db, transaction.dict())
    return {"message": "Transaction received"}


@router.delete("/", response_model=dict)
async def delete_transactions(db: Session = Depends(get_db), api_key: str = Depends(security.get_api_key)):
    crud.delete_all_transactions(db)
    return {"message": "Transactions deleted"}