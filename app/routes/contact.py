from fastapi import APIRouter,Request
from fastapi.responses import HTMLResponse
from app.routes.home import templates

router=APIRouter()


@router.get("/contact")
def contect(request:Request):
    if request.method=="GET":
        return templates.TemplateResponse(request,'contact.html')