from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status, Request, Response, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import get_db
from auth import authenticate_user, create_access_token
from config import settings

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})

@router.post("/login")
async def login_for_access_token(
    response: Response,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, username, password)
    if not user:
        return templates.TemplateResponse(
            "auth/login.html", 
            {"request": Request, "error": "Nombre de usuario o contraseña incorrectos"}
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    
    response = RedirectResponse(url="/transactions/", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(
        key="session_token",
        value=access_token,
        httponly=True,
        max_age=1800,
        expires=1800,
    )
    
    return response

@router.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse("auth/register.html", {"request": request})

@router.post("/register")
async def register_user(
    request: Request,
    email: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    db_user_email = crud.get_user_by_email(db, email=email)
    if db_user_email:
        return templates.TemplateResponse(
            "auth/register.html", 
            {"request": request, "error": "El correo electrónico ya está registrado"}
        )
    
    db_user_username = crud.get_user_by_username(db, username=username)
    if db_user_username:
        return templates.TemplateResponse(
            "auth/register.html", 
            {"request": request, "error": "El nombre de usuario ya está registrado"}
        )
    
    user = schemas.UserCreate(email=email, username=username, password=password)
    crud.create_user(db=db, user=user)
    
    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/logout")
async def logout(response: Response):
    response = RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
    response.delete_cookie(key="session_token")
    return response
