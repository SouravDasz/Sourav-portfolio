from fastapi import FastAPI
from app.routes import home 
from fastapi.staticfiles import StaticFiles
from app.routes import about
app = FastAPI()

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(home.router)
app.include_router(about.router)

