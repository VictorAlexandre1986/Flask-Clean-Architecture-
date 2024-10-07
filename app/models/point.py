from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from app.models.user import User

def get_db():
    from app import db  # Importa db somente quando necessário
    return db

class Point(get_db().Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    photo = Column(String(100) , nullable=True)
    id_user = Column(Integer, get_db().ForeignKey('user.id'), nullable=False)
    total_hours = Column(Float, nullable=False)

    # Relacionamento com User
    user = relationship(User, backref='point')

    def __init__(self, date, photo, id_user, total_hours):
        self.date = date
        self.photo = photo
        self.id_user = id_user
        self.total_hours = total_hours

    def __repr__(self):
        return f'<Id User {self.id_user} Date {self.date} Photo {self.photo} Total Hours {self.total_hours}>'
