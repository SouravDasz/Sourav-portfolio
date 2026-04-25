from fastapi import APIRouter,Request
from fastapi.responses import HTMLResponse
from app.routes.home import templates

router=APIRouter()

@router.get("/resume")
def resume(request:Request):
    return templates.TemplateResponse(request,"resume.html")