from sqlalchemy import Column, Integer, String

def get_db():
    from app import db  # Importa db somente quando necessário
    return db

class User(get_db().Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
