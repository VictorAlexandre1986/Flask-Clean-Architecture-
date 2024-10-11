from app.repositories.login_repository import LoginRepository

class LoginUseCase:
    def __init__(self):
        self.login_repository = LoginRepository()
    
    def create_login(self, login_data):
        return self.login_repository.create(login_data)
    
    def get_login_by_id(self, login_id):
        return self.login_repository.get_by_id(login_id)
    
    def get_all_logins(self):
        return self.login_repository.get_all()
    
    def update_login(self, login_id, login_data):
        return self.login_repository.update(login_id, login_data)
    
    def delete_login(self, login_id):
        return self.login_repository.delete(login_id)