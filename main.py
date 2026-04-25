from fastapi import FastAPI,Request
from app.routes import home 
from fastapi.staticfiles import StaticFiles
from app.routes import about
from app.routes import projects
from app.routes import contact
from app.routes import resume
from app.routes.home import templates
app = FastAPI()

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(home.router)
app.include_router(about.router)
app.include_router(projects.router)
app.include_router(contact.router)
app.include_router(resume.router)


@app.exception_handler(404)
async def custom_404(request: Request, exc):
    return templates.TemplateResponse(
        request,                 
        "p404.html",             
        {"request": request},    
        status_code=404
    )

