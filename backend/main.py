from contextlib import asynccontextmanager
from http.client import HTTPException
from fastapi import FastAPI
from sqlmodel import select
from database_model import Item
from database import SessionDep, create_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield

app = FastAPI(title="FastAPI + PostgreSQL (SQLModel)", lifespan=lifespan) 
 
@app.get("/")
def root():
    return {"message": "Backend attivo"}
 
@app.get("/health/db")
def check_db(db: SessionDep):
    """Verifica che la connessione al database funzioni."""
    db.exec(select(1))
    return {"database": "connesso"}

@app.get("/items/")
def read_items(db: SessionDep) -> list[Item]:
    items = db.exec(select(Item)).all()
    return items

@app.post("/items/")
def create_item(item: Item, db: SessionDep) -> Item:
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@app.get("/items/{item_id}")
def read_hero(item_id: int, db: SessionDep) -> Item:
    item = db.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.delete("/items/{item_id}")
def delete_hero(item_id: int, db: SessionDep):
    item = db.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"ok": True}