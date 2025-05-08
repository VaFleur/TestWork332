from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import transactions, statistics

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(transactions.router)
app.include_router(statistics.router)