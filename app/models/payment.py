from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from app.models.enterprise import Enterprise

def get_db():
    from app import db  # Importa db somente quando necessário
    return db

class Payment(get_db().Model):
    __tablename__ = 'payment'

    id = Column(Integer, primary_key=True)
    id_enterprise = Column(Integer, get_db().ForeignKey('enterprise.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    amount = Column(Float, nullable=False)
    type_payment = Column(String(50), nullable=False) # Credito, Debito
    status_payment = Column(String(50), nullable=False) # Pendente, Pago, Cancelado
    transaction_id = Column(String(50), nullable=False, unique=True) # Recebe do stripe
    status_refund = Column(String(50), nullable=False) # Reembolso total, Nao Reembolso, Reembolso Parcial
        # Relacionamento com Login
    enterprise = relationship(Enterprise, backref='user')

    def __init__(self, id_enterprise, date, amount, type_payment, status_payment, transaction_id, status_refund):
        self.id_enterprise = id_enterprise
        self.date = date
        self.amount = amount
        self.type_payment = type_payment
        self.status_payment = status_payment
        self.transaction_id = transaction_id
        self.status_refund = status_refund

    def __repr__(self):
        return f'<Id Enterprise {self.id_enterprise} Date {self.date} Amount {self.amount} Type Payment {self.type_payment} Status Payment {self.status_payment} Transaction Id {self.transaction_id} Status Refund {self.status_refund}>'
