from fastapi import FastAPI
from sqlmodel import select
 
from database import SessionDep
 
app = FastAPI(title="FastAPI + PostgreSQL (SQLModel)")
 
 
@app.get("/")
def root():
    return {"message": "Backend attivo"}
 
 
@app.get("/health/db")
def check_db(db: SessionDep):
    """Verifica che la connessione al database funzioni."""
    db.exec(select(1))
    return {"database": "connesso"}