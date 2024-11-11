from app.repositories.payment_repository import PaymentRepository

class PaymentUseCase:
    def __init__(self):
        self.payment_repository = PaymentRepository()
    
    def create_payment(self, payment_data):
        return self.payment_repository.create(payment_data)
    
    def get_payment_by_id(self, payment_id):
        return self.payment_repository.get_by_id(payment_id)
    
    def get_all_payments(self):
        return self.payment_repository.get_all()
    
    def update_payment(self, payment_id, payment_data):
        return self.payment_repository.update(payment_id, payment_data)
    
    def delete_payment(self, payment_id):
        return self.payment_repository.delete(payment_id)