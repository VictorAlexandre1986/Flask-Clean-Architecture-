from flask import request, jsonify
from app.usecases.payment  import PaymentUseCase
from app.dto.payment import PaymentDTO
from app.entities.payment import PaymentEntity

class PaymentController:
    def __init__(self):
        self.payment_usecase = PaymentUseCase()

    def create_user(self):
        data = request.get_json()
        payment_dto = PaymentDTO(**data)
        payment = self.payment_usecase.create_payment(payment_dto)
        return jsonify({'id': payment.id, 'id_enterprise': payment.id_enterprise, 'date': payment.date, 'amount': payment.amount, 'type_payment': payment.type_payment, 'status_payment': payment.status_payment, 'transaction_id': payment.transaction_id, 'status_refund': payment.status_refund})

    def get_payment_by_id(self, user_id):
        payment = self.payment_usecase.get_payment_by_id(user_id)
        if payment:
            return jsonify({'id': payment.id, 'id_enterprise': payment.id_enterprise, 'date': payment.date, 'amount': payment.amount, 'type_payment': payment.type_payment, 'status_payment': payment.status_payment, 'transaction_id': payment.transaction_id, 'status_refund': payment.status_refund})
            
        return jsonify({'message': 'Payment not found'}), 404

    def get_all_payments(self):
        payments = self.payments_usecase.get_all_payments()
        if payments:
            return jsonify([{'id': payment.id, 'id_enterprise': payment.id_enterprise, 'date': payment.date, 'amount': payment.amount, 'type_payment': payment.type_payment, 'status_payment': payment.status_payment, 'transaction_id': payment.transaction_id, 'status_refund': payment.status_refund} for payment in payments])
        return jsonify({'message': 'No payments found'}), 404

    def update_payment(self, payment_id):
        data = request.get_json()
        payment_dto = PaymentDTO(**data)
        payment = self.payment_usecase.update_payment(payment_id, payment_dto)
        if payment:
            return jsonify({'id': payment.id, 'id_enterprise': payment.id_enterprise, 'date': payment.date, 'amount': payment.amount, 'type_payment': payment.type_payment, 'status_payment': payment.status_payment, 'transaction_id': payment.transaction_id, 'status_refund': payment.status_refund})
        return jsonify({'message': 'Payment not found'}), 404
    
    def delete_payment(self, payment_id):
        payment = self.payment_usecase.delete_payment(payment_id)
        if payment:
            return jsonify({'message': 'Payment deleted'})
        return jsonify({'message': 'Payment not found'}), 404
