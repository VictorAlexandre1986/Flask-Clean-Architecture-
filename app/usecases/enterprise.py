from app.repositories.enterprise_repository import EnterpriseRepository

class EnterpriseUseCase:
    def __init__(self):
        self.enterprise_repository = EnterpriseRepository()
    
    def create_enterprise(self, login_data):
        return self.enterprise_repository.create(login_data)
    
    def get_enterprise_by_id(self, login_id):
        return self.enterprise_repository.get_by_id(login_id)
    
    def get_all_enterprises(self):
        return self.enterprise_repository.get_all()
    
    def update_enterprise(self, login_id, login_data):
        return self.enterprise_repository.update(login_id, login_data)
    
    def delete_enterprise(self, login_id):
        return self.enterprise_repository.delete(login_id)