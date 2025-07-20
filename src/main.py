from fastapi import FastAPI
from database import SessionLocal, engine
from src import models, crud

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/AdicionarUsuario/")
def adicionar_usuario(email: str, nome: str):
    db = SessionLocal()
    try:
        return crud.adicionar_usuario(db, email, nome)
    finally:
        db.close()

@app.delete("/RemoverUsuario/")
def remover_usuario(email: str):
    db = SessionLocal()
    try:
        return crud.remover_usuario(db, email)
    finally:
        db.close()

@app.post("/AdicionarPonto/")
def adicionar_ponto(latitude: float, longitude: float, email: str, descricao: str = ""):
    db = SessionLocal()
    try:
        return crud.adicionar_ponto(db, latitude, longitude, email, descricao)
    finally:
        db.close()

@app.delete("/RemoverPonto/")
def remover_ponto(id: str, user: str):
    db = SessionLocal()
    try:
        return crud.remover_ponto(db, id, user)
    finally:
        db.close()