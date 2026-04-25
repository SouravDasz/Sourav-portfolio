from fastapi import FastAPI,APIRouter,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.routes.home import templates

router=APIRouter()


@router.get("/about")
def about(request:Request):
    return templates.TemplateResponse(request,"about.html")