from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.models.login_enterprise import LoginEnterprise
from app.models.user import User

def get_db():
    from app import db  # Importa db somente quando necessário
    return db

class Enterprise(get_db().Model):
    __tablename__ = 'enterprise'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phoneNumber = Column(String(11), unique=True, nullable=False)
    address = Column(String(100), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(2), nullable=False)
    cep = Column(String(8), nullable=False)
    number = Column(String(10), nullable=False)
    complement = Column(String(50), nullable=False)
    cnpj = Column(String(14), unique=True, nullable=False)
    status = Column(Boolean, nullable=False)
    id_login = Column(Integer, get_db().ForeignKey('login_enterprise.id'), nullable=False)
    id_user = Column(Integer, get_db().ForeignKey('user.id'), nullable=False)

            # Relacionamento com Login
    user = relationship(User, backref='user')
        # Relacionamento com Login
    login = relationship(LoginEnterprise, backref='user')

    def __init__(self, name, email, phoneNumber, id_login, id_user, address, city, state, cep, number, complement, cnpj):
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
        self.id_login = id_login
        self.id_user = id_user

    def __repr__(self):
        return f'<User {self.name}>'
