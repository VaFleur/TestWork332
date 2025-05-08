from sqlalchemy.orm import Session
from app.models import Transaction
from app.utils import find_top_transactions


def create_transaction(db: Session, transaction: dict):
    db_transaction = Transaction(**transaction)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def delete_all_transactions(db: Session):
    db.query(Transaction).delete()
    db.commit()


def get_statistics(db: Session):
    transactions = db.query(Transaction).all()

    total_transactions = len(transactions)
    current_mean = 0.0

    for i, tx in enumerate(transactions, start=1):
        current_mean += (tx.amount - current_mean) / i

    transactions_data = [{"transaction_id": tx.transaction_id, "amount": tx.amount} for tx in transactions]
    top_transactions = find_top_transactions(transactions_data, n=3)

    return {
        "total_transactions": total_transactions,
        "average_transaction_amount": round(current_mean, 2),
        "top_transactions": top_transactions
    }