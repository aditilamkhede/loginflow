import logging
from datetime import datetime, timedelta

from sendgrid import SendGridAPIClient
import os
from sendgrid.helpers.mail import *
import settings

# import emails
# from emails.template import JinjaTemplate
from jose import jwt
import secrets;

EMAIL_RESET_TOKEN_EXPIRE_HOURS = 720
ALGORITHM = "HS256"
SECRET_KEY = secrets.token_urlsafe(32)

PROJECT_NAME="Formations"



def generate_password_reset_token(email: str) -> str:
    # delta = timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    delta = timedelta(hours=EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        # {"exp": exp, "nbf": now, "sub": email}, settings.SECRET_KEY, algorithm="HS256",
        {"exp": exp, "nbf": now, "sub": email}, SECRET_KEY, algorithm=ALGORITHM,
    )
    return encoded_jwt

def send_reset_password_email(email_to: str, email: str, token: str):
    server_host = settings.SERVER_HOST
    link = f"{server_host}/reset-password?token={token}"
    message = Mail(
    from_email=email,
    to_emails=email_to,
    subject='Password Recover Email for Choreowiz',
    html_content=f'<strong>Please click <a href="{link}">here</a> to reset your password.</strong></br> This is an auto generated email. Please do not reply to the sender.')
    try:
        print('message', message)
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        print('after api key from settings', settings.SENDGRID_API_KEY)
        response = sg.send(message)
        # print('after send')
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
    except Exception as e:
        print(e)
    return

def send_reset_password_email_old(email_to: str, email: str, token: str) -> None:
    project_name = PROJECT_NAME
    subject = f"{project_name} - Password recovery for user {email}"
    with open(Path(settings.EMAIL_TEMPLATES_DIR) / "reset_password.html") as f:
        template_str = f.read()
    server_host = settings.SERVER_HOST
    link = f"{server_host}/reset-password?token={token}"
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={
            "project_name": PROJECT_NAME,
            "username": email,
            "email": email_to,
            "valid_hours": EMAIL_RESET_TOKEN_EXPIRE_HOURS,
            "link": link,
        },
    )
