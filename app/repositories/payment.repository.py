from app.models.payment import Payment,get_db


class PaymentRepository:
    def create(self, payment_data):
        db = get_db()
        payment = Payment(id_enterprise=payment_data.id_enterprise, date=payment_data.date, amount=payment_data.amount, type_payment=payment_data.type_payment, status_payment=payment_data.status_payment, transaction_id=payment_data.transaction_id, status_refund=payment_data.status_refund)
        db.session.add(payment)
        db.session.commit()
        return payment

    def get_by_id(self, payment_id):
        return Payment.query.get(payment_id)
    
    def get_all(self):
        return Payment.query.all()
    
    def update(self, payment_id, payment_data):
        db = get_db()
        payment = Payment.query.get(payment_id)
        if payment:
            payment.id_enterprise = payment_data.id_enterprise
            payment.date = payment_data.date
            payment.amount = payment_data.amount
            payment.type_payment = payment_data.type_payment
            payment.status_payment = payment_data.status_payment
            payment.transaction_id = payment_data.transaction_id
            payment.status_refund = payment_data.status_refund
            db.session.commit()
        return payment
    
    def delete(self, payment_id):
        db = get_db()
        payment = Payment.query.get(payment_id)
        if payment:
            db.session.delete(payment)
            db.session.commit()
        return payment
