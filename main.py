from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

import models
from database import engine, get_db
from routers import auth, transactions, categories
from dependencies import get_current_active_user

# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finanzas Personales")

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Incluir routers
app.include_router(auth.router, prefix="", tags=["autenticación"])
app.include_router(transactions.router, prefix="/transactions", tags=["transacciones"], dependencies=[Depends(get_current_active_user)])
app.include_router(categories.router, prefix="/categories", tags=["categorías"], dependencies=[Depends(get_current_active_user)])

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return RedirectResponse(url="/login")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
