from celery import Celery
from app.crud import get_statistics
from app.database import SessionLocal

celery_app = Celery("tasks", broker="redis://redis:6379/0")


@celery_app.task
def update_statistics():
    db = SessionLocal()
    try:
        stats = get_statistics(db)
        print("Updated statistics:", stats)
    finally:
        db.close()