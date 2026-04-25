from fastapi import FastAPI
from app.routes import home 
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.include_router(home.router)

