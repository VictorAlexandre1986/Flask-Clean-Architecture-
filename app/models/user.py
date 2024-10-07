from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.login import Login

def get_db():
    from app import db  # Importa db somente quando necessário
    return db

class User(get_db().Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    photo = Column(String(100) , nullable=True)
    phoneNumber = Column(String(11), unique=True, nullable=False)
    id_login = Column(Integer, get_db().ForeignKey('login.id'), nullable=False)

        # Relacionamento com Login
    login = relationship(Login, backref='user')

    def __init__(self, name, email, phoneNumber, id_login):
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.id_login = id_login

    def __repr__(self):
        return f'<User {self.name}>'
