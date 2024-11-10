from app.repositories.enterprise_repository import EnterpriseRepository

class EnterpriseUseCase:
    def __init__(self):
        self.enterprise_repository = EnterpriseRepository()
    
    def create_enterprise(self, enterprise_data):
        return self.enterprise_repository.create(enterprise_data)
    
    def get_enterprise_by_id(self, enterprise_id):
        return self.enterprise_repository.get_by_id(enterprise_id)
    
    def get_all_enterprises(self):
        return self.enterprise_repository.get_all()
    
    def update_enterprise(self, enterprise_id, enterprise_data):
        return self.enterprise_repository.update(enterprise_id, enterprise_data)
    
    def delete_enterprise(self, enterprise_id):
        return self.enterprise_repository.delete(enterprise_id)