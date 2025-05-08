from celery import Celery
from app.crud import get_statistics
from app.database import SessionLocal
from dotenv import load_dotenv
import os

load_dotenv()

celery_app = Celery("tasks", broker=os.getenv("CELERY_BROKER_URL"))


@celery_app.task
def update_statistics():
    db = SessionLocal()
    try:
        stats = get_statistics(db)
        print("Updated statistics:", stats)
    finally:
        db.close()