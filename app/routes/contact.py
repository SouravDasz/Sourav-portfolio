from fastapi import APIRouter, Request, Form
from app.routes.home import templates
import smtplib
from email.message import EmailMessage
router = APIRouter()

@router.post("/contact/mail")
def mailsend(request: Request, name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    email_sender = "sourav177official@gmail.com"
    email_password = "jffd fskx tbxl syjh"

    email_receiver = "sourav177official@gmail.com"
    msg = EmailMessage()
    msg["Subject"] = f"A email form {name}"
    msg["From"] = email_sender
    msg["To"] = email_receiver
    body=f"""
    Hi
    I am {name}
    Email : {email}
    message : {message}
"""
    msg.set_content(body)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

        smtp.starttls()

        smtp.login(email_sender, email_password)

        smtp.send_message(msg)

    return templates.TemplateResponse("maildone.html", {"request": request})

@router.get("/contact")
def contect(request: Request):
    return templates.TemplateResponse(request, 'contact.html')