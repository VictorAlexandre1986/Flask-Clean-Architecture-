from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.login import LoginUser

def get_db():
    from app import db  # Importa db somente quando necessário
    return db



class User(get_db().Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}  # Extende a definição existente da tabela

    id = get_db().Column(get_db().Integer, primary_key=True)
    name = get_db().Column(get_db().String(50), nullable=False)
    email = get_db().Column(get_db().String(100), unique=True, nullable=False)
    photo = get_db().Column(get_db().String(100), nullable=True)
    phoneNumber = get_db().Column(get_db().String(11), unique=True, nullable=False)
    id_login = get_db().Column(get_db().Integer, get_db().ForeignKey('login_user.id'), nullable=False)

    # Relacionamento com LoginUser
    # login = get_db().relationship('LoginUser', backref='user')

    def __init__(self, name, email, photo, phoneNumber, id_login):
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.photo = photo
        self.id_login = id_login

    def __repr__(self):
        return f'<User {self.name}>'
