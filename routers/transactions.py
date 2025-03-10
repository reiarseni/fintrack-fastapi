from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime

import crud
import schemas
import models
from database import get_db
from dependencies import get_current_active_user

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def read_transactions(
    request: Request,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    transactions = crud.get_transactions(db, user_id=current_user.id)
    return templates.TemplateResponse(
        "transactions/list.html", 
        {"request": request, "transactions": transactions, "user": current_user}
    )

@router.get("/create")
async def create_transaction_form(
    request: Request, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    categories = crud.get_categories(db, user_id=current_user.id)
    return templates.TemplateResponse(
        "transactions/form.html", 
        {"request": request, "categories": categories, "user": current_user}
    )

@router.post("/create")
async def create_transaction(
    amount: float = Form(...),
    description: str = Form(...),
    type: str = Form(...),
    category_id: int = Form(...),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    transaction_data = schemas.TransactionCreate(
        amount=amount, description=description, type=type, category_id=category_id
    )
    crud.create_transaction(db=db, transaction=transaction_data, user_id=current_user.id)
    return RedirectResponse(url="/transactions/", status_code=303)

@router.get("/edit/{transaction_id}")
async def edit_transaction_form(
    request: Request,
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    transaction = crud.get_transaction(db, transaction_id=transaction_id, user_id=current_user.id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    categories = crud.get_categories(db, user_id=current_user.id)
    return templates.TemplateResponse(
        "transactions/form.html", 
        {"request": request, "transaction": transaction, "categories": categories, "user": current_user}
    )

@router.post("/edit/{transaction_id}")
async def update_transaction(
    transaction_id: int,
    amount: float = Form(...),
    description: str = Form(...),
    type: str = Form(...),
    category_id: int = Form(...),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    transaction_data = schemas.TransactionCreate(
        amount=amount, description=description, type=type, category_id=category_id
    )
    updated_transaction = crud.update_transaction(
        db=db, transaction_id=transaction_id, transaction=transaction_data, user_id=current_user.id
    )
    if not updated_transaction:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    return RedirectResponse(url="/transactions/", status_code=303)

@router.get("/delete/{transaction_id}")
async def delete_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    deleted = crud.delete_transaction(db=db, transaction_id=transaction_id, user_id=current_user.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    return RedirectResponse(url="/transactions/", status_code=303)
