from app.repositories.login_enterprise_repository import LoginEnterpriseRepository

class LoginEnterpriseUseCase:
    def __init__(self):
        self.login_enterprise_repository = LoginEnterpriseRepository()
    
    def create_login(self, login_data):
        return self.login_enterprise_repository.create(login_data)
    
    def get_login_by_id(self, login_id):
        return self.login_enterprise_repository.get_by_id(login_id)
    
    def get_all_logins(self):
        return self.login_enterprise_repository.get_all()
    
    def update_login(self, login_id, login_data):
        return self.login_enterprise_repository.update(login_id, login_data)
    
    def delete_login(self, login_id):
        return self.login_enterprise_repository.delete(login_id)