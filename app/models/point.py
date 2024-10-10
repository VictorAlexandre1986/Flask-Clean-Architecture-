from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from app.models.user import User

def get_db():
    from app import db  # Importa db somente quando necessário
    return db


class Point(get_db().Model):
    __tablename__ = 'point'  # Corrigido para refletir o nome correto da tabela

    id = get_db().Column(get_db().Integer, primary_key=True)
    date = get_db().Column(get_db().DateTime, nullable=False)
    photo = get_db().Column(get_db().String(100), nullable=True)
    id_user = get_db().Column(get_db().Integer, get_db().ForeignKey('user.id'), nullable=False)
    total_hours = get_db().Column(get_db().Float, nullable=False)

    # Relacionamento com User
    user = get_db().relationship('User', backref='points')  # 'points' é o plural para relacionamento

    def __init__(self, date, photo, id_user, total_hours):
        self.date = date
        self.photo = photo
        self.id_user = id_user
        self.total_hours = total_hours

    def __repr__(self):
        return f'<Id User {self.id_user} Date {self.date} Photo {self.photo} Total Hours {self.total_hours}>'
