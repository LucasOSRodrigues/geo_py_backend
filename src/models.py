from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base
import uuid

class Usuario(Base):
    __tablename__ = "usuarios"

    email = Column(String, primary_key=True, index=True)
    nome = Column(String)

    pontos = relationship("Ponto", back_populates="usuario")

class Ponto(Base):
    __tablename__ = "pontos"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    latitude = Column(Float)
    longitude = Column(Float)
    descricao = Column(String)

    usuario_email = Column(String, ForeignKey("usuarios.email"))
    usuario = relationship("Usuario", back_populates="pontos")
