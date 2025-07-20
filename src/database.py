from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# cria um banco de dados chamado geo.db
SQLLALCHEMY_DATABASE_URL = "sqlite:///./geo.db"

engine = create_engine(
    SQLLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
