from sqlalchemy import Column, Integer, String

def get_db():
    from app import db  # Importa db somente quando necessário
    return db

class LoginUser(get_db().Model):
    __tablename__ = 'login_user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), unique=True, nullable=False)
    user = get_db().relationship('User', backref='login_user', uselist=False)    # Relacionamento com User (uselist=False garante relacionamento um-para-um)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f'<Login {self.username}>'