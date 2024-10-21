from flask import request, jsonify
from app.usecases.login_enterprise  import LoginEnterpriseUseCase
from app.dto.login_enterprise import LoginEnterpriseDTO

class LoginEnterpriseController:
    def __init__(self):
        self.login_enterprise_usecase = LoginEnterpriseUseCase()

    def create_login(self):
        data = request.get_json()
        login_dto = LoginEnterpriseDTO(**data)
        login = self.login_enterprise_usecase.create_login(login_dto)
        return jsonify({'id': login.id, 'username': login.username, 'password': login.password, 'email': login.email})

    def get_login_by_id(self, login_id):
        login = self.login_enterprise_usecase.get_login_by_id(login_id)
        if login:
            return jsonify({'id': login.id, 'username': login.username, 'password': login.password, 'email': login.email})
        return jsonify({'message': 'Login not found'}), 404

    def get_all_logins(self):
        logins = self.login_enterprise_usecase.get_all_logins()
        return jsonify([{'id': login.id, 'username': login.username, 'password': login.password ,'email': login.email} for login in logins])
    
    def update_login(self, user_id):
        data = request.get_json()
        login_dto = LoginEnterpriseDTO(**data)
        login = self.login_enterprise_usecase.update_login(user_id, login_dto)
        if login:
            return jsonify({'id': login.id, 'username': login.username, 'password': login.password ,'email': login.email})
        return jsonify({'message': 'Login not found'}), 404
    
    def delete_login(self, login_id):
        login = self.login_enterprise_usecase.delete_user(login_id)
        if login:
            return jsonify({'message': 'Login deleted'})
        return jsonify({'message': 'Login not found'}), 404
