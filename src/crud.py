from fastapi import HTTPException
from sqlalchemy.orm import Session
from src import models

def adicionar_usuario(db: Session, email: str, nome: str):
    usuario = db.query(models.Usuario).filter_by(email=email).first()
    if usuario:
        raise HTTPException(status_code=409, detail="Usuário já existe")
    novo_usuario = models.Usuario(email=email, nome=nome)
    db.add(novo_usuario)
    db.commit()
    return {"mensagem": "Usuário criado com sucesso"}

def remover_usuario(db: Session, email: str):
    usuario = db.query(models.Usuario).filter_by(email=email).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(usuario)
    db.commit()
    return {"mensagem": "Usuário removido com sucesso"}

def adicionar_ponto(db: Session, latitude: float, longitude: float, email: str, descricao: str = ""):
    usuario = db.query(models.Usuario).filter_by(email=email).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    ponto = models.Ponto(latitude=latitude, longitude=longitude, usuario_email=email, descricao=descricao)
    db.add(ponto)
    db.commit()
    return {"mensagem": "Ponto adicionado com sucesso", "id": ponto.id}

def remover_ponto(db: Session, id: str, user: str):
    # busca o usuario com o nome fornecido
    user = db.query(models.Usuario).filter_by(nome=user).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # busca o email do usuario
    user_email = user.email
    # busca o ponto com o id do ponto e email do user
    ponto = db.query(models.Ponto).filter_by(id=id, usuario_email=user_email).first()
    if not ponto:
        raise HTTPException(status_code=404, detail="Ponto não encontrado")
    db.delete(ponto)
    db.commit()
    return {"mensagem": "Ponto removido com sucesso"}
