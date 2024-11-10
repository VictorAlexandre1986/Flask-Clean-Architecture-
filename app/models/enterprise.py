from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.models.login_enterprise import LoginEnterprise
from app.models.user import User

def get_db():
    from app import db  # Importa db somente quando necessário
    return db

class Enterprise(get_db().Model):
    __tablename__ = 'enterprise'

    id = get_db().Column(get_db().Integer, primary_key=True)
    name = get_db().Column(get_db().String(50), nullable=False)
    email = get_db().Column(get_db().String(100), unique=True, nullable=False)
    phoneNumber = get_db().Column(get_db().String(11), unique=True, nullable=False)
    address = get_db().Column(get_db().String(100), nullable=False)
    city = get_db().Column(get_db().String(50), nullable=False)
    state = get_db().Column(get_db().String(2), nullable=False)
    cep = get_db().Column(get_db().String(8), nullable=False)
    number = get_db().Column(get_db().String(10), nullable=False)
    complement = get_db().Column(get_db().String(50), nullable=False)
    cnpj = get_db().Column(get_db().String(14), unique=True, nullable=False)
    status = get_db().Column(get_db().Boolean, nullable=False)
    id_login = get_db().Column(get_db().Integer, get_db().ForeignKey('login_enterprise.id'), nullable=False)

        # Relacionamento com Login
    login = relationship(LoginEnterprise, backref='enterprise',uselist=False)

    def __init__(self, name, email, phoneNumber, id_login, address, city, state, cep, number, complement, cnpj, status):
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.address = address
        self.city = city
        self.state = state
        self.cep = cep
        self.number = number
        self.complement = complement
        self.cnpj = cnpj
        self.status = status
        self.id_login = id_login

    def __repr__(self):
        return f'<User {self.name}>'
